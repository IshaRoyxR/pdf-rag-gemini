import re


class DockerParser:

    def parse(self, filepath):

        docker_info = {
            "base_image": None,
            "user": None,
            "cmd": None,
            "entrypoint": None,
            "expose_ports": [],
            "environment": [],
            "file": filepath
        }

        try:

            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            # Base Image
            match = re.search(r"FROM\s+(.+)", text)
            if match:
                docker_info["base_image"] = match.group(1).strip()

            # USER
            match = re.search(r"USER\s+(.+)", text)
            if match:
                docker_info["user"] = match.group(1).strip()

            # CMD
            match = re.search(r"CMD\s+(.+)", text)
            if match:
                docker_info["cmd"] = match.group(1).strip()

            # ENTRYPOINT
            match = re.search(r"ENTRYPOINT\s+(.+)", text)
            if match:
                docker_info["entrypoint"] = match.group(1).strip()

            # EXPOSE
            ports = re.findall(r"EXPOSE\s+(\d+)", text)
            docker_info["expose_ports"] = ports

            # ENV
            envs = re.findall(r"ENV\s+(.+)", text)
            docker_info["environment"] = envs

        except Exception:
            pass

        return docker_info