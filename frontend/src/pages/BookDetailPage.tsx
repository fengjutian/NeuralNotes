import { useState } from "react"
import { useParams, useNavigate } from "react-router-dom"
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import {
  Card, Spin, Typography, Button, Empty, List, Space, Tag,
  message, Modal, Input, Alert, Form, Tooltip
} from "antd"
import {
  ArrowLeftOutlined, DeleteOutlined, LinkOutlined,
  EditOutlined, RobotOutlined, SearchOutlined
} from "@ant-design/icons"
import { bookApi, analyzeApi, type Book } from "../api"
import dayjs from "dayjs"

const { Title, Text, Paragraph } = Typography

export default function BookDetailPage() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const queryClient = useQueryClient()

  const [editMode, setEditMode] = useState(false)
  const [highlightSearch, setHighlightSearch] = useState("")
  const [analyzing, setAnalyzing] = useState(false)
  const [form] = Form.useForm()

  const { data: bookData, isLoading, error, refetch } = useQuery({
    queryKey: ["book", id],
    queryFn: () => bookApi.get(id!),
    enabled: !!id,
  })

  const { data: highlightsData } = useQuery({
    queryKey: ["book", id, "highlights"],
    queryFn: () => bookApi.getHighlights(id!, { page_size: 500 }),
    enabled: !!id,
  })

  const deleteMutation = useMutation({
    mutationFn: () => bookApi.delete(id!),
    onSuccess: () => {
      message.success("删除成功")
      navigate("/books")
    },
    onError: () => {
      message.error("删除失败")
    },
  })

  const updateMutation = useMutation({
    mutationFn: (data: Partial<Book>) => bookApi.update(id!, data),
    onSuccess: () => {
      message.success("更新成功")
      setEditMode(false)
      queryClient.invalidateQueries({ queryKey: ["book", id] })
    },
    onError: (err: any) => {
      message.error("更新失败: " + (err?.response?.data?.detail || err.message))
    },
  })

  const handleDelete = () => {
    Modal.confirm({
      title: "确认删除",
      content: "确定要删除这本书吗？所有笔记也将被删除。",
      okText: "确认",
      cancelText: "取消",
      onOk: () => deleteMutation.mutate(),
    })
  }

  const handleAnalyze = async () => {
    setAnalyzing(true)
    try {
      message.loading("AI 正在分析中，请稍候...", 0)
      const response = await analyzeApi.trigger({ book_id: id! })
      const analyzedCount = (response.data as any)?.total || 0
      message.destroy()
      message.success(`AI 分析完成！已分析 ${analyzedCount} 条笔记`)
    } catch (err: any) {
      message.destroy()
      message.error("分析失败: " + (err?.response?.data?.detail || err.message || "请稍后重试"))
    } finally {
      setAnalyzing(false)
    }
  }

  const startEdit = () => {
    if (!book) return
    form.setFieldsValue({
      title: book.title,
      author: book.author,
      category: book.category || "",
      reading_time: book.reading_time || "",
      progress: book.progress || 0,
    })
    setEditMode(true)
  }

  const handleEditSubmit = () => {
    form.validateFields().then((values) => {
      updateMutation.mutate(values)
    })
  }

  if (isLoading) {
    return (
      <div style={{ textAlign: "center", padding: 50 }}>
        <Spin size="large" />
      </div>
    )
  }

  if (error) {
    return (
      <div>
        <Button icon={<ArrowLeftOutlined />} onClick={() => navigate("/books")}>
          返回书架
        </Button>
        <Alert
          type="error"
          message="加载失败"
          description={(error as Error)?.message || "无法加载书籍信息"}
          showIcon
          action={
            <Button onClick={() => refetch()}>重试</Button>
          }
          style={{ marginTop: 16 }}
        />
      </div>
    )
  }

  const book = bookData?.data

  if (!book) {
    return (
      <div>
        <Button icon={<ArrowLeftOutlined />} onClick={() => navigate("/books")}>
          返回书架
        </Button>
        <Empty description="书籍不存在" style={{ marginTop: 40 }} />
      </div>
    )
  }

  const highlights = highlightsData?.data?.items || []

  const filteredHighlights = highlightSearch.trim()
    ? highlights.filter((h: any) =>
        h.content.toLowerCase().includes(highlightSearch.toLowerCase()) ||
        (h.chapter && h.chapter.toLowerCase().includes(highlightSearch.toLowerCase()))
      )
    : highlights

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 8, marginBottom: 16 }}>
        <Button icon={<ArrowLeftOutlined />} onClick={() => navigate("/books")}>
          返回书架
        </Button>
        <Space wrap>
          <Tooltip title="AI 分析笔记概念">
            <Button
              icon={<RobotOutlined />}
              onClick={handleAnalyze}
              loading={analyzing}
            >
              AI 分析
            </Button>
          </Tooltip>
          <Button
            icon={<EditOutlined />}
            onClick={editMode ? () => setEditMode(false) : startEdit}
          >
            {editMode ? "取消编辑" : "编辑信息"}
          </Button>
          <Button
            danger
            icon={<DeleteOutlined />}
            onClick={handleDelete}
            loading={deleteMutation.isPending}
          >
            删除
          </Button>
        </Space>
      </div>

      <Card style={{ marginTop: 0 }}>
        {editMode ? (
          <Form form={form} layout="vertical">
            <Space direction="vertical" style={{ width: "100%" }}>
              <Form.Item name="title" label="书名" rules={[{ required: true, message: "请输入书名" }]}>
                <Input />
              </Form.Item>
              <Form.Item name="author" label="作者">
                <Input />
              </Form.Item>
              <Form.Item name="category" label="分类">
                <Input />
              </Form.Item>
              <Form.Item name="reading_time" label="阅读时长">
                <Input placeholder="如: 3小时20分钟" />
              </Form.Item>
              <Form.Item name="progress" label="阅读进度 (%)">
                <Input type="number" min={0} max={100} />
              </Form.Item>
              <Button type="primary" onClick={handleEditSubmit} loading={updateMutation.isPending}>
                保存修改
              </Button>
            </Space>
          </Form>
        ) : (
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", flexWrap: "wrap", gap: 16 }}>
            <div>
              <Title level={2} style={{ marginBottom: 8 }}>{book.title}</Title>
              <Text type="secondary" style={{ fontSize: 16 }}>{book.author}</Text>
              <br /><br />
              <Space wrap>
                {book.category && <Tag color="blue">{book.category}</Tag>}
                {book.reading_time && <Tag>{book.reading_time}</Tag>}
                {book.progress !== undefined && (
                  <Tag color="green">进度 {book.progress}%</Tag>
                )}
                <Text type="secondary" style={{ fontSize: 12 }}>
                  导入于 {dayjs(book.created_at).format("YYYY-MM-DD HH:mm")}
                </Text>
              </Space>
            </div>
          </div>
        )}
      </Card>

      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: 24, flexWrap: "wrap", gap: 8 }}>
        <Title level={4} style={{ margin: 0 }}>
          我的笔记 ({filteredHighlights.length}{highlightSearch ? ` / ${highlights.length}` : ""})
        </Title>
        <Input.Search
          placeholder="搜索笔记内容或章节..."
          allowClear
          onSearch={(v) => setHighlightSearch(v)}
          onChange={(e) => { if (!e.target.value) setHighlightSearch("") }}
          style={{ width: 280 }}
          prefix={<SearchOutlined />}
        />
      </div>

      {highlights.length === 0 ? (
        <Empty description="还没有笔记" style={{ marginTop: 24 }} />
      ) : filteredHighlights.length === 0 ? (
        <Empty description="没有匹配的笔记" style={{ marginTop: 24 }} />
      ) : (
        <List
          itemLayout="vertical"
          dataSource={filteredHighlights}
          renderItem={(item: any) => (
            <Card className="highlight-card" style={{ marginBottom: 12 }}>
              <Paragraph style={{ color: "white", marginBottom: 8 }}>
                {highlightSearch ? (
                  <HighlightText text={item.content} query={highlightSearch} />
                ) : (
                  item.content
                )}
              </Paragraph>
              <Space wrap>
                {item.chapter && (
                  <Text style={{ color: "rgba(255,255,255,0.7)", fontSize: 12 }}>
                    {highlightSearch ? (
                      <HighlightText text={item.chapter} query={highlightSearch} color="rgba(255,255,255,0.7)" />
                    ) : (
                      item.chapter
                    )}
                  </Text>
                )}
                {item.emotion && <Tag color="purple">{item.emotion}</Tag>}
                {item.domain && <Tag color="cyan">{item.domain}</Tag>}
                {item.url && (
                  <a href={item.url} target="_blank" rel="noopener noreferrer">
                    <LinkOutlined /> 原文链接
                  </a>
                )}
              </Space>
            </Card>
          )}
        />
      )}
    </div>
  )
}

/** Highlight matching text within a string */
function HighlightText({ text, query, color }: { text: string; query: string; color?: string }) {
  if (!query.trim()) return <>{text}</>
  const idx = text.toLowerCase().indexOf(query.toLowerCase())
  if (idx === -1) return <>{text}</>
  const before = text.slice(0, idx)
  const match = text.slice(idx, idx + query.length)
  const after = text.slice(idx + query.length)
  return (
    <span style={{ color: color || "white" }}>
      {before}
      <mark style={{ background: "#faad14", color: "#000", padding: "0 2px", borderRadius: 2 }}>{match}</mark>
      {after}
    </span>
  )
}
