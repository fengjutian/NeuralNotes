import { useParams, useNavigate } from "react-router-dom"
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import { Card, Spin, Typography, Button, Empty, List, Space, Tag, message, Modal } from "antd"
import { ArrowLeftOutlined, DeleteOutlined, LinkOutlined } from "@ant-design/icons"
import { bookApi } from "../api"
import dayjs from "dayjs"

const { Title, Text, Paragraph } = Typography

export default function BookDetailPage() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const queryClient = useQueryClient()

  const { data, isLoading } = useQuery({
    queryKey: ["book", id],
    queryFn: () => bookApi.get(id!),
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

  const handleDelete = () => {
    Modal.confirm({
      title: "确认删除",
      content: "确定要删除这本书吗？所有笔记也将被删除。",
      okText: "确认",
      cancelText: "取消",
      onOk: () => deleteMutation.mutate(),
    })
  }

  if (isLoading) {
    return (
      <div style={{ textAlign: "center", padding: 50 }}>
        <Spin size="large" />
      </div>
    )
  }

  const book = data?.data

  if (!book) {
    return <Empty description="书籍不存在" />
  }

  return (
    <div>
      <Button icon={<ArrowLeftOutlined />} onClick={() => navigate("/books")}>
        返回书架
      </Button>

      <Card style={{ marginTop: 16 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
          <div>
            <Title level={2}>{book.title}</Title>
            <Text type="secondary" style={{ fontSize: 16 }}>{book.author}</Text>
            <br /><br />
            <Space wrap>
              {book.category && <Tag color="blue">{book.category}</Tag>}
              {book.reading_time && <Tag>{book.reading_time}</Tag>}
              {book.progress !== undefined && (
                <Tag color="green">进度 {book.progress}%</Tag>
              )}
            </Space>
          </div>
          <Button
            danger
            icon={<DeleteOutlined />}
            onClick={handleDelete}
            loading={deleteMutation.isPending}
          >
            删除
          </Button>
        </div>
      </Card>

      <Title level={4} style={{ marginTop: 24 }}>
        我的笔记 ({book.highlight_count})
      </Title>

      {book.highlight_count === 0 ? (
        <Empty description="还没有笔记" />
      ) : (
        <List
          itemLayout="vertical"
          dataSource={[]}
          renderItem={(item: any) => (
            <Card className="highlight-card" style={{ marginBottom: 12 }}>
              <Paragraph style={{ color: "white", marginBottom: 8 }}>
                {item.content}
              </Paragraph>
              <Space>
                {item.chapter && (
                  <Text style={{ color: "rgba(255,255,255,0.7)" }}>
                    {item.chapter}
                  </Text>
                )}
                {item.url && (
                  <a href={item.url} target="_blank" rel="noopener noreferrer">
                    <LinkOutlined />
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
