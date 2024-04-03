import subprocess


class ContainerService:
    @staticmethod
    def check_status():
        result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
        return result.stdout, result.stderr
