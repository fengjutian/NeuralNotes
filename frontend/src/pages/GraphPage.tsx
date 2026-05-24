import { useQuery } from "@tanstack/react-query"
import { Card, Spin, Empty, Typography, Tag, Space } from "antd"
import api from "../api"

const { Title, Text } = Typography

export default function GraphPage() {
  const { data, isLoading } = useQuery({
    queryKey: ["graph"],
    queryFn: () => api.get("/graph/"),
  })

  if (isLoading) {
    return <div style={{ textAlign: "center", padding: 50 }}><Spin size="large" /></div>
  }

  const nodes = data?.data?.nodes || []
  const edges = data?.data?.edges || []
  const books = nodes.filter((n: any) => n.type === "book")
  const concepts = nodes.filter((n: any) => n.type === "concept")
  const authors = nodes.filter((n: any) => n.type === "author")
  const highlights = nodes.filter((n: any) => n.type === "highlight")

  return (
    <div>
      <Title level={2}>📊 知识图谱</Title>

      {nodes.length === 0 ? (
        <Empty style={{ marginTop: 50 }}
          description={
            <div>
              <p>暂无图谱数据</p>
              <Text type="secondary">
                请先在 Neo4j 中创建数据，或在 Swagger 文档中调用 POST /api/v1/analyze 进行 AI 分析
              </Text>
            </div>
          }
        />
      ) : (
        <div style={{ marginTop: 24 }}>
          {/* 统计 */}
          <Card size="small" style={{ marginBottom: 16 }}>
            <Space wrap>
              <Tag color="blue">📚 书籍 {books.length}</Tag>
              <Tag color="green">✍️ 作者 {authors.length}</Tag>
              <Tag color="purple">🧠 概念 {concepts.length}</Tag>
              <Tag color="orange">💬 笔记 {highlights.length}</Tag>
              <Tag color="red">🔗 关系 {edges.length}</Tag>
            </Space>
          </Card>

          {/* 概念云 */}
          {concepts.length > 0 && (
            <Card title="🧠 概念云" size="small" style={{ marginBottom: 16 }}>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                {concepts.map((c: any) => (
                  <Tag
                    key={c.id}
                    color="purple"
                    style={{ fontSize: 14, padding: "4px 12px", cursor: "pointer" }}
                  >
                    {c.label}
                    {c.properties?.frequency && (
                      <span style={{ marginLeft: 4, opacity: 0.7 }}>
                        ×{c.properties.frequency}
                      </span>
                    )}
                  </Tag>
                ))}
              </div>
            </Card>
          )}

          {/* 书籍列表 */}
          {books.length > 0 && (
            <Card title="📚 书籍" size="small" style={{ marginBottom: 16 }}>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                {books.map((b: any) => (
                  <Tag key={b.id} color="blue" style={{ fontSize: 14, padding: "4px 12px" }}>
                    {b.label}
                  </Tag>
                ))}
              </div>
            </Card>
          )}

          {/* 关系列表 */}
          {edges.length > 0 && (
            <Card title="🔗 关系" size="small">
              <Space direction="vertical" size="small" style={{ width: "100%" }}>
                {edges.slice(0, 50).map((edge: any, idx: number) => {
                  const sourceNode = nodes.find((n: any) => n.id === edge.source)
                  const targetNode = nodes.find((n: any) => n.id === edge.target)
                  return (
                    <div key={idx} style={{ display: "flex", alignItems: "center", gap: 8 }}>
                      <Tag>{sourceNode?.label || edge.source}</Tag>
                      <span style={{ color: "#999" }}>→ {edge.type} →</span>
                      <Tag>{targetNode?.label || edge.target}</Tag>
                    </div>
                  )
                })}
              </Space>
            </Card>
          )}
        </div>
      )}
    </div>
  )
}