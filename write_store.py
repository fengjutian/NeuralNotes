import pathlib

content = '''import { create } from "zustand"
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
'''

p = pathlib.Path('frontend/src/store/themeStore.ts')
p.write_text(content, encoding='utf-8')
print('Written themeStore.ts')
