import { useState } from "react"
import { useQuery } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"
import { Card, Row, Col, Empty, Spin, Typography, Space, Tag, Select, Button, Input, Alert } from "antd"
import { BookOutlined, ReadOutlined, ReloadOutlined, SortAscendingOutlined } from "@ant-design/icons"
import { bookApi, type Book } from "../api"
import dayjs from "dayjs"

const { Title, Text } = Typography

export default function BooksPage() {
  const navigate = useNavigate()
  const [category, setCategory] = useState<string | undefined>(undefined)
  const [search, setSearch] = useState("")
  const [sortBy, setSortBy] = useState<string>("created_at")

  const { data, isLoading, error, refetch, isFetching } = useQuery({
    queryKey: ["books", { category, page: 1, page_size: 100 }],
    queryFn: () => bookApi.list({ page: 1, page_size: 100, category }),
  })

  const books = data?.data?.items || []

  const handleBookClick = (book: Book) => {
    navigate("/books/" + book.id)
  }

  const allCategories = Array.from(
    new Set(
      books
        .map((b) => b.category)
        .filter((c): c is string => !!c)
    )
  )

  let filteredBooks = books
  if (search.trim()) {
    const lower = search.toLowerCase()
    filteredBooks = books.filter(
      (b) =>
        b.title.toLowerCase().includes(lower) ||
        b.author.toLowerCase().includes(lower)
    )
  }

  if (sortBy === "title") {
    filteredBooks = [...filteredBooks].sort((a, b) =>
      a.title.localeCompare(b.title)
    )
  } else if (sortBy === "highlights") {
    filteredBooks = [...filteredBooks].sort(
      (a, b) => (b.highlight_count || 0) - (a.highlight_count || 0)
    )
  } else if (sortBy === "author") {
    filteredBooks = [...filteredBooks].sort((a, b) =>
      a.author.localeCompare(b.author)
    )
  } else {
    filteredBooks = [...filteredBooks].sort(
      (a, b) =>
        new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
    )
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
        <Title level={2}>我的书架</Title>
        <Alert
          type="error"
          message="加载失败"
          description={
            (error as Error)?.message ||
            "无法加载书籍列表，请检查网络或数据库连接"
          }
          showIcon
          action={
            <Button onClick={() => refetch()} icon={<ReloadOutlined />}>
              重试
            </Button>
          }
        />
      </div>
    )
  }

  return (
    <div>
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          marginBottom: 16,
          flexWrap: "wrap",
          gap: 8,
        }}
      >
        <Title level={2} style={{ margin: 0 }}>
          我的书架
        </Title>
        <Space wrap>
          <Button
            icon={<ReloadOutlined />}
            onClick={() => refetch()}
            loading={isFetching}
          >
            刷新
          </Button>
        </Space>
      </div>

      <Space wrap style={{ marginBottom: 16 }}>
        <Input.Search
          placeholder="搜索书名或作者..."
          allowClear
          onSearch={(v) => setSearch(v)}
          onChange={(e) => {
            if (!e.target.value) setSearch("")
          }}
          style={{ width: 240 }}
        />
        <Select
          placeholder="分类筛选"
          allowClear
          style={{ width: 160 }}
          value={category}
          onChange={(v) => setCategory(v)}
          options={allCategories.map((c) => ({ label: c, value: c }))}
        />
        <Select
          style={{ width: 140 }}
          value={sortBy}
          onChange={setSortBy}
          suffixIcon={<SortAscendingOutlined />}
          options={[
            { label: "按时间排序", value: "created_at" },
            { label: "按书名排序", value: "title" },
            { label: "按作者排序", value: "author" },
            { label: "笔记最多", value: "highlights" },
          ]}
        />
        <Text type="secondary">
          共 {filteredBooks.length} 本
          {search || category ? ` (筛选自 ${books.length} 本)` : ""}
        </Text>
      </Space>

      {filteredBooks.length === 0 ? (
        <Empty
          description={
            search || category
              ? "没有匹配的书籍"
              : "还没有书籍，快去导入一本吧！"
          }
          image={Empty.PRESENTED_IMAGE_SIMPLE}
        />
      ) : (
        <Row gutter={[16, 16]}>
          {filteredBooks.map((book) => (
            <Col key={book.id} xs={24} sm={12} md={8} lg={6}>
              <Card
                className="book-card"
                hoverable
                onClick={() => handleBookClick(book)}
                cover={
                  <div
                    style={{
                      height: 120,
                      background:
                        "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                    }}
                  >
                    <BookOutlined style={{ fontSize: 48, color: "white" }} />
                  </div>
                }
              >
                <Card.Meta
                  title={book.title}
                  description={
                    <Space
                      direction="vertical"
                      size="small"
                      style={{ width: "100%" }}
                    >
                      <Text type="secondary">{book.author}</Text>
                      <Space>
                        <Tag icon={<ReadOutlined />}>
                          {book.highlight_count} 条笔记
                        </Tag>
                        {book.category && (
                          <Tag color="blue">{book.category}</Tag>
                        )}
                      </Space>
                      <Text type="secondary" style={{ fontSize: 12 }}>
                        {dayjs(book.created_at).format("YYYY-MM-DD")}
                      </Text>
                    </Space>
                  }
                />
              </Card>
            </Col>
          ))}
        </Row>
      )}
    </div>
  )
}
