import { useState } from "react"
import { useQuery } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"
import { Card, Input, Spin, Empty, Typography, Space, Tag } from "antd"
import { SearchOutlined, BookOutlined } from "@ant-design/icons"
import { searchApi } from "../api"

const { Title, Text, Paragraph } = Typography

export default function SearchPage() {
  const navigate = useNavigate()
  const [query, setQuery] = useState("")


  const { data, isLoading } = useQuery({
    queryKey: ["search", query],
    queryFn: () => searchApi.search({ q: query, limit: 20 }),
    enabled: query.length > 0,
  })

  const handleSearch = (value: string) => {
    setQuery(value)
  }

  return (
    <div>
      <Title level={2}>语义搜索</Title>
      
      <Input.Search
        placeholder="输入关键词搜索笔记内容..."
        allowClear
        enterButton={<SearchOutlined />}
        size="large"
        onSearch={handleSearch}
        style={{ maxWidth: 600, marginBottom: 24 }}
      />

      {isLoading && (
        <div style={{ textAlign: "center", padding: 50 }}>
          <Spin size="large" />
        </div>
      )}

      {!query && !isLoading && (
        <Empty description="输入关键词开始搜索" />
      )}

      {query && !isLoading && (!data?.data || data.data.length === 0) && (
        <Empty description="未找到相关笔记" />
      )}


      {data?.data && data.data.length > 0 && (
        <Space direction="vertical" style={{ width: "100%" }}>
          <Text type="secondary">找到 {data.data.length} 条相关笔记</Text>
          {data.data.map((item: any, index: number) => (
            <Card
              key={item.id || index}
              hoverable
              onClick={() => navigate("/books/" + item.book_id)}
            >
              <Paragraph
                ellipsis={{ rows: 3, expandable: true, symbol: "展开" }}
                style={{ marginBottom: 8 }}
              >
                {item.content}
              </Paragraph>
              <Space wrap>
                {item.book_title && (
                  <Tag icon={<BookOutlined />} color="blue">
                    {item.book_title}
                  </Tag>
                )}
                {item.chapter && <Tag>{item.chapter}</Tag>}
                <Tag color="green">相关度 {Math.round((item.score || 0) * 100)}%</Tag>
              </Space>
            </Card>
          ))}
        </Space>
      )}
    </div>
  )
}
