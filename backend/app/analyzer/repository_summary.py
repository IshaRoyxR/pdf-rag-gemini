class RepositorySummary:

    def generate(self, repository):

        summary = []

        # Kubernetes
        k8s = repository.get("kubernetes", [])

        deployments = [
            r["name"]
            for r in k8s
            if r.get("kind") == "Deployment"
        ]

        services = [
            r["name"]
            for r in k8s
            if r.get("kind") == "Service"
        ]

        ingresses = [
            r["name"]
            for r in k8s
            if r.get("kind") == "Ingress"
        ]

        if deployments:
            summary.append(
                f"Deployments: {', '.join(deployments)}"
            )

        if services:
            summary.append(
                f"Services: {', '.join(services)}"
            )

        if ingresses:
            summary.append(
                f"Ingresses: {', '.join(ingresses)}"
            )

        # Docker
        docker = repository.get("docker", [])

        for image in docker:

            if image.get("base_image"):

                summary.append(
                    f"Docker Base Image: {image['base_image']}"
                )

        # Docker Compose
        compose = repository.get("compose", [])

        if compose:

            summary.append(
                f"Docker Compose Services: {len(compose)}"
            )

        # Terraform
        terraform = repository.get("terraform", [])

        if terraform:

            summary.append(
                f"Terraform Resources: {len(terraform)}"
            )

        # Nginx
        nginx = repository.get("nginx", [])

        if nginx:

            summary.append(
                "Nginx configuration detected"
            )

        return "\n".join(summary)