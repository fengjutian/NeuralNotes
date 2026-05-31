import { useState } from "react"
import { useQuery } from "@tanstack/react-query"
import { useNavigate } from "react-router-dom"
import { Card, Input, Spin, Empty, Typography, Space, Tag, Select, Button, Alert } from "antd"
import { SearchOutlined, BookOutlined, FilterOutlined, ClearOutlined } from "@ant-design/icons"
import { searchApi, bookApi } from "../api"

const { Title, Text, Paragraph } = Typography

const SEARCH_HISTORY_KEY = "neural_notes_search_history"

export default function SearchPage() {
  const navigate = useNavigate()
  const [query, setQuery] = useState("")
  const [bookId, setBookId] = useState<string | undefined>(undefined)
  const [minScore, setMinScore] = useState<number | undefined>(undefined)
  const [searchHistory, setSearchHistory] = useState<string[]>(
    JSON.parse(localStorage.getItem(SEARCH_HISTORY_KEY) || "[]")
  )
  const [showFilters, setShowFilters] = useState(false)

  const searchParams = {
    q: query,
    limit: 50,
    ...(bookId && { book_id: bookId }),
    ...(minScore !== undefined && { min_score: minScore }),
  }

  const { data, isLoading, error } = useQuery({
    queryKey: ["search", searchParams],
    queryFn: () => searchApi.search(searchParams),
    enabled: query.length > 0,
  })

  const { data: booksListData } = useQuery({
    queryKey: ["books", "list"],
    queryFn: () => bookApi.list({ page: 1, page_size: 200 }),
    enabled: showFilters,
  })

  const handleSearch = (value: string) => {
    const trimmed = value.trim()
    if (!trimmed) return
    setQuery(trimmed)
    // Save to search history
    const updated = [trimmed, ...searchHistory.filter((h) => h !== trimmed)].slice(0, 10)
    setSearchHistory(updated)
    localStorage.setItem(SEARCH_HISTORY_KEY, JSON.stringify(updated))
  }

  const clearHistory = () => {
    setSearchHistory([])
    localStorage.removeItem(SEARCH_HISTORY_KEY)
  }

  const responseData = data?.data
  const results: any[] = Array.isArray(responseData)
    ? responseData
    : responseData?.results || []
  const total = !Array.isArray(responseData) ? (responseData?.total || results.length) : results.length

  return (
    <div>
      <Title level={2}>语义搜索</Title>
      
      <Input.Search
        placeholder="输入关键词搜索笔记内容..."
        allowClear
        enterButton={<SearchOutlined />}
        size="large"
        onSearch={handleSearch}
        style={{ maxWidth: 600, marginBottom: 12 }}
      />

      <Space wrap style={{ marginBottom: 16 }}>
        <Button
          icon={<FilterOutlined />}
          size="small"
          onClick={() => setShowFilters(!showFilters)}
        >
          {showFilters ? "收起筛选" : "高级筛选"}
        </Button>
        {showFilters && (
          <>
            <Select
              placeholder="按书籍筛选"
              allowClear
              style={{ width: 200 }}
              value={bookId}
              onChange={setBookId}
              options={(booksListData?.data?.items || []).map((b: any) => ({
                label: b.title,
                value: b.id,
              }))}
            />
            <Select
              placeholder="最低相关度"
              allowClear
              style={{ width: 140 }}
              value={minScore}
              onChange={setMinScore}
              options={[
                { label: ">= 0.3 (宽松)", value: 0.3 },
                { label: ">= 0.5 (中等)", value: 0.5 },
                { label: ">= 0.7 (严格)", value: 0.7 },
              ]}
            />
          </>
        )}
      </Space>

      {searchHistory.length > 0 && !query && (
        <div style={{ marginBottom: 16 }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <Text type="secondary">搜索历史</Text>
            <Button type="link" size="small" icon={<ClearOutlined />} onClick={clearHistory}>
              清除历史
            </Button>
          </div>
          <Space wrap>
            {searchHistory.map((h, i) => (
              <Tag
                key={i}
                style={{ cursor: "pointer" }}
                onClick={() => handleSearch(h)}
              >
                {h}
              </Tag>
            ))}
          </Space>
        </div>
      )}

      {isLoading && (
        <div style={{ textAlign: "center", padding: 50 }}>
          <Spin size="large" />
        </div>
      )}

      {error && (
        <Alert
          type="error"
          message="搜索失败"
          description={(error as Error)?.message || "无法完成搜索，请检查服务是否可用"}
          showIcon
          style={{ marginBottom: 16 }}
        />
      )}

      {!query && !isLoading && (
        <Empty description="输入关键词开始搜索" />
      )}

      {query && !isLoading && results.length === 0 && !error && (
        <Empty description="未找到相关笔记" />
      )}

      {results.length > 0 && (
        <Space direction="vertical" style={{ width: "100%" }}>
          <Space wrap>
            <Text type="secondary">
              找到 {results.length} 条相关笔记
              {total > results.length ? ` (共 ${total} 条)` : ""}
            </Text>
            {data?.data?.error && <Tag color="orange">{data.data.error}</Tag>}
          </Space>
          {results.map((item: any, index: number) => (
            <Card
              key={item.id || index}
              hoverable
              onClick={() => navigate("/books/" + item.book_id)}
            >
              <Paragraph
                ellipsis={{ rows: 3, expandable: true, symbol: "展开" }}
                style={{ marginBottom: 8 }}
              >
                <HighlightMatch text={item.content} query={query} />
              </Paragraph>
              <Space wrap>
                {item.book_title && (
                  <Tag icon={<BookOutlined />} color="blue">
                    {item.book_title}
                  </Tag>
                )}
                {item.chapter && <Tag>{item.chapter}</Tag>}
                <Tag color="green">
                  相关度 {Math.round((item.score || 0) * 100)}%
                </Tag>
              </Space>
            </Card>
          ))}
        </Space>
      )}
    </div>
  )
}

function HighlightMatch({ text, query }: { text: string; query: string }) {
  if (!query.trim()) return <>{text}</>
  const idx = text.toLowerCase().indexOf(query.toLowerCase())
  if (idx === -1) return <>{text}</>
  const before = text.slice(0, idx)
  const match = text.slice(idx, idx + query.length)
  const after = text.slice(idx + query.length)
  return (
    <>
      {before}
      <mark style={{ background: "#faad14", padding: "0 2px", borderRadius: 2 }}>{match}</mark>
      {after}
    </>
  )
}
