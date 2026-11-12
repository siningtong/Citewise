import { useState } from 'react'
import type { FormEvent } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { useChatStore } from '@/stores/chatStore'

function AskForm() {
  const [question, setQuestion] = useState('')
  const askQuestion = useChatStore((state) => state.askQuestion)
  const isAsking = useChatStore((state) => state.isAsking)

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    const trimmed = question.trim()
    if (!trimmed) return

    setQuestion('')
    await askQuestion(trimmed)
  }

  return (
    <form className="flex gap-2" onSubmit={handleSubmit}>
      <Input
        value={question}
        onChange={(event) => setQuestion(event.target.value)}
        placeholder="Type your question..."
        maxLength={1000}
        aria-label="Question"
      />
      <Button type="submit" disabled={isAsking || !question.trim()}>
        {isAsking ? 'Thinking...' : 'Ask'}
      </Button>
    </form>
  )
}

export default AskForm
