import { useState } from "react"
import { useNavigate, useLocation } from "react-router-dom"
import { Layout, Menu, Button, Tooltip } from "antd"
import {
  BookOutlined,
  UploadOutlined,
  SearchOutlined,
  UserOutlined,
  ApartmentOutlined,
  ClockCircleOutlined,
  BulbOutlined,
} from "@ant-design/icons"
import { useThemeStore } from "../store/themeStore"

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
    key: "/timeline",
    icon: <ClockCircleOutlined />,
    label: "时间线",
    path: "/timeline",
  },
  {
    key: "/profile",
    icon: <UserOutlined />,
    label: "画像",
    path: "/profile",
  },
  {
    key: "/graph",
    icon: <ApartmentOutlined />,
    label: "图谱",
    path: "/graph",
  },
]

interface Props {
  children: React.ReactNode
}

export default function AppLayout({ children }: Props) {
  const navigate = useNavigate()
  const location = useLocation()
  const [collapsed, setCollapsed] = useState(false)
  const { darkMode, toggleDarkMode } = useThemeStore()

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
        <div style={{
          position: "absolute",
          bottom: 24,
          left: 0,
          right: 0,
          textAlign: "center",
        }}>
          <Tooltip title={darkMode ? "切换到浅色模式" : "切换到深色模式"} placement="right">
            <Button
              type="text"
              icon={<BulbOutlined style={{ color: darkMode ? "#faad14" : "rgba(255,255,255,0.65)" }} />}
              onClick={toggleDarkMode}
              style={{ color: "rgba(255,255,255,0.85)" }}
            >
              {!collapsed && (darkMode ? "浅色模式" : "深色模式")}
            </Button>
          </Tooltip>
        </div>
      </Sider>
      <Layout style={{ marginLeft: collapsed ? 80 : 200, transition: "margin-left 0.2s" }}>
        <Content style={{}}>
          {children}
        </Content>
      </Layout>
    </Layout>
  )
}
