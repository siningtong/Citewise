# Citewise

A document Q&A app that answers questions using only your documents, and cites the exact passage behind every answer. If the answer isn't in the documents, it says so.

> Work in progress.

## Tech stack

- **Backend:** Python 3.11, FastAPI
- **Frontend:** React + TypeScript (Vite) — coming soon
- **LLM:** OpenAI — coming soon
- **Database:** PostgreSQL + pgvector — coming soon

## Local development

### Prerequisites

- Python 3.10+
- Node.js 24 (for the frontend)

### Backend

All backend commands run from the `backend/` directory.

1. Create a virtual environment (first time only):

   ```bash
   cd backend
   python3 -m venv .venv
   ```

2. Activate the virtual environment (every time you open a new terminal):

   ```bash
   source .venv/bin/activate
   ```

   Your prompt should now start with `(.venv)`. To leave it, run `deactivate`.

3. Install dependencies (first time, and whenever `requirements.txt` changes):

   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:

   ```bash
   fastapi dev app/main.py
   ```

   The server reloads automatically when you save a file. Stop it with `Ctrl + C`.

5. Check that it works:

   - Health check: http://localhost:8000/health
   - Interactive API docs: http://localhost:8000/docs

## Design decisions

See [docs/decisions.md](docs/decisions.md).

## License

[MIT](LICENSE)
