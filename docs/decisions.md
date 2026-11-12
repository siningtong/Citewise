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

## Vector store: PostgreSQL + pgvector
**Date:** 2026-11-12
**Status:** Planned
**Decision:** Store documents, chunks, and embeddings in PostgreSQL with the pgvector extension.
**Why:** I already know PostgreSQL, and keeping documents, chunks, and vectors in one database makes joins and filtering simple. The data size of this project doesn't need a dedicated vector database.
**Alternatives:** Pinecone (managed), Qdrant, Weaviate. Worth revisiting if the data grows a lot or advanced filtering and hybrid search become important.

## License: MIT
**Date:** 2026-11-12
**Status:** Implemented
**Decision:** Publish the project under the MIT License.
**Why:** It's a public portfolio project. MIT lets others read and reuse the code as long as they keep the attribution.
