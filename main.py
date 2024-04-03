from fastapi import FastAPI, HTTPException
from env import SETTINGS
import subprocess
from constants import STATER_TEST

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/tests")
async def run_tests():
    try:
        script_path = SETTINGS.TEST_SUITE_PATH
        subprocess.Popen(["sh", "-c", f"cd {script_path} && {STATER_TEST}"])
        return {"message": "tests started."}
    except Exception as e:
        raise HTTPException(500, detail=str(e))


@app.get("/container/status")
async def container_status():
    result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    return {"output": result.stdout, "error": result.stderr}
