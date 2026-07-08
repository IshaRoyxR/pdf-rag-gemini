import os

from app.parsers.kubernetes_parser import KubernetesParser
from app.parsers.terraform_parser import TerraformParser
from app.parsers.docker_parser import DockerParser
from app.parsers.compose_parser import ComposeParser
from app.parsers.nginx_parser import NginxParser
from app.parsers.cicd_parser import CICDParser


class RepositoryParser:

    def __init__(self):

        self.kubernetes = KubernetesParser()
        self.terraform = TerraformParser()
        self.docker = DockerParser()
        self.compose = ComposeParser()
        self.nginx = NginxParser()
        self.cicd = CICDParser()

    def parse_repository(self, repo_path):

        repository = {
            "kubernetes": [],
            "terraform": [],
            "docker": [],
            "compose": [],
            "nginx": [],
            "cicd": []
        }

        for root, dirs, files in os.walk(repo_path):

            for file in files:

                filepath = os.path.join(root, file)

                try:

                    # Kubernetes YAML
                    if file.endswith((".yaml", ".yml")):
                        repository["kubernetes"].extend(
                            self.kubernetes.parse(filepath)
                        )

                        # CI/CD YAML
                        if file in (
                            "ci.yml",
                            ".gitlab-ci.yml",
                            "github-actions.yml",
                            "workflow.yml",
                        ):
                            repository["cicd"].extend(
                                self.cicd.parse(filepath)
                            )

                    # Terraform
                    elif file.endswith(".tf"):
                        repository["terraform"].extend(
                            self.terraform.parse(filepath)
                        )

                    # Dockerfile
                    elif file == "Dockerfile":
                        repository["docker"].append(
                            self.docker.parse(filepath)
                        )

                    # Docker Compose
                    elif file in (
                        "docker-compose.yml",
                        "docker-compose.yaml",
                        "compose.yml",
                        "compose.yaml",
                    ):
                        repository["compose"].extend(
                            self.compose.parse(filepath)
                        )

                    # Nginx
                    elif file.endswith(".conf"):
                        repository["nginx"].append(
                            self.nginx.parse(filepath)
                        )

                except Exception:
                    pass

        return repository