import { useQuery } from "@tanstack/react-query"
import { Card, Spin, Empty, Typography, Tag, Space, Button, message, Alert } from "antd"
import api from "../api"

const { Title, Text } = Typography

export default function GraphPage() {
  const { data: neo4jData, isLoading: neo4jLoading, error: neo4jError } = useQuery({
    queryKey: ["graph", "neo4j"],
    queryFn: () => api.get("/graph/"),
    retry: 1,
    timeout: 5000,
  })

  const { data: mysqlData, isLoading: mysqlLoading } = useQuery({
    queryKey: ["graph", "mysql"],
    queryFn: () => api.get("/mysql-graph/"),
    enabled: !neo4jLoading && (!!neo4jError || !neo4jData?.data?.nodes?.length),
  })

  const isLoading = neo4jLoading || mysqlLoading
  const data = neo4jData?.data?.nodes?.length > 0 ? neo4jData?.data : mysqlData?.data
  const graphSource = neo4jData?.data?.nodes?.length > 0 ? "neo4j" : "mysql"

  if (isLoading) {
    return <div style={{ textAlign: "center", padding: 50 }}><Spin size="large" /></div>
  }

  const nodes = data?.nodes || []
  const edges = data?.edges || []
  const books = nodes.filter((n: any) => n.type === "book")
  const concepts = nodes.filter((n: any) => n.type === "concept")
  const authors = nodes.filter((n: any) => n.type === "author")
  const highlights = nodes.filter((n: any) => n.type === "highlight")

  const handleSyncAll = async () => {
    try {
      const response = await api.post("/sync/all")
      message.success(`同步完成！已同步 ${response.data.synced_books} 本书`)
    } catch (err: any) {
      message.error("同步失败: " + (err.message || "请确保 Neo4j 服务已启动"))
    }
  }

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
        <Title level={2} style={{ margin: 0 }}>📊 知识图谱</Title>
        <Button onClick={handleSyncAll}>🔄 同步数据到图谱</Button>
      </div>
      
      {neo4jError && (
        <Alert type="warning" message="Neo4j 不可用" description="无法连接到 Neo4j 数据库，图谱数据从 MySQL 读取。" style={{ marginBottom: 16 }} showIcon />
      )}

      {nodes.length === 0 ? (
        <Empty style={{ marginTop: 50 }} description={<div><p>暂无图谱数据</p><Text type="secondary">点击「同步数据到图谱」将你的书籍和笔记同步到图谱数据库</Text></div>} />
      ) : (
        <div style={{ marginTop: 24 }}>
          <Card size="small" style={{ marginBottom: 16, background: "#f6f8fa" }}>
            <Space><Text type="secondary">数据来源: {graphSource === "neo4j" ? "🟢 Neo4j" : "🟡 MySQL"}</Text></Space>
          </Card>
          <Card size="small" style={{ marginBottom: 16 }}>
            <Space wrap>
              <Tag color="blue">📚 书籍 {books.length}</Tag>
              <Tag color="green">✍️ 作者 {authors.length}</Tag>
              <Tag color="purple">🧠 概念 {concepts.length}</Tag>
              <Tag color="orange">💬 笔记 {highlights.length}</Tag>
              <Tag color="red">🔗 关系 {edges.length}</Tag>
            </Space>
          </Card>
          {concepts.length > 0 && (
            <Card title="🧠 概念云" size="small" style={{ marginBottom: 16 }}>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                {concepts.map((c: any) => (
                  <Tag key={c.id} color="purple" style={{ fontSize: 14, padding: "4px 12px" }}>{c.label}</Tag>
                ))}
              </div>
            </Card>
          )}
          {books.length > 0 && (
            <Card title="📚 书籍" size="small" style={{ marginBottom: 16 }}>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                {books.map((b: any) => (
                  <Tag key={b.id} color="blue" style={{ fontSize: 14, padding: "4px 12px" }}>{b.label}</Tag>
                ))}
              </div>
            </Card>
          )}
          {highlights.length > 0 && (
            <Card title="💬 笔记预览" size="small" style={{ marginBottom: 16 }}>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
                {highlights.slice(0, 20).map((h: any) => (
                  <Tag key={h.id} color="orange" style={{ maxWidth: 300, whiteSpace: "normal" }}>{h.label}</Tag>
                ))}
              </div>
            </Card>
          )}
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
