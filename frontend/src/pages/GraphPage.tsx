import { useEffect, useRef, useState } from "react"
import { useQuery, useQueryClient } from "@tanstack/react-query"
import {
  Card, Spin, Empty, Typography, Tag, Space, Button, message, Alert,
  Modal, Select, Divider, Tooltip, Segmented
} from "antd"
import {
  RobotOutlined, CameraOutlined, ReloadOutlined
} from "@ant-design/icons"
import { Network, DataSet } from "vis-network/standalone"
import api from "../api"
import { useNavigate } from "react-router-dom"

const { Title, Text } = Typography

type LayoutType = "force" | "hierarchical"

export default function GraphPage() {
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const containerRef = useRef<HTMLDivElement>(null)
  const networkRef = useRef<Network | null>(null)
  const [analyzeModalVisible, setAnalyzeModalVisible] = useState(false)
  const [selectedBookId, setSelectedBookId] = useState<string | null>(null)
  const [analyzing, setAnalyzing] = useState(false)
  const [layout, setLayout] = useState<LayoutType>("force")

  const { data: neo4jData, isLoading: neo4jLoading, error: neo4jError } = useQuery({
    queryKey: ["graph", "neo4j"],
    queryFn: () => api.get("/graph/"),
    retry: 1,
  })

  const { data: mysqlData, isLoading: mysqlLoading } = useQuery({
    queryKey: ["graph", "mysql"],
    queryFn: () => api.get("/mysql-graph/"),
    enabled: !neo4jLoading && (!!neo4jError || !neo4jData?.data?.nodes?.length),
  })

  const { data: booksData } = useQuery({
    queryKey: ["books"],
    queryFn: () => api.get("/books/"),
  })

  const isLoading = neo4jLoading || mysqlLoading
  const data = neo4jData?.data?.nodes?.length > 0 ? neo4jData?.data : mysqlData?.data
  const graphSource = neo4jData?.data?.nodes?.length > 0 ? "neo4j" : "mysql"

  const nodes = data?.nodes || []
  const edges = data?.edges || []

  const nodeTypeCounts = {
    book: nodes.filter((n: any) => n.type === "book").length,
    concept: nodes.filter((n: any) => n.type === "concept").length,
    author: nodes.filter((n: any) => n.type === "author").length,
    highlight: nodes.filter((n: any) => n.type === "highlight").length,
  }

  useEffect(() => {
    if (!containerRef.current || nodes.length === 0) return

    // Destroy previous network instance
    if (networkRef.current) {
      networkRef.current.destroy()
      networkRef.current = null
    }

    // Map node types to colors and icons
    const typeConfig: Record<string, { color: string; shape: string; size: number }> = {
      book: { color: "#1677ff", shape: "dot", size: 25 },
      concept: { color: "#722ed1", shape: "diamond", size: 20 },
      author: { color: "#52c41a", shape: "triangle", size: 18 },
      highlight: { color: "#fa8c16", shape: "square", size: 12 },
    }

    const visNodes = new DataSet<any>(
      nodes.map((n: any) => ({
        id: n.id,
        label: n.label?.length > 20 ? n.label.slice(0, 20) + "..." : n.label,
        title: n.label,
        color: typeConfig[n.type]?.color || "#999",
        shape: typeConfig[n.type]?.shape || "dot",
        size: typeConfig[n.type]?.size || 15,
        font: { size: 11, color: "#333" },
        _type: n.type,
        _origId: n.id,
      }))
    )

    const visEdges = new DataSet<any>(
      edges.map((e: any, idx: number) => ({
        id: idx,
        from: e.source,
        to: e.target,
        label: e.type,
        arrows: "to",
        color: { color: "#bbb", highlight: "#667eea" },
        font: { size: 9, color: "#999", strokeWidth: 0 },
      }))
    )

    const options = {
      physics: layout === "force" ? {
        solver: "forceAtlas2Based" as const,
        forceAtlas2Based: {
          gravitationalConstant: -40,
          centralGravity: 0.005,
          springLength: 120,
          springConstant: 0.08,
        },
        stabilization: { iterations: 150 },
      } : false,
      layout: layout === "hierarchical" ? {
        hierarchical: {
          direction: "LR",
          sortMethod: "directed",
          nodeSpacing: 120,
          levelSeparation: 200,
        },
      } : undefined,
      interaction: {
        hover: true,
        tooltipDelay: 200,
        zoomView: true,
        dragView: true,
        navigationButtons: true,
      },
      edges: {
        smooth: { type: "continuous" },
      },
    }

    const network = new Network(containerRef.current, { nodes: visNodes as any, edges: visEdges as any }, options as any)
    networkRef.current = network

    // Node click: navigate to book detail
    network.on("click", (params: any) => {
      if (params.nodes.length === 1) {
        const nodeId = params.nodes[0]
        const node = visNodes.get(nodeId) as any
        if (node?._type === "book" && node?._origId) {
          navigate("/books/" + node._origId)
        }
      }
    })

    return () => {
      if (networkRef.current) {
        networkRef.current.destroy()
        networkRef.current = null
      }
    }
  }, [nodes, edges, layout, navigate])

  const handleSyncAll = async () => {
    try {
      const response = await api.post("/sync/all")
      message.success(`同步完成！已同步 ${response.data.synced_books} 本书`)
      queryClient.invalidateQueries({ queryKey: ["graph"] })
    } catch (err: any) {
      message.error("同步失败: " + (err.message || "请确保 Neo4j 服务已启动"))
    }
  }

  const handleAnalyze = async () => {
    if (!selectedBookId) {
      message.warning("请选择要分析的书籍")
      return
    }
    setAnalyzing(true)
    try {
      message.loading("AI 正在分析中，请稍候...")
      const response = await api.post(`/analyze/?book_id=${selectedBookId}`)
      const analyzedCount = response.data?.total || 0
      message.destroy()
      message.success(`AI 分析完成！已分析 ${analyzedCount} 条笔记`)
      setAnalyzeModalVisible(false)
      queryClient.invalidateQueries({ queryKey: ["graph"] })
    } catch (err: any) {
      message.destroy()
      message.error("分析失败: " + (err.message || "请稍后重试"))
    } finally {
      setAnalyzing(false)
    }
  }

  const handleExportImage = () => {
    if (!containerRef.current) return
    const canvas = containerRef.current.querySelector("canvas")
    if (canvas) {
      const link = document.createElement("a")
      link.download = "knowledge-graph.png"
      link.href = canvas.toDataURL("image/png")
      link.click()
      message.success("图谱已导出！")
    } else {
      message.warning("无法导出，请等待图谱加载完成")
    }
  }

  if (isLoading) {
    return <div style={{ textAlign: "center", padding: 50 }}><Spin size="large" /></div>
  }

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16, flexWrap: "wrap", gap: 8 }}>
        <Title level={2} style={{ margin: 0 }}>📊 知识图谱</Title>
        <Space wrap>
          <Segmented
            value={layout}
            onChange={(v) => setLayout(v as LayoutType)}
            options={[
              { label: "力导向", value: "force" },
              { label: "层级", value: "hierarchical" },
            ]}
          />
          <Tooltip title="导出为 PNG 图片">
            <Button icon={<CameraOutlined />} onClick={handleExportImage} disabled={nodes.length === 0}>
              导出
            </Button>
          </Tooltip>
          <Button icon={<RobotOutlined />} onClick={() => setAnalyzeModalVisible(true)}>
            🤖 AI 分析
          </Button>
          <Button icon={<ReloadOutlined />} onClick={handleSyncAll}>
            同步到图谱
          </Button>
        </Space>
      </div>

      <Modal
        title="🤖 AI 概念分析"
        open={analyzeModalVisible}
        onOk={handleAnalyze}
        onCancel={() => setAnalyzeModalVisible(false)}
        confirmLoading={analyzing}
        okText="开始分析"
        cancelText="取消"
      >
        <p>选择一本书，系统将使用 AI 分析该书所有未分析的笔记，提取概念和知识点。</p>
        <Divider />
        <Select
          style={{ width: "100%" }}
          placeholder="请选择书籍"
          value={selectedBookId}
          onChange={setSelectedBookId}
          showSearch
          optionFilterProp="children"
        >
          {(booksData?.data?.items || []).map((book: any) => (
            <Select.Option key={book.id} value={book.id}>
              <Space>
                <span>{book.title}</span>
                <Tag>{book.highlight_count} 条笔记</Tag>
              </Space>
            </Select.Option>
          ))}
        </Select>
      </Modal>

      {neo4jError && (
        <Alert type="warning" message="Neo4j 不可用" description="无法连接到 Neo4j 数据库，图谱数据从 MySQL 读取。" style={{ marginBottom: 16 }} showIcon />
      )}

      {nodes.length === 0 ? (
        <Empty style={{ marginTop: 50 }} description={<div><p>暂无图谱数据</p><Text type="secondary">点击「同步数据到图谱」将你的书籍和笔记同步到图谱数据库</Text></div>} />
      ) : (
        <>
          <Card size="small" style={{ marginBottom: 16, background: "#f6f8fa" }}>
            <Space wrap>
              <Text type="secondary">数据来源: {graphSource === "neo4j" ? "🟢 Neo4j" : "🟡 MySQL"}</Text>
              <Tag color="blue">📚 书籍 {nodeTypeCounts.book}</Tag>
              <Tag color="green">✍️ 作者 {nodeTypeCounts.author}</Tag>
              <Tag color="purple">🧠 概念 {nodeTypeCounts.concept}</Tag>
              <Tag color="orange">💬 笔记 {nodeTypeCounts.highlight}</Tag>
              <Tag color="red">🔗 关系 {edges.length}</Tag>
            </Space>
          </Card>

          <Card size="small">
            <div
              ref={containerRef}
              style={{
                width: "100%",
                height: "65vh",
                minHeight: 450,
                border: "1px solid #f0f0f0",
                borderRadius: 8,
              }}
            />
            <div style={{ marginTop: 8, display: "flex", gap: 16, flexWrap: "wrap" }}>
              <Text type="secondary" style={{ fontSize: 12 }}>💡 提示: 滚轮缩放 | 拖拽移动 | 点击书籍节点跳转详情</Text>
              <Text type="secondary" style={{ fontSize: 12 }}>🔷 概念 🔺 作者 📘 书籍 ▪️ 笔记</Text>
            </div>
          </Card>
        </>
      )}
    </div>
  )
}
