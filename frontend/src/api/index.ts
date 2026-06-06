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
  emotion?: string
  domain?: string
}

export interface BookListResponse {
  items: Book[]
  total: number
  page: number
  page_size: number
}

export interface HighlightListResponse {
  items: Highlight[]
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
  book_id?: string
  chapter?: string
}

export interface Profile {
  total_books: number
  total_highlights: number
  categories: Record<string, number>
  reading_time_total: string
  recent_books: Book[]
  _summary?: { avg_highlights_per_book: number }
  _preferences?: {
    favorite_categories: { name: string; count: number }[]
    reading_emotions: { type: string; count: number }[]
    domains_of_interest: { name: string; count: number }[]
  }
  _tendencies?: {
    dominant_emotion: string
    primary_domain: string
  }
}

export interface Preferences {
  categories: { name: string; count: number; percentage: number }[]
  authors: { name: string; book_count: number }[]
  topics: string[]
  reading_times: { morning: number; afternoon: number; evening: number; night: number }
}

export interface BlindSpots {
  missing_domains: string[]
  suggestions: { type: string; message: string; priority: string }[]
  stats: { active_domains: number; potential_domains: number; coverage_percentage: number }
}

export interface TimelineYear {
  year: number
  highlight_count: number
  theme: string
  dominant_domains: string[]
  top_books: { title: string; highlights: number }[]
}

export interface TimelinePivotPoint {
  year: number
  type: string
  message: string
  highlight_count?: number
  new_domains?: string[]
  growth_rate?: number
}

export interface Timeline {
  years: TimelineYear[]
  pivot_points: TimelinePivotPoint[]
  total_highlights: number
  year_count: number
}

export interface GraphNode {
  id: string
  type: string
  label: string
  properties: Record<string, any>
}

export interface GraphEdge {
  source: string
  target: string
  type: string
  properties: Record<string, any>
}

export interface GraphData {
  nodes: GraphNode[]
  edges: GraphEdge[]
}

// API Methods
export const bookApi = {
  list: (params: { page?: number; page_size?: number; category?: string }) =>
    api.get<BookListResponse>("/books", { params }),
  
  get: (id: string) =>
    api.get<Book>("/books/" + id),
  
  update: (id: string, data: Partial<Book>) =>
    api.put<Book>("/books/" + id, data),

  delete: (id: string) =>
    api.delete("/books/" + id),

  getHighlights: (id: string, params?: { page?: number; page_size?: number }) =>
    api.get<HighlightListResponse>("/books/" + id + "/highlights", { params }),
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
  search: (params: { q: string; limit?: number; book_id?: string; min_score?: number }) =>
    api.get<{ query: string; results: SearchResult[]; total: number; error?: string }>("/search", { params }),

  aggregate: (topic: string, limit?: number) =>
    api.post("/search/aggregate", null, { params: { topic, limit } }),

  indexBook: (bookId: string) =>
    api.post("/search/index", null, { params: { book_id: bookId } }),
}

export const profileApi = {
  get: () =>
    api.get<Profile>("/profile"),

  getPreferences: () =>
    api.get<Preferences>("/profile/preferences"),

  getBlindSpots: () =>
    api.get<BlindSpots>("/profile/blind-spots"),
}

export const timelineApi = {
  get: (params?: { start_year?: number; end_year?: number }) =>
    api.get<Timeline>("/timeline", { params }),

  getPivotPoints: () =>
    api.get<{ pivot_points: TimelinePivotPoint[]; count: number }>("/timeline/pivot-points"),
}

export const graphApi = {
  get: (limit?: number) =>
    api.get<GraphData>("/graph", { params: { limit } }),

  getForBook: (bookId: string) =>
    api.get<GraphData>("/graph/book/" + bookId),

  getConcept: (name: string) =>
    api.get("/graph/concept/" + name),
}

export const exportApi = {
  download: (bookId: string, format: string = "md") =>
    api.get("/export/books/" + bookId + "/export/download?format=" + format, {
      responseType: "blob",
    }),
}

export const highlightApi = {
  delete: (highlightId: string) =>
    api.delete("/highlights/" + highlightId),
}

export const analyzeApi = {
  trigger: (params: { book_id: string; highlight_ids?: string[] }) =>
    api.post("/analyze", params),

  getJobStatus: (jobId: string) =>
    api.get("/analyze/" + jobId),
}

export const syncApi = {
  syncAll: () =>
    api.post("/sync/all"),
}

export default api
