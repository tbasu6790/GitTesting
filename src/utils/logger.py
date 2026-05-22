import datetime

def log(level, message):
    ts = datetime.datetime.now().isoformat()
    print(f"[{ts}] [{level.upper()}] {message}")
