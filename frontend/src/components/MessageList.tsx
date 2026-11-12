import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { useChatStore } from '@/stores/chatStore'

function MessageList() {
  const messages = useChatStore((state) => state.messages)

  if (messages.length === 0) {
    return <p className="text-muted-foreground">No questions yet.</p>
  }

  return (
    <ul className="flex flex-col gap-4">
      {messages.map((message) => (
        <li key={message.id}>
          <Card>
            <CardHeader>
              <CardTitle>{message.question}</CardTitle>
            </CardHeader>
            <CardContent>
              {message.status === 'pending' && (
                <p className="animate-pulse text-muted-foreground">Thinking...</p>
              )}
              {message.status === 'done' && (
                <p className="whitespace-pre-wrap">{message.answer}</p>
              )}
              {message.status === 'error' && (
                <p className="text-destructive">{message.error}</p>
              )}
            </CardContent>
          </Card>
        </li>
      ))}
    </ul>
  )
}

export default MessageList
