import { useState, useEffect } from "react"
import { useNavigate, useLocation } from "react-router-dom"
import { Layout, Menu, Button, Tooltip, Drawer, Grid } from "antd"
import {
  BookOutlined,
  UploadOutlined,
  SearchOutlined,
  UserOutlined,
  ApartmentOutlined,
  ClockCircleOutlined,
  BulbOutlined,
  MenuOutlined,
} from "@ant-design/icons"
import { useThemeStore } from "../store/themeStore"

const { Sider, Content } = Layout
const { useBreakpoint } = Grid

type MenuItem = {
  key: string
  icon: React.ReactNode
  label: string
  path: string
}

const menuItems: MenuItem[] = [
  { key: "/books", icon: <BookOutlined />, label: "书架", path: "/books" },
  { key: "/import", icon: <UploadOutlined />, label: "导入", path: "/import" },
  { key: "/search", icon: <SearchOutlined />, label: "搜索", path: "/search" },
  { key: "/timeline", icon: <ClockCircleOutlined />, label: "时间线", path: "/timeline" },
  { key: "/profile", icon: <UserOutlined />, label: "画像", path: "/profile" },
  { key: "/graph", icon: <ApartmentOutlined />, label: "图谱", path: "/graph" },
]

interface Props {
  children: React.ReactNode
}

export default function AppLayout({ children }: Props) {
  const navigate = useNavigate()
  const location = useLocation()
  const [collapsed, setCollapsed] = useState(false)
  const [mobileOpen, setMobileOpen] = useState(false)
  const { darkMode, toggleDarkMode } = useThemeStore()
  const screens = useBreakpoint()

  const isMobile = !screens.md

  // Close mobile drawer on route change
  useEffect(() => {
    setMobileOpen(false)
  }, [location.pathname])

  const selectedKey =
    menuItems.find((item) => location.pathname.startsWith(item.key))?.key ||
    "/books"

  const handleMenuClick = (e: { key: string }) => {
    const item = menuItems.find((m) => m.key === e.key)
    if (item) {
      navigate(item.path)
      if (isMobile) setMobileOpen(false)
    }
  }

  const menuContent = (
    <>
      <div
        style={{
          height: 64,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          color: "white",
          fontSize: isMobile ? 20 : collapsed ? 14 : 18,
          fontWeight: "bold",
        }}
      >
        {isMobile || collapsed ? "NN" : "Neural Notes"}
      </div>
      <Menu
        theme="dark"
        mode="inline"
        selectedKeys={[selectedKey]}
        items={menuItems}
        onClick={handleMenuClick}
      />
      <div
        style={{
          position: "absolute",
          bottom: 24,
          left: 0,
          right: 0,
          textAlign: "center",
        }}
      >
        <Tooltip
          title={darkMode ? "切换到浅色模式" : "切换到深色模式"}
          placement="right"
        >
          <Button
            type="text"
            icon={
              <BulbOutlined
                style={{
                  color: darkMode ? "#faad14" : "rgba(255,255,255,0.65)",
                }}
              />
            }
            onClick={toggleDarkMode}
            style={{ color: "rgba(255,255,255,0.85)" }}
          >
            {!collapsed && !isMobile && (darkMode ? "浅色模式" : "深色模式")}
          </Button>
        </Tooltip>
      </div>
    </>
  )

  return (
    <Layout style={{ minHeight: "100vh" }}>
      {isMobile ? (
        <>
          {/* Mobile top bar */}
          <div
            style={{
              height: 48,
              background: darkMode ? "#141414" : "#001529",
              display: "flex",
              alignItems: "center",
              paddingLeft: 12,
              gap: 12,
            }}
          >
            <Button
              type="text"
              icon={<MenuOutlined style={{ color: "white" }} />}
              onClick={() => setMobileOpen(true)}
            />
            <span
              style={{ color: "white", fontWeight: "bold", fontSize: 16 }}
            >
              Neural Notes
            </span>
          </div>
          <Drawer
            placement="left"
            open={mobileOpen}
            onClose={() => setMobileOpen(false)}
            width={260}
            bodyStyle={{ padding: 0, background: "#001529", height: "100%" }}
            headerStyle={{ display: "none" }}
          >
            {menuContent}
          </Drawer>
        </>
      ) : (
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
          {menuContent}
        </Sider>
      )}

      <Layout
        style={{
          marginLeft: isMobile ? 0 : collapsed ? 80 : 200,
          transition: "margin-left 0.2s",
        }}
      >
        <Content
          style={{
            padding: isMobile ? 12 : 24,
            minHeight: "100vh",
            ...(isMobile && !darkMode
              ? { background: "#f5f5f5" }
              : {}),
          }}
        >
          {children}
        </Content>
      </Layout>
    </Layout>
  )
}
