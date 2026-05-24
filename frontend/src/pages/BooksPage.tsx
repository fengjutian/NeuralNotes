import { useQuery } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"
import { Card, Row, Col, Empty, Spin, Typography, Space, Tag } from "antd"
import { BookOutlined, ReadOutlined } from "@ant-design/icons"
import { bookApi, type Book } from "../api"
import dayjs from "dayjs"

const { Title, Text } = Typography

export default function BooksPage() {
  const navigate = useNavigate()
  
  const { data, isLoading } = useQuery({
    queryKey: ["books"],
    queryFn: () => bookApi.list({ page: 1, page_size: 100 }),
  })

  const books = data?.data?.items || []

  const handleBookClick = (book: Book) => {
    navigate("/books/" + book.id)
  }

  if (isLoading) {
    return (
      <div style={{ textAlign: "center", padding: 50 }}>
        <Spin size="large" />
      </div>
    )
  }

  return (
    <div>
      <Title level={2}>我的书架</Title>
      
      {books.length === 0 ? (
        <Empty 
          description="还没有书籍，快去导入一本吧！" 
          image={Empty.PRESENTED_IMAGE_SIMPLE}
        />
      ) : (
        <Row gutter={[16, 16]}>
          {books.map((book) => (
            <Col key={book.id} xs={24} sm={12} md={8} lg={6}>
              <Card
                className="book-card"
                hoverable
                onClick={() => handleBookClick(book)}
                cover={
                  <div style={{
                    height: 120,
                    background: "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}>
                    <BookOutlined style={{ fontSize: 48, color: "white" }} />
                  </div>
                }
              >
                <Card.Meta
                  title={book.title}
                  description={
                    <Space direction="vertical" size="small" style={{ width: "100%" }}>
                      <Text type="secondary">{book.author}</Text>
                      <Space>
                        <Tag icon={<ReadOutlined />}>{book.highlight_count} 条笔记</Tag>
                        {book.category && <Tag color="blue">{book.category}</Tag>}
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
