# Design Decisions

A short record of the main technical decisions in this project: what was decided, why, and what else was considered.

## Template

```markdown
## <Topic>
**Date:** YYYY-MM-DD
**Status:** Planned | Implemented | Replaced
**Decision:** What I chose.
**Why:** The main reasons.
**Alternatives:** What else I considered, and why I didn't pick it.
```

---

## Monorepo
**Date:** 2026-11-12
**Status:** Implemented
**Decision:** Keep the frontend (`frontend/`) and backend (`backend/`) in one repository.
**Why:** One link and one README show the whole project. A feature that touches both sides lands in a single commit. CI and `docker-compose` live in one place.
**Alternatives:** Separate repositories. That makes sense when different teams own each side or they release on different schedules, which isn't the case for a single-developer project.

## Backend framework: FastAPI
**Date:** 2026-11-12
**Status:** Implemented
**Decision:** Build the backend with FastAPI.
**Why:** Request and response shapes are declared once as Pydantic models, and FastAPI validates every request against them (bad input gets a 422 before my code runs). The same models generate the OpenAPI docs at `/docs`, so the docs never drift from the code. The app will spend most of its time waiting on OpenAI and the database, and FastAPI supports `async` endpoints natively. I've used both FastAPI and Flask in production, and this combination makes FastAPI the better fit here.
**Alternatives:** Flask is simpler and has a larger ecosystem of extensions, but validation and API docs need extra libraries, and async support is an add-on rather than the default. Django is more than this project needs.

## Node.js 24 LTS
**Date:** 2026-11-12
**Status:** Implemented
**Decision:** Use Node.js 24 for the frontend toolchain.
**Why:** Vite 8 requires Node 20.19+ or 22.12+. Node 24 is an LTS release supported until April 2028, while Node 22 reaches end of life in April 2027.
**Alternatives:** Node 26 is newer, but it only became LTS in late October 2026, so some packages may not support it yet.

## LLM provider: OpenAI
**Date:** 2026-11-12
**Status:** Planned
**Decision:** Use OpenAI. Start with `gpt-5-nano` during development and compare it with `gpt-5-mini` once evals are in place. Use `text-embedding-3-small` for embeddings.
**Why:** Low cost for a personal project, and I have used OpenAI in production before. Comparing models with an eval set will turn the final model choice into a measured decision.
**Alternatives:** Anthropic Claude and Google Gemini also have low-cost models. A local open-source embedding model would be free.

## Reasoning effort: low
**Date:** 2026-11-12
**Status:** Implemented (to be re-checked with the eval set in stage 6)
**Decision:** Call `gpt-5-nano` with reasoning effort `low` by default, configurable through `OPENAI_REASONING_EFFORT`.
**Why:** Usage logging showed that most output tokens were hidden reasoning tokens, and a short answer took almost 10 seconds. One comparison on the same question:

| Effort | Output tokens | Reasoning tokens | Latency |
|---|---|---|---|
| Not set | 1,213 | 960 | 9.8 s |
| `low` | 140 | 64 | 2.9 s |

With `low`, latency dropped about 3x and estimated cost per answer about 8x. This is a single sample, so the numbers will vary; answer quality still needs to be measured properly with the eval set in stage 6.
**Alternatives:** Leave the model default (slower and more expensive). Try `minimal` for even lower latency. Streaming (stage 3) makes the wait feel shorter but doesn't reduce cost.

## Vector store: PostgreSQL + pgvector
**Date:** 2026-11-12
**Status:** Planned
**Decision:** Store documents, chunks, and embeddings in PostgreSQL with the pgvector extension.
**Why:** I already know PostgreSQL, and keeping documents, chunks, and vectors in one database makes joins and filtering simple. The data size of this project doesn't need a dedicated vector database.
**Alternatives:** Pinecone (managed), Qdrant, Weaviate. Worth revisiting if the data grows a lot or advanced filtering and hybrid search become important.

## HTTP client: axios
**Date:** 2026-11-12
**Status:** Implemented
**Decision:** Use axios for frontend API calls, through a shared client in `frontend/src/api.ts`.
**Why:** It throws on 4xx/5xx responses automatically, parses JSON for me, and a single instance keeps the base URL in one place.
**Alternatives:** The built-in `fetch` (no dependency). Streaming responses in stage 3 may still need `fetch`, since reading a response stream is built into it.

## Frontend state: Zustand
**Date:** 2026-11-12
**Status:** Implemented
**Decision:** Use Zustand for client state (the chat history and whether a request is in flight), in `frontend/src/stores/`.
**Why:** Several components need the same chat state. Zustand needs very little boilerplate and no Provider. I've used Redux and Valtio before; for an app this size, Redux Toolkit adds more structure than it needs.
**Alternatives:** Redux Toolkit, Valtio, Jotai, React Context. Data that lives on the server (document list, processing status) may move to TanStack Query later, so the store only holds client state.

## UI: shadcn/ui + Tailwind CSS
**Date:** 2026-11-12
**Status:** Implemented
**Decision:** Build the UI with shadcn/ui (Radix base, Nova preset) on Tailwind CSS v4.
**Why:** shadcn/ui copies component source into the repo, so every component can be read and changed. It's built on Radix, which handles keyboard and screen-reader accessibility. Tailwind keeps styles next to the markup.
**Alternatives:** Material UI (complete, but hard to move away from the Material look), Ant Design (strong for admin dashboards, less suited to a chat-style app), Mantine.

## License: MIT
**Date:** 2026-11-12
**Status:** Implemented
**Decision:** Publish the project under the MIT License.
**Why:** It's a public portfolio project. MIT lets others read and reuse the code as long as they keep the attribution.
