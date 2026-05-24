import axios from 'axios'

const api = axios.create({
  baseURL: "/api/v1",
  timeout: 30000,
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error)
    return Promise.reject(error)
  }
)

// Types
export interface Book {
  id: string
  title: string
  author: string
  category?: string
  isbn?: string
  reading_time?: string
  progress?: number
  reading_date?: string
  highlight_count: number
  created_at: string
  updated_at: string
}

export interface Highlight {
  id: string
  book_id: string
  content: string
  chapter?: string
  create_time?: string
  url?: string
  created_at: string
}

export interface BookListResponse {
  items: Book[]
  total: number
  page: number
  page_size: number
}

export interface ImportResponse {
  status: string
  book_id: string
  title: string
  author: string
  highlight_count: number
}

export interface SearchResult {
  id: string
  content: string
  score: number
  book_title?: string
  chapter?: string
}

export interface Profile {
  total_books: number
  total_highlights: number
  categories: Record<string, number>
  reading_time_total: string
  recent_books: Book[]
}

// API Methods
export const bookApi = {
  list: (params: { page?: number; page_size?: number; category?: string }) =>
    api.get<BookListResponse>("/books", { params }),
  
  get: (id: string) =>
    api.get<Book>("/books/" + id),
  
  delete: (id: string) =>
    api.delete("/books/" + id),
}

export const importApi = {
  upload: async (file: File) => {
    const formData = new FormData()
    formData.append("file", file)
    return api.post<ImportResponse>("/import", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    })
  },
}

export const searchApi = {
  search: (params: { q: string; limit?: number }) =>
    api.get<SearchResult[]>("/search", { params }),
}

export const profileApi = {
  get: () =>
    api.get<Profile>("/profile"),
}

export default api
