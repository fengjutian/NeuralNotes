import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { useMutation } from "@tanstack/react-query"
import { Upload, Typography, message, Card, Space, Button, Progress, List, Tag, Alert } from "antd"
import { InboxOutlined, CheckCircleOutlined, FileTextOutlined, InfoCircleOutlined } from "@ant-design/icons"
import { importApi } from "../api"

const { Title, Text, Paragraph } = Typography
const { Dragger } = Upload

export default function ImportPage() {
  const navigate = useNavigate()
  const [results, setResults] = useState<any[]>([])
  const [currentFile, setCurrentFile] = useState<File | null>(null)
  const [preview, setPreview] = useState<string | null>(null)
  const [uploadProgress, setUploadProgress] = useState(0)

  const uploadMutation = useMutation({
    mutationFn: async (file: File) => {
      setCurrentFile(file)
      setUploadProgress(10)
      const reader = new FileReader()
      reader.onload = (e) => {
        const text = (e.target?.result as string)?.slice(0, 500) || ""
        setPreview(text)
      }
      reader.readAsText(file)
      setUploadProgress(40)
      const response = await importApi.upload(file)
      setUploadProgress(100)
      return response
    },
    onSuccess: (response) => {
      setResults((prev) => [response.data, ...prev])
      message.success("导入成功！")
      setCurrentFile(null)
      setPreview(null)
      setUploadProgress(0)
    },
    onError: (error: any) => {
      const detail = error.response?.data?.detail || error.message || "导入失败"
      message.error(detail)
      setCurrentFile(null)
      setUploadProgress(0)
    },
  })

  const handleFileChange = (info: any) => {
    const file: File = info.file.originFileObj || info.file
    if (!file) return false
    const validExtensions = [".md", ".txt", ".markdown"]
    const ext = "." + file.name.split(".").pop()?.toLowerCase()
    if (!validExtensions.includes(ext)) {
      message.warning("请上传 .md 或 .txt 格式的文件")
      return false
    }
    if (file.size > 50 * 1024 * 1024) {
      message.warning("文件大小不能超过 50MB")
      return false
    }
    uploadMutation.mutate(file)
    return false
  }

  const handleViewBook = (bookId: string) => {
    navigate("/books/" + bookId)
  }

  return (
    <div>
      <Title level={2}>导入书籍</Title>
      <Text type="secondary" style={{ marginBottom: 16, display: "block" }}>
        上传微信读书导出的 Markdown 文件，支持 .md / .txt 格式
      </Text>

      <Alert
        message="支持格式"
        description="支持微信读书笔记导出的 Markdown 格式，也支持简单的书名+笔记文本格式。文件大小不超过 50MB。"
        type="info"
        showIcon
        icon={<InfoCircleOutlined />}
        style={{ marginBottom: 24 }}
      />

      <Dragger
        name="file"
        multiple
        accept=".md,.txt,.markdown"
        showUploadList={false}
        beforeUpload={handleFileChange}
        className="upload-dragger"
        disabled={uploadMutation.isPending}
      >
        <p className="ant-upload-drag-icon">
          <InboxOutlined
            style={{
              fontSize: 64,
              color: uploadMutation.isPending ? "#ccc" : "#667eea",
            }}
          />
        </p>
        <p className="ant-upload-text">
          {uploadMutation.isPending
            ? "正在导入..."
            : "点击或拖拽文件到此区域上传"}
        </p>
        <p className="ant-upload-hint">
          支持微信读书导出的 .md 文件，可批量上传
        </p>
      </Dragger>

      {uploadMutation.isPending && currentFile && (
        <Card size="small" style={{ marginTop: 16 }}>
          <Space direction="vertical" style={{ width: "100%" }}>
            <Space>
              <FileTextOutlined />
              <Text strong>{currentFile.name}</Text>
              <Text type="secondary">
                ({(currentFile.size / 1024).toFixed(1)} KB)
              </Text>
            </Space>
            <Progress percent={uploadProgress} status="active" size="small" />
            {preview && (
              <Card
                size="small"
                style={{
                  background: "#f6f8fa",
                  maxHeight: 120,
                  overflow: "auto",
                }}
              >
                <Text type="secondary" style={{ fontSize: 12 }}>
                  文件预览：
                </Text>
                <Paragraph
                  ellipsis={{ rows: 3 }}
                  style={{ fontSize: 12, whiteSpace: "pre-wrap" }}
                >
                  {preview}
                </Paragraph>
              </Card>
            )}
          </Space>
        </Card>
      )}

      {uploadMutation.isPending && !currentFile && (
        <Text
          type="secondary"
          style={{ display: "block", textAlign: "center", marginTop: 16 }}
        >
          正在导入，请稍候...
        </Text>
      )}

      {results.length > 0 && (
        <Card title="📋 导入记录" style={{ marginTop: 24 }} size="small">
          <List
            dataSource={results}
            renderItem={(item: any, index: number) => (
              <List.Item
                key={index}
                extra={
                  <Button
                    type="link"
                    onClick={() => handleViewBook(item.book_id)}
                  >
                    查看
                  </Button>
                }
              >
                <List.Item.Meta
                  avatar={
                    <CheckCircleOutlined
                      style={{ color: "#52c41a", fontSize: 20 }}
                    />
                  }
                  title={item.title}
                  description={
                    <Space>
                      <Text type="secondary">{item.author}</Text>
                      <Tag>{item.highlight_count} 条笔记</Tag>
                    </Space>
                  }
                />
              </List.Item>
            )}
          />
        </Card>
      )}
    </div>
  )
}
