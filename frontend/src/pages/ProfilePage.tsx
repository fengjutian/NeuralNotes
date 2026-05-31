import { useQuery } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"
import {
  Card, Row, Col, Statistic, Spin, Empty, Typography, Space,
  Progress, Tag, Alert, Button
} from "antd"
import {
  BookOutlined, ReadOutlined, TagOutlined, ClockCircleOutlined,
  WarningOutlined
} from "@ant-design/icons"
import { profileApi } from "../api"
import dayjs from "dayjs"
import relativeTime from "dayjs/plugin/relativeTime"

dayjs.extend(relativeTime)

const { Title, Text } = Typography

export default function ProfilePage() {
  const navigate = useNavigate()

  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ["profile"],
    queryFn: () => profileApi.get(),
  })

  const { data: blindSpotsData } = useQuery({
    queryKey: ["profile", "blind-spots"],
    queryFn: () => profileApi.getBlindSpots(),
  })

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
        <Title level={2}>阅读画像</Title>
        <Alert
          type="error"
          message="加载失败"
          description={(error as Error)?.message || "无法获取阅读画像数据"}
          showIcon
          action={
            <Button onClick={() => refetch()}>重试</Button>
          }
        />
      </div>
    )
  }

  const profile = data?.data
  if (!profile) {
    return <Empty description="暂无数据" />
  }

  const categoryList = Object.entries(profile.categories || {}).map(([name, count]) => ({
    name,
    count,
  }))

  const blindSpots = blindSpotsData?.data
  const preferences = profile._preferences
  const tendencies = profile._tendencies
  const summary = profile._summary

  // Trend bar chart via simple CSS bars (no heavy chart lib needed)
  const maxBarValue = Math.max(...categoryList.map((c: any) => (c as any).count), 1)

  return (
    <div>
      <Title level={2}>阅读画像</Title>

      {/* Key statistics */}
      <Row gutter={[16, 16]}>
        <Col xs={12} md={6}>
          <Card className="stat-card">
            <Statistic
              title="阅读书籍"
              value={profile.total_books}
              prefix={<BookOutlined />}
              valueStyle={{ color: "#667eea" }}
            />
          </Card>
        </Col>
        <Col xs={12} md={6}>
          <Card className="stat-card">
            <Statistic
              title="笔记总数"
              value={profile.total_highlights}
              prefix={<ReadOutlined />}
              valueStyle={{ color: "#764ba2" }}
            />
          </Card>
        </Col>
        <Col xs={12} md={6}>
          <Card className="stat-card">
            <Statistic
              title="阅读时长"
              value={profile.reading_time_total || "0"}
              prefix={<ClockCircleOutlined />}
            />
          </Card>
        </Col>
        <Col xs={12} md={6}>
          <Card className="stat-card">
            <Statistic
              title="阅读领域"
              value={categoryList.length}
              prefix={<TagOutlined />}
              valueStyle={{ color: "#52c41a" }}
            />
          </Card>
        </Col>
      </Row>

      {/* Summary info */}
      {summary && (
        <Card size="small" style={{ marginTop: 16, background: "#f6f8fa" }}>
          <Text type="secondary">
            平均每本书 {summary.avg_highlights_per_book.toFixed(1)} 条笔记
          </Text>
        </Card>
      )}

      <Row gutter={[16, 16]} style={{ marginTop: 24 }}>
        {/* Categories with trend-style bars */}
        <Col xs={24} md={12}>
          <Card title="📊 阅读分类分布">
            {categoryList.length === 0 ? (
              <Empty description="暂无分类数据" />
            ) : (
              <Space direction="vertical" style={{ width: "100%" }} size="middle">
                {categoryList.map((cat) => (
                  <div key={cat.name}>
                    <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 4 }}>
                      <Tag
                        color="blue"
                        style={{ cursor: "pointer" }}
                        onClick={() => navigate("/books?category=" + encodeURIComponent(cat.name))}
                      >
                        {cat.name}
                      </Tag>
                      <Text strong>{cat.count} 本</Text>
                    </div>
                    {/* Horizontal bar chart */}
                    <div style={{ background: "#f0f0f0", borderRadius: 4, height: 8, overflow: "hidden" }}>
                      <div
                        style={{
                          width: `${(cat.count / maxBarValue) * 100}%`,
                          height: "100%",
                          background: "linear-gradient(90deg, #667eea, #764ba2)",
                          borderRadius: 4,
                          transition: "width 0.5s ease",
                        }}
                      />
                    </div>
                  </div>
                ))}
              </Space>
            )}
          </Card>
        </Col>

        {/* Favorite categories & domains */}
        <Col xs={24} md={12}>
          <Card title="🧠 偏好与倾向">
            {preferences?.favorite_categories && preferences.favorite_categories.length > 0 && (
              <>
                <Text strong>最喜欢分类</Text>
                <div style={{ marginTop: 4, marginBottom: 12 }}>
                  <Space wrap>
                    {preferences.favorite_categories.map((fc: any) => (
                      <Tag key={fc.name} color="magenta">
                        {fc.name} ({fc.count})
                      </Tag>
                    ))}
                  </Space>
                </div>
              </>
            )}
            {preferences?.reading_emotions && preferences.reading_emotions.length > 0 && (
              <>
                <Text strong>阅读情绪</Text>
                <div style={{ marginTop: 4, marginBottom: 12 }}>
                  <Space wrap>
                    {preferences.reading_emotions.map((e: any) => (
                      <Tag key={e.type} color="purple">
                        {e.type} ({e.count})
                      </Tag>
                    ))}
                  </Space>
                </div>
              </>
            )}
            {preferences?.domains_of_interest && preferences.domains_of_interest.length > 0 && (
              <>
                <Text strong>兴趣领域</Text>
                <div style={{ marginTop: 4, marginBottom: 12 }}>
                  <Space wrap>
                    {preferences.domains_of_interest.map((d: any) => (
                      <Tag key={d.name} color="cyan">
                        {d.name} ({d.count})
                      </Tag>
                    ))}
                  </Space>
                </div>
              </>
            )}
            {tendencies && (
              <div style={{ marginTop: 8 }}>
                {tendencies.dominant_emotion && (
                  <Tag color="gold">主导情绪: {tendencies.dominant_emotion}</Tag>
                )}
                {tendencies.primary_domain && (
                  <Tag color="blue">主领域: {tendencies.primary_domain}</Tag>
                )}
              </div>
            )}
            {!preferences && !tendencies && (
              <Text type="secondary">暂无偏好数据，多读几本书并开启 AI 分析吧</Text>
            )}
          </Card>
        </Col>
      </Row>

      {/* Blind spots */}
      {blindSpots && (
        <Card
          title={
            <Space>
              <WarningOutlined style={{ color: "#faad14" }} />
              知识盲区检测
            </Space>
          }
          style={{ marginTop: 24 }}
          size="small"
        >
          <Row gutter={[16, 16]}>
            <Col xs={24} md={8}>
              <Statistic
                title="已覆盖领域"
                value={blindSpots.stats?.active_domains || 0}
                suffix={`/ ${blindSpots.stats?.potential_domains || 0}`}
              />
              <Progress
                percent={blindSpots.stats?.coverage_percentage || 0}
                size="small"
                style={{ marginTop: 8 }}
              />
            </Col>
            <Col xs={24} md={8}>
              <Text strong>缺失领域</Text>
              <div style={{ marginTop: 4 }}>
                {(blindSpots.missing_domains || []).length > 0 ? (
                  <Space wrap>
                    {blindSpots.missing_domains.map((d: string) => (
                      <Tag key={d} color="orange">{d}</Tag>
                    ))}
                  </Space>
                ) : (
                  <Text type="secondary">暂无</Text>
                )}
              </div>
            </Col>
            <Col xs={24} md={8}>
              <Text strong>阅读建议</Text>
              <div style={{ marginTop: 4 }}>
                {(blindSpots.suggestions || []).map((s: any, i: number) => (
                  <div key={i} style={{ marginBottom: 4 }}>
                    <Tag color={s.priority === "high" ? "red" : s.priority === "medium" ? "orange" : "green"}>
                      {s.priority}
                    </Tag>
                    {s.message}
                  </div>
                ))}
              </div>
            </Col>
          </Row>
        </Card>
      )}

      {/* Recent books */}
      <Row gutter={[16, 16]} style={{ marginTop: 24 }}>
        <Col xs={24}>
          <Card title="📖 最近阅读">
            {!profile.recent_books || profile.recent_books.length === 0 ? (
              <Empty description="暂无阅读记录" />
            ) : (
              <Space direction="vertical" style={{ width: "100%" }}>
                {profile.recent_books.slice(0, 5).map((book: any) => (
                  <Card
                    key={book.id}
                    hoverable
                    size="small"
                    onClick={() => navigate("/books/" + book.id)}
                  >
                    <Text strong>{book.title}</Text>
                    <br />
                    <Text type="secondary">{book.author}</Text>
                    <br />
                    <Text type="secondary" style={{ fontSize: 12 }}>
                      {dayjs(book.created_at).fromNow()}
                    </Text>
                  </Card>
                ))}
              </Space>
            )}
          </Card>
        </Col>
      </Row>
    </div>
  )
}
