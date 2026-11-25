# Citewise

A document Q&A app that answers questions using only your documents, and cites the exact passage behind every answer. If the answer isn't in the documents, it says so.

> Work in progress.

## Tech stack

- **Backend:** Python 3.11, FastAPI
- **Frontend:** React + TypeScript (Vite), Tailwind CSS, shadcn/ui, Zustand, axios
- **LLM:** OpenAI (Responses API)
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

4. Create a `.env` file in `backend/` with your OpenAI API key (first time only):

   ```bash
   OPENAI_API_KEY=sk-...
   ```

   Get a key at https://platform.openai.com/api-keys. Never commit this file; it's already in `.gitignore`.

   Optional settings (the defaults are shown):

   ```bash
   OPENAI_MODEL=gpt-5-nano
   OPENAI_REASONING_EFFORT=low
   ```

   `OPENAI_REASONING_EFFORT` must be one of `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`, and not every model supports every value. Variables set in your shell override the values in `.env`. Restart the server after changing `.env`.

5. Start the development server:

   ```bash
   fastapi dev app/main.py
   ```

   The server reloads automatically when you save a file. Stop it with `Ctrl + C`.

6. Check that it works:

   - Health check: http://localhost:8000/health
   - Interactive API docs: http://localhost:8000/docs (try `POST /ask`)

   Each OpenAI call logs its model, token usage, and latency to the terminal. Questions and answers are never logged.

### Frontend

All frontend commands run from the `frontend/` directory. The backend must be running for the app to answer questions.

1. Make sure you're on Node.js 24:

   ```bash
   node --version
   ```

2. Install dependencies (first time, and whenever `package.json` changes):

   ```bash
   cd frontend
   npm install
   ```

3. Create a `.env` file in `frontend/` that tells the app where the backend is (first time only):

   ```bash
   VITE_API_URL=http://localhost:8000
   ```

   Restart the dev server after changing `.env`.

4. Start the development server:

   ```bash
   npm run dev
   ```

5. Open http://localhost:5173 and ask a question.

The backend only accepts browser requests from `http://localhost:5173` (CORS). If you run the frontend on a different port, update the allowed origins in `backend/app/main.py`.

## Design decisions

See [docs/decisions.md](docs/decisions.md).

## License

[MIT](LICENSE)
