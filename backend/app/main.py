from fastapi import FastAPI

app = FastAPI(title="Citewise")


@app.get("/health")
def health():
    return {"status": "ok"}
