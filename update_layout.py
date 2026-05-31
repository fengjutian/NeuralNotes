import pathlib

p = pathlib.Path('frontend/src/components/AppLayout.tsx')
content = p.read_text(encoding='utf-8')

# 1. Add the new imports
# Add Button to Layout import
content = content.replace(
    'import { Layout, Menu } from "antd"',
    'import { Layout, Menu, Button, Tooltip } from "antd"'
)

# Add BulbOutlined to icons
content = content.replace(
    '  ClockCircleOutlined,',
    '  ClockCircleOutlined,\n  BulbOutlined,\n  FileTextOutlined,'
)

# 2. Add useThemeStore import after the last import
content = content.replace(
    '} from "@ant-design/icons"',
    '} from "@ant-design/icons"\nimport { useThemeStore } from "../store/themeStore"'
)

# 3. Add darkMode state inside the component
old_fn_start = '''export default function AppLayout({ children }: Props) {
  const navigate = useNavigate()
  const location = useLocation()
  const [collapsed, setCollapsed] = useState(false)'''

new_fn_start = '''export default function AppLayout({ children }: Props) {
  const navigate = useNavigate()
  const location = useLocation()
  const [collapsed, setCollapsed] = useState(false)
  const { darkMode, toggleDarkMode } = useThemeStore()'''

content = content.replace(old_fn_start, new_fn_start)

# 4. Add the toggle button at the bottom of the sider (right after </Menu>)
old_menu_end = '''        />
      </Sider>'''
new_menu_end = '''        />
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
      </Sider>'''

content = content.replace(old_menu_end, new_menu_end)

# 5. Make the Content background adapt to theme (remove hard-coded #f0f2f5)
# With ConfigProvider darkAlgorithm, this will auto-adapt, but the hard-coded bg overrides it
content = content.replace(
    'style={{ background: "#f0f2f5" }}',
    'style={{}}'
)

p.write_text(content, encoding='utf-8')
print('Updated AppLayout with dark mode toggle')
