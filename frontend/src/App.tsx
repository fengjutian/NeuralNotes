import { Routes, Route, Navigate } from 'react-router-dom'
import { Layout } from 'antd'
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

const { Content } = Layout

function App() {
  return (
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
  )
}

export default App
