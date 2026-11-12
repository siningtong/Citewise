import axios from 'axios'
import { create } from 'zustand'
import { ask } from '../api'

export type MessageStatus = 'pending' | 'done' | 'error'

export type Message = {
  id: string
  question: string
  answer?: string
  error?: string
  status: MessageStatus
}

type ChatState = {
  messages: Message[]
  isAsking: boolean
  askQuestion: (question: string) => Promise<void>
  clearMessages: () => void
}

function toErrorMessage(err: unknown): string {
  if (axios.isAxiosError(err)) {
    return err.response
      ? `Request failed with status ${err.response.status}`
      : 'Could not reach the server'
  }
  return 'Something went wrong'
}

export const useChatStore = create<ChatState>()((set) => ({
  messages: [],
  isAsking: false,

  askQuestion: async (question) => {
    const id = crypto.randomUUID()

    // Show the question right away, then fill in the answer when it arrives.
    set((state) => ({
      isAsking: true,
      messages: [...state.messages, { id, question, status: 'pending' }],
    }))

    try {
      const data = await ask(question)
      set((state) => ({
        messages: state.messages.map((message) =>
          message.id === id
            ? { ...message, answer: data.answer, status: 'done' }
            : message,
        ),
      }))
    } catch (err) {
      set((state) => ({
        messages: state.messages.map((message) =>
          message.id === id
            ? { ...message, error: toErrorMessage(err), status: 'error' }
            : message,
        ),
      }))
    } finally {
      set({ isAsking: false })
    }
  },

  clearMessages: () => set({ messages: [] }),
}))
