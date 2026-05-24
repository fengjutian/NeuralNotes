import { useQuery } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"
import { Card, Row, Col, Statistic, Spin, Empty, Typography, Space, Progress } from "antd"
import { BookOutlined, ReadOutlined, TagOutlined, ClockCircleOutlined } from "@ant-design/icons"
import { profileApi } from "../api"
import dayjs from "dayjs"

const { Title, Text } = Typography

export default function ProfilePage() {
  const navigate = useNavigate()
  const { data, isLoading } = useQuery({
    queryKey: ["profile"],
    queryFn: () => profileApi.get(),
  })
  if (isLoading) {
    return (
      <div style={{ textAlign: "center", padding: 50 }}>
        <Spin size="large" />
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
  const maxCategory = categoryList.reduce((max, item) => 
    item.count > (max?.count || 0) ? item : max, { name: "", count: 0 })
  return (
    <div>
      <Title level={2}>阅读画像</Title>
      <Row gutter={[16, 16]}>
        <Col xs={12} md={6}>
          <Card className="stat-card">
            <Statistic title="阅读书籍" value={profile.total_books} prefix={<BookOutlined />} valueStyle={{ color: "#667eea" }} />
          </Card>
        </Col>
        <Col xs={12} md={6}>
          <Card className="stat-card">
            <Statistic title="笔记总数" value={profile.total_highlights} prefix={<ReadOutlined />} valueStyle={{ color: "#764ba2" }} />
          </Card>
        </Col>
        <Col xs={12} md={6}>
          <Card className="stat-card">
            <Statistic title="阅读时长" value={profile.reading_time_total || "0"} prefix={<ClockCircleOutlined />} />
          </Card>
        </Col>
        <Col xs={12} md={6}>
          <Card className="stat-card">
            <Statistic title="阅读领域" value={categoryList.length} prefix={<TagOutlined />} valueStyle={{ color: "#52c41a" }} />
          </Card>
        </Col>
      </Row>
      <Row gutter={[16, 16]} style={{ marginTop: 24 }}>
        <Col xs={24} md={12}>
          <Card title="阅读分类">
            {categoryList.length === 0 ? (
              <Empty description="暂无分类数据" />
            ) : (
              <Space direction="vertical" style={{ width: "100%" }}>
                {categoryList.map((cat) => (
                  <div key={cat.name}>
                    <Space style={{ width: "100%", justifyContent: "space-between" }}>
                      <Text>{cat.name}</Text>
                      <Text type="secondary">{cat.count} 本</Text>
                    </Space>
                    <Progress percent={maxCategory.count > 0 ? (cat.count / maxCategory.count) * 100 : 0} showInfo={false} strokeColor="#667eea" size="small" />
                  </div>
                ))}
              </Space>
            )}
          </Card>
        </Col>
        <Col xs={24} md={12}>
          <Card title="最近阅读">
            {!profile.recent_books || profile.recent_books.length === 0 ? (
              <Empty description="暂无阅读记录" />
            ) : (
              <Space direction="vertical" style={{ width: "100%" }}>
                {profile.recent_books.slice(0, 5).map((book: any) => (
                  <Card key={book.id} hoverable size="small" onClick={() => navigate("/books/" + book.id)}>
                    <Text strong>{book.title}</Text>
                    <br /><Text type="secondary">{book.author}</Text>
                    <br /><Text type="secondary" style={{ fontSize: 12 }}>{dayjs(book.created_at).fromNow()}</Text>
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
