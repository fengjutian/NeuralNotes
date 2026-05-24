import { Routes, Route, Navigate } from 'react-router-dom'
import { Layout } from 'antd'
import type { MenuProps } from 'antd'
import AppLayout from './components/AppLayout'
import BooksPage from './pages/BooksPage'
import BookDetailPage from './pages/BookDetailPage'
import ImportPage from './pages/ImportPage'
import SearchPage from './pages/SearchPage'
import ProfilePage from './pages/ProfilePage'
import GraphPage from './pages/GraphPage'

const { Content } = Layout

function App() {
  return (
    <AppLayout>
      <Content style={{ padding: "24px", minHeight: "100vh" }}>
        <Routes>
          <Route path="/" element={<Navigate to="/books" replace />} />
          <Route path="/books" element={<BooksPage />} />
          <Route path="/books/:id" element={<BookDetailPage />} />
          <Route path="/import" element={<ImportPage />} />
          <Route path="/search" element={<SearchPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/graph" element={<GraphPage />} />
        </Routes>
      </Content>
    </AppLayout>
  )
}

export default App
