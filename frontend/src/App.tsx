import AskForm from '@/components/AskForm'
import MessageList from '@/components/MessageList'
import { Button } from '@/components/ui/button'
import { useChatStore } from '@/stores/chatStore'

function App() {
  const hasMessages = useChatStore((state) => state.messages.length > 0)
  const clearMessages = useChatStore((state) => state.clearMessages)

  return (
    <main className="mx-auto flex min-h-svh max-w-3xl flex-col gap-6 px-4 py-10">
      <header className="flex items-start justify-between gap-4">
        <div>
          <h1 className="text-3xl font-semibold tracking-tight">Citewise</h1>
          <p className="text-muted-foreground">
            Ask a question about your documents.
          </p>
        </div>
        {hasMessages && (
          <Button variant="outline" onClick={clearMessages}>
            Clear
          </Button>
        )}
      </header>

      <MessageList />
      <AskForm />
    </main>
  )
}

export default App
