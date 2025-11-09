# FreeCAD WebUI Frontend

Здесь размещается исходный код SPA (React/Vue/Svelte), который будет собираться и упаковываться в qrc для интеграции с QtWebEngine.

Рекомендуемый процесс:
- Разработка SPA в этой папке
- Сборка (npm run build) — результат кладётся в webui/dist/
- Автоматическая упаковка в webui.qrc для интеграции

Пример package.json:

```json
{
  "name": "freecad-webui-frontend",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  },
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  }
}
```

SPA должна экспортировать index.html и статические ассеты в папку dist/ для упаковки.