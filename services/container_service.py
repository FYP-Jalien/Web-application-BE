import subprocess
from schemas.container_schema import ContainerInformationSchema, ContainerSchema


class ContainerService:
    @staticmethod
    def check_status():
        result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
        containers_details = []
        if result.stdout:
            lines = result.stdout.split("\n")
            for i in range(1, len(lines)):
                container_details = lines[i].strip().split('  ')
                container_details = [i.strip() for i in container_details if i != '']
                if not container_details:
                    continue

                formatted_container_details = ContainerInformationSchema(
                    container_name=container_details[0],
                    image=container_details[1],
                    uptime=container_details[3],
                    status=container_details[4]
                )

                containers_details.append(formatted_container_details)

        return ContainerSchema(
            container_information=containers_details,
            error=result.stderr
        )
