import styled from 'styled-components'
import { useEffect, useState } from 'react'

const Container = styled.div`
  padding: 1rem;
  font-family: Arial, sans-serif;
`

const ButtonGroup = styled.div`
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
`

const Button = styled.button`
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background: #f0f0f0;
  cursor: pointer;
  &:hover {
    background: #e0e0e0;
  }
`

const LogArea = styled.pre`
  background: #f6f6f6;
  padding: 1rem;
  border-radius: 4px;
  white-space: pre-wrap;
  font-family: monospace;
  max-height: 300px;
  overflow-y: auto;
`

function App() {
  const [logs, setLogs] = useState<string[]>([])

  const addLog = (msg: string) => {
    setLogs(prev => [...prev, msg])
  }

  useEffect(() => {
    if (!window.backend) {
      addLog('Backend not connected')
      return
    }

    window.backend.objectCreated.connect((info) => {
      addLog(`objectCreated: ${JSON.stringify(info)}`)
    })

    window.backend.selectionChanged.connect((payload) => {
      addLog(`selectionChanged: ${JSON.stringify(payload)}`)
    })

    addLog('Connected to backend')
  }, [])

  const handleCreateBox = () => {
    try {
      const params = { type: 'box', size: { x: 10, y: 10, z: 10 } }
      const res = window.backend?.createObject(params)
      addLog(`createObject -> ${JSON.stringify(res)}`)
    } catch (e) {
      addLog(`Error: ${e}`)
    }
  }

  const handleGetDocuments = () => {
    try {
      const docs = window.backend?.getDocuments()
      addLog(`documents -> ${JSON.stringify(docs)}`)
    } catch (e) {
      addLog(`Error: ${e}`)
    }
  }

  return (
    <Container>
      <h2>FreeCAD WebUI</h2>
      <ButtonGroup>
        <Button onClick={handleCreateBox}>Create Box</Button>
        <Button onClick={handleGetDocuments}>Get Documents</Button>
      </ButtonGroup>
      <LogArea>
        {logs.map((log, i) => (
          <div key={i}>{log}</div>
        ))}
      </LogArea>
    </Container>
  )
}

export default App