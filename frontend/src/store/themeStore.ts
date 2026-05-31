import { create } from "zustand"
import { persist } from "zustand/middleware"

interface ThemeState {
  darkMode: boolean
  toggleDarkMode: () => void
  setDarkMode: (dark: boolean) => void
}

export const useThemeStore = create<ThemeState>()(
  persist(
    (set) => ({
      darkMode: false,
      toggleDarkMode: () =>
        set((state) => ({ darkMode: !state.darkMode })),
      setDarkMode: (dark: boolean) => set({ darkMode: dark }),
    }),
    {
      name: "neural-notes-theme",
    }
  )
)
