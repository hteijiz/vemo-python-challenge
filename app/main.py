from fastapi import FastAPI, HTTPException
from services import read_logs

app = FastAPI()

@app.get("/logs", response_model=list[str])
def get_logs(filter: str | None):
    """
    Endpoint that returns a JSON with all lines that contains a specific filter (optional).
    """
    try:
        return read_logs(filter)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

