from config import LOGS_FILENAME
from pathlib import Path

LOG_FILE = Path(LOGS_FILENAME)

def read_logs(filter: str | None) -> list[str]:
    """
    Reads all lines from specific file. Aplies a filter (optional).
    """
    # Check if exists
    if not LOG_FILE.exists():
        raise FileNotFoundError("Nothing to process or file does'n exist")

    # Ge all data from file
    lines = []
    with LOG_FILE.open(encoding="utf-8") as f:
        lines = [ln.rstrip('\n') for ln in f]

    # Filter data
    if filter:
        lines = [ln for ln in lines if filter in ln]

    return lines
