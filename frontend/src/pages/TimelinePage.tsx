import { useQuery } from "@tanstack/react-query"
import { Card, Spin, Empty, Typography, Timeline, Space, Tag, Alert } from "antd"
import {
  ClockCircleOutlined,
  RocketOutlined,
  BulbOutlined,
  WarningOutlined,
} from "@ant-design/icons"
import { timelineApi, type TimelineYear, type TimelinePivotPoint } from "../api"

const { Title, Text, Paragraph } = Typography

export default function TimelinePage() {
  const {
    data,
    isLoading,
    error,
  } = useQuery({
    queryKey: ["timeline"],
    queryFn: () => timelineApi.get(),
    retry: 2,
  })

  const { data: pivotData } = useQuery({
    queryKey: ["timeline", "pivots"],
    queryFn: () => timelineApi.getPivotPoints(),
    retry: 2,
  })

  if (isLoading) {
    return <div style={{ textAlign: "center", padding: 50 }}><Spin size="large" /></div>
  }

  if (error) {
    return (
      <div>
        <Title level={2}>⏱️ 阅读时间线</Title>
        <Alert type="error" message="加载失败" description={(error as Error)?.message || "无法获取时间线数据，请检查数据库连接"} showIcon />
      </div>
    )
  }

  const timeline = data?.data
  const pivotPoints = pivotData?.data?.pivot_points || []

  if (!timeline || timeline.years.length === 0) {
    return (
      <div>
        <Title level={2}>⏱️ 阅读时间线</Title>
        <Empty description="暂无时间线数据，先导入一些书籍吧！" />
      </div>
    )
  }

  const getPivotIcon = (type: string) => {
    switch (type) {
      case "growth_spike":
      case "growth":
        return <RocketOutlined />
      case "new_domain":
        return <BulbOutlined />
      case "reading_drop":
        return <WarningOutlined />
      default:
        return <ClockCircleOutlined />
    }
  }

  const getPivotColor = (type: string) => {
    switch (type) {
      case "growth_spike":
      case "growth":
        return "#52c41a"
      case "new_domain":
        return "#1890ff"
      case "reading_drop":
        return "#faad14"
      default:
        return "#667eea"
    }
  }

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16, flexWrap: "wrap", gap: 8 }}>
        <Title level={2} style={{ margin: 0 }}>⏱️ 阅读时间线</Title>
        <Space wrap>
          <Tag color="blue">📚 {timeline.year_count} 年阅读史</Tag>
          <Tag color="purple">💬 {timeline.total_highlights} 条笔记</Tag>
          <Tag color="orange">🔑 {pivotPoints.length} 个关键转折</Tag>
        </Space>
      </div>

      {pivotPoints.length > 0 && (
        <Card size="small" style={{ marginBottom: 24, background: "#f6f8fa" }}>
          <Text strong>🔑 认知转折点</Text>
          <Paragraph type="secondary" style={{ marginTop: 8, marginBottom: 0 }}>
            你的阅读兴趣在以下年份发生了显著变化，这些转折点反映了知识结构的演进。
          </Paragraph>
        </Card>
      )}

      <Timeline
        items={timeline.years.map((year: TimelineYear) => {
          const yearPivots = pivotPoints.filter((p: TimelinePivotPoint) => p.year === year.year)
          const hasPivot = yearPivots.length > 0

          return {
            key: year.year,
            dot: hasPivot ? (
              <div style={{
                width: 24, height: 24, borderRadius: "50%",
                background: getPivotColor(yearPivots[0].type),
                display: "flex", alignItems: "center", justifyContent: "center",
              }}>
                {getPivotIcon(yearPivots[0].type)}
              </div>
            ) : (
              <ClockCircleOutlined style={{ fontSize: 16 }} />
            ),
            color: hasPivot ? getPivotColor(yearPivots[0].type) : "#1890ff",
            children: (
              <Card size="small" hoverable style={{ marginBottom: 12 }}>
                <Space direction="vertical" size="small" style={{ width: "100%" }}>
                  <Space>
                    <Text strong style={{ fontSize: 18 }}>{year.year}</Text>
                    <Tag color="blue">{year.highlight_count} 条笔记</Tag>
                    <Tag color="purple">主题情绪：{year.theme}</Tag>
                  </Space>

                  {year.dominant_domains.length > 0 && (
                    <Space wrap>
                      <Text type="secondary">主要领域：</Text>
                      {year.dominant_domains.map((domain: string) => (
                        <Tag key={domain} color="green">{domain}</Tag>
                      ))}
                    </Space>
                  )}

                  {year.top_books.length > 0 && (
                    <div>
                      <Text type="secondary">年度重点书籍：</Text>
                      <Space wrap style={{ marginTop: 4 }}>
                        {year.top_books.map((book) => (
                          <Tag key={book.title} color="orange">
                            📖 {book.title}
                            <Text type="secondary" style={{ fontSize: 11, marginLeft: 4 }}>
                              ({book.highlights} 条笔记)
                            </Text>
                          </Tag>
                        ))}
                      </Space>
                    </div>
                  )}

                  {yearPivots.map((pivot: TimelinePivotPoint, idx: number) => (
                    <Alert key={idx} type={pivot.type === "reading_drop" ? "warning" : "info"}
                      message={<Space>{getPivotIcon(pivot.type)}<Text>{pivot.message}</Text></Space>}
                      style={{ marginTop: 4 }} showIcon={false} />
                  ))}
                </Space>
              </Card>
            ),
          }
        })}
      />

      {timeline.years.length === 1 && (
        <Alert type="info" message="刚开始记录"
          description="目前只有一年的数据，随着更多书籍的导入，时间线会越来越丰富。"
          showIcon style={{ marginTop: 16 }} />
      )}
    </div>
  )
}
