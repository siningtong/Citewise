import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export type AskResponse = {
  answer: string;
};

export async function ask(question: string): Promise<AskResponse> {
  const response = await api.post<AskResponse>("/ask", { question });
  return response.data;
}
