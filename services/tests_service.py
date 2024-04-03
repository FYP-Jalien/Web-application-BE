from fastapi import HTTPException
from env import SETTINGS
import subprocess
from constants import STATER_TEST


class TestService:

    def start_tests(self):
        try:
            script_path = SETTINGS.TEST_SUITE_PATH
            subprocess.Popen(["sh", "-c", f"cd {script_path} && {STATER_TEST}"])
            return {"message": "tests started."}
        except Exception as e:
            raise HTTPException(500, detail=str(e))
