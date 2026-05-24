import { useQuery } from "@tanstack/react-query"
import { Card, Spin, Empty, Typography, Tag, List, Space } from "antd"
import { api } from "../api"
import { useSearchParams } from "react-router-dom"

const { Title, Text } = Typography

interface GraphNode {
  id: string
  type: "book" | "author" | "concept" | "highlight"
  label: string
  properties?: Record<string, any>
}

interface GraphEdge {
  source: string
  target: string
  type: string
}


export default function GraphPage() {
  const [searchParams] = useSearchParams()
  const bookId = searchParams.get("book_id")

  const { data, isLoading } = useQuery({
    queryKey: ["graph", bookId],
    queryFn: () => api.get<{ nodes: GraphNode[]; edges: GraphEdge[] }>("/graph" + (bookId ? `?book_id=${bookId}` : "")),
  })

  if (isLoading) {
    return (
      <div style={{ textAlign: "center", padding: 50 }}>
        <Spin size="large" />
      </div>
    )
  }

  const graph = data?.data
  const nodes = graph?.nodes || []
  const edges = graph?.edges || []

  // Group nodes by type
  const books = nodes.filter(n => n.type === "book")
  const authors = nodes.filter(n => n.type === "author")
  const concepts = nodes.filter(n => n.type === "concept")
  const highlights = nodes.filter(n => n.type === "highlight")


  return (
    <div>
      <Title level={2}>📊 知识图谱</Title>

      <Text type="secondary">展示书籍、作者和概念之间的关系</Text>


      {nodes.length === 0 ? (
        <Empty style={{ marginTop: 50 }}
          description={
            <div>
              <p>暂无图谱数据</p>
              <Text type="secondary">
                请先导入书籍，然后使用 AI 分析功能提取概念
              </Text>
            </div>
          }
        />
      ) : (
        <div style={{ marginTop: 24 }}>
          {/* Stats */}
          <Card size="small" style={{ marginBottom: 16 }}>
            <Space>
              <Tag color="blue">书籍: {books.length}</Tag>
              <Tag color="green">作者: {authors.length}</Tag>
              <Tag color="purple">概念: {concepts.length}</Tag>
              <Tag color="orange">笔记: {highlights.length}</Tag>
              <Tag color="red">关系: {edges.length}</Tag>
            </Space>
          </Card>

          {/* Books */}
          {books.length > 0 && (
            <Card title="📚 书籍" size="small" style={{ marginBottom: 16 }}>
              <List
                size="small"
                dataSource={books.slice(0, 10)}
                renderItem={(item) => (
                  <List.Item style={{ padding: "8px 0" }}>
                    <Text strong>{item.label}</Text>
                    {item.properties?.category && (
                      <Tag style={{ marginLeft: 8 }}>{item.properties.category}</Tag>
                    )}
                  </List.Item>
                )}
              />
            </Card>
          )}

          {/* Authors */}
          {authors.length > 0 && (
            <Card title="✍️ 作者" size="small" style={{ marginBottom: 16 }}>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                {authors.map(author => (
                  <Tag key={author.id} color="green" style={{ fontSize: 14, padding: "4px 12px" }}>
                    {author.label}
                  </Tag>
                ))}
              </div>
            </Card>
          )}

          {/* Concepts */}
          {concepts.length > 0 && (
            <Card title="🧠 概念" size="small" style={{ marginBottom: 16 }}>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                {concepts.map(concept => (
                  <Tag key={concept.id} color="purple" style={{ fontSize: 14, padding: "4px 12px" }}>
                    {concept.label}
                  </Tag>
                ))}
              </div>
            </Card>
          )}

          {/* Highlights */}
          {highlights.length > 0 && (
            <Card title="💬 笔记" size="small">
              <List
                size="small"
                dataSource={highlights.slice(0, 20)}
                renderItem={(item) => (
                  <List.Item style={{ padding: "8px 0" }}>
                    <Text type="secondary" style={{ fontSize: 12 }}>
                      {item.label?.substring(0, 100)}...
                    </Text>
                  </List.Item>
                )}
              />
            </Card>
          )}
        </div>
      )}
    </div>
  )
}