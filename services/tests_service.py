from fastapi import HTTPException
from env import SETTINGS
import subprocess
from constants import STATER_TEST
from schemas.testsuite_schemas import TestSummarySchema


class TestService:

    @staticmethod
    def start_tests():
        try:
            script_path = SETTINGS.TEST_SUITE_PATH
            process = subprocess.Popen(["sh", "-c", f"cd {script_path} && {STATER_TEST} --csv"],
                                       stderr=subprocess.PIPE)

            pid = process.pid  # Get PID from the process object

            return {"message": "test suite started", "pid": pid}

        except Exception as e:
            raise HTTPException(500, detail=str(e))

    @staticmethod
    def stop_tests(pid: int):
        try:
            subprocess.Popen(["sh", "-c", f"kill {pid}"])
        except Exception as e:
            raise HTTPException(500, detail=str(e))

    @staticmethod
    def read_test_summary():

        try:
            data = []
            with open(f"{SETTINGS.TEST_SUITE_PATH}/files/out.csv", "r") as file:
                # Read all lines and iterate over each line
                for line in file.readlines():
                    line = line.replace('"','')
                    row = line.split(",")
                    if len(row) >= 5:
                        test_summary = TestSummarySchema(id=row[0], name=row[1], status=row[2], level=row[3],
                                                         message=row[4])
                        data.append(test_summary)  # Append each row to the data list

            return data[1:]

        except FileNotFoundError:
            # Handle file not found case
            return {"error": "Test summary file not found."}

        except Exception as e:
            # Handle other potential errors
            raise HTTPException(500, detail=str(e))
