import pathlib

p = pathlib.Path('frontend/src/App.tsx')
content = p.read_text(encoding='utf-8')

# Replace the entire App component to wrap with ConfigProvider for dark mode
new_app = '''import { Routes, Route, Navigate } from 'react-router-dom'
import { Layout, ConfigProvider, theme as antdTheme } from 'antd'
import ErrorBoundary from './components/ErrorBoundary'
import AppLayout from './components/AppLayout'
import BooksPage from './pages/BooksPage'
import BookDetailPage from './pages/BookDetailPage'
import ImportPage from './pages/ImportPage'
import SearchPage from './pages/SearchPage'
import ProfilePage from './pages/ProfilePage'
import GraphPage from './pages/GraphPage'
import TimelinePage from './pages/TimelinePage'
import NotFoundPage from './pages/NotFoundPage'
import { useThemeStore } from './store/themeStore'

const { Content } = Layout

function App() {
  const darkMode = useThemeStore((s) => s.darkMode)

  return (
    <ConfigProvider
      theme={{
        algorithm: darkMode ? antdTheme.darkAlgorithm : antdTheme.defaultAlgorithm,
        token: {
          colorPrimary: '#667eea',
          colorSuccess: '#52c41a',
          colorWarning: '#faad14',
          colorError: '#ff4d4f',
          borderRadius: 6,
        },
      }}
    >
      <ErrorBoundary>
        <AppLayout>
          <Content style={{ padding: "24px", minHeight: "100vh" }}>
            <Routes>
              <Route path="/" element={<Navigate to="/books" replace />} />
              <Route path="/books" element={<BooksPage />} />
              <Route path="/books/:id" element={<BookDetailPage />} />
              <Route path="/import" element={<ImportPage />} />
              <Route path="/search" element={<SearchPage />} />
              <Route path="/timeline" element={<TimelinePage />} />
              <Route path="/profile" element={<ProfilePage />} />
              <Route path="/graph" element={<GraphPage />} />
              <Route path="*" element={<NotFoundPage />} />
            </Routes>
          </Content>
        </AppLayout>
      </ErrorBoundary>
    </ConfigProvider>
  )
}

export default App
'''

p.write_text(new_app, encoding='utf-8')
print('Updated App.tsx with dark mode ConfigProvider')
