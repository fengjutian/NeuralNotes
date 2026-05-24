import { useState } from "react"
import { useNavigate, useLocation } from "react-router-dom"
import { Layout, Menu } from "antd"
import {
  BookOutlined,
  UploadOutlined,
  SearchOutlined,
  UserOutlined,
} from "@ant-design/icons"

const { Sider, Content } = Layout

type MenuItem = {
  key: string
  icon: React.ReactNode
  label: string
  path: string
}

const menuItems: MenuItem[] = [
  {
    key: "/books",
    icon: <BookOutlined />,
    label: "书架",
    path: "/books",
  },
  {
    key: "/import",
    icon: <UploadOutlined />,
    label: "导入",
    path: "/import",
  },
  {
    key: "/search",
    icon: <SearchOutlined />,
    label: "搜索",
    path: "/search",
  },
  {
    key: "/profile",
    icon: <UserOutlined />,
    label: "画像",
    path: "/profile",
  },
]

interface Props {
  children: React.ReactNode
}

export default function AppLayout({ children }: Props) {
  const navigate = useNavigate()
  const location = useLocation()
  const [collapsed, setCollapsed] = useState(false)

  const selectedKey = menuItems.find(
    (item) => location.pathname.startsWith(item.key)
  )?.key || "/books"

  const handleMenuClick = (e: { key: string }) => {
    const item = menuItems.find((m) => m.key === e.key)
    if (item) {
      navigate(item.path)
    }
  }

  return (
    <Layout style={{ minHeight: "100vh" }}>
      <Sider
        collapsible
        collapsed={collapsed}
        onCollapse={setCollapsed}
        theme="dark"
        style={{
          position: "fixed",
          left: 0,
          top: 0,
          bottom: 0,
          overflow: "auto",
        }}
      >
        <div
          style={{
            height: 64,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "white",
            fontSize: collapsed ? 14 : 18,
            fontWeight: "bold",
          }}
        >
          {collapsed ? "NN" : "Neural Notes"}
        </div>
        <Menu
          theme="dark"
          mode="inline"
          selectedKeys={[selectedKey]}
          items={menuItems}
          onClick={handleMenuClick}
        />
      </Sider>
      <Layout style={{ marginLeft: collapsed ? 80 : 200, transition: "margin-left 0.2s" }}>
        <Content style={{ background: "#f0f2f5" }}>
          {children}
        </Content>
      </Layout>
    </Layout>
  )
}
