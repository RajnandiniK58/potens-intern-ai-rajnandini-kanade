from fastapi import FastAPI


app = FastAPI(
    title="Telecom Triage Agent",
    description="AI Agent for Telecom Support Ticket Triage",
    version="1.0.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Telecom Triage Agent is running!"}
