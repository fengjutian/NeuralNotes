import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { useMutation } from "@tanstack/react-query"
import { Upload, Typography, message, Card, Space, Result, Button } from "antd"
import { InboxOutlined, CheckCircleOutlined } from "@ant-design/icons"
import { importApi } from "../api"

const { Title, Text } = Typography
const { Dragger } = Upload

export default function ImportPage() {
  const navigate = useNavigate()
  const [result, setResult] = useState<any>(null)

  const uploadMutation = useMutation({
    mutationFn: (file: File) => importApi.upload(file),
    onSuccess: (response) => {
      setResult(response.data)
      message.success("导入成功！")
    },
    onError: (error: any) => {
      message.error(error.response?.data?.detail || "导入失败")
    },
  })

  const handleFileChange = (info: any) => {
    const file = info.file.originFileObj || info.file
    if (file) {
      uploadMutation.mutate(file)
    }
    return false
  }

  const handleViewBook = () => {
    if (result?.book_id) {
      navigate("/books/" + result.book_id)
    }
  }

  if (result) {
    return (
      <Card>
        <Result
          icon={<CheckCircleOutlined style={{ color: "#52c41a" }} />}
          title="导入成功！"
          subTitle={\`已成功导入《\${result.title}》\`}
          extra={[
            <Button type="primary" key="view" onClick={handleViewBook}>
              查看书籍
            </Button>,
            <Button key="continue" onClick={() => setResult(null)}>
              继续导入
            </Button>,
          ]}
          subDescription={
            <Space direction="vertical">
              <Text>作者：{result.author}</Text>
              <Text>笔记数量：{result.highlight_count} 条</Text>
            </Space>
          }
        />
      </Card>
    )
  }

  return (
    <div>
      <Title level={2}>导入书籍</Title>
      <Text type="secondary" style={{ marginBottom: 24, display: "block" }}>
        上传微信读书导出的 Markdown 文件
      </Text>

      <Dragger
        name="file"
        multiple={false}
        accept=".md"
        showUploadList={false}
        beforeUpload={handleFileChange}
        className="upload-dragger"
      >
        <p className="ant-upload-drag-icon">
          <InboxOutlined style={{ fontSize: 64, color: "#667eea" }} />
        </p>
        <p className="ant-upload-text">点击或拖拽文件到此区域上传</p>
        <p className="ant-upload-hint">
          支持微信读书导出的 .md 文件
        </p>
      </Dragger>

      {uploadMutation.isPending && (
        <Text type="secondary" style={{ display: "block", textAlign: "center", marginTop: 16 }}>
          正在导入，请稍候...
        </Text>
      )}
    </div>
  )
}
