import os
import yaml
import re


class InfrastructureAnalyzer:

    def __init__(self):
        self.relationships = []

    def analyze_repository(self, repo_path):

        for root, dirs, files in os.walk(repo_path):

            for file in files:

                path = os.path.join(root, file)

                if file.endswith((".yaml", ".yml")):
                    self._analyze_yaml(path)

                elif file == "Dockerfile":
                    self._analyze_dockerfile(path)

                elif file.endswith(".tf"):
                    self._analyze_terraform(path)

        return self.relationships

    def _analyze_yaml(self, filepath):

        try:

            with open(filepath, "r", encoding="utf-8") as f:

                docs = list(yaml.safe_load_all(f))

            for doc in docs:

                if not doc:
                    continue

                kind = doc.get("kind")

                name = (
                    doc.get("metadata", {})
                    .get("name", "Unknown")
                )

                self.relationships.append(
                    {
                        "type": "kubernetes",
                        "kind": kind,
                        "name": name,
                        "file": filepath,
                    }
                )

        except Exception:
            pass

    def _analyze_dockerfile(self, filepath):

        try:

            with open(filepath, "r") as f:

                text = f.read()

            match = re.search(r"FROM (.+)", text)

            if match:

                self.relationships.append(
                    {
                        "type": "docker",
                        "image": match.group(1),
                        "file": filepath,
                    }
                )

        except Exception:
            pass

    def _analyze_terraform(self, filepath):

        try:

            with open(filepath, "r") as f:

                text = f.read()

            resources = re.findall(
                r'resource\\s+"([^"]+)"\\s+"([^"]+)"',
                text,
            )

            for resource in resources:

                self.relationships.append(
                    {
                        "type": "terraform",
                        "resource": resource[0],
                        "name": resource[1],
                        "file": filepath,
                    }
                )

        except Exception:
            pass