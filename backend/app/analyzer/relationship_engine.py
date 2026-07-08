class RelationshipEngine:

    def build(self, repository):

        relationships = []

        deployments = repository.get("kubernetes", [])
        compose = repository.get("compose", [])
        docker = repository.get("docker", [])
        terraform = repository.get("terraform", [])
        nginx = repository.get("nginx", [])

        # -----------------------------
        # Deployment -> Docker Image
        # -----------------------------
        for deployment in deployments:

            if deployment.get("kind") != "Deployment":
                continue

            for image in deployment.get("images", []):

                relationships.append({
                    "source": deployment["name"],
                    "target": image,
                    "type": "uses_docker_image"
                })

        # -----------------------------
        # Deployment -> Port
        # -----------------------------
        for deployment in deployments:

            for port in deployment.get("ports", []):

                relationships.append({
                    "source": deployment["name"],
                    "target": str(port),
                    "type": "exposes_port"
                })

        # -----------------------------
        # Docker Compose Services
        # -----------------------------
        for service in compose:

            for dependency in service.get("depends_on", []):

                relationships.append({
                    "source": service["service"],
                    "target": dependency,
                    "type": "depends_on"
                })

        # -----------------------------
        # Terraform Resources
        # -----------------------------
        for resource in terraform:

            relationships.append({
                "source": resource["type"],
                "target": resource["name"],
                "type": "creates"
            })

        # -----------------------------
        # Nginx -> Backend
        # -----------------------------
        for server in nginx:

            for proxy in server.get("proxy_pass", []):

                relationships.append({
                    "source": "Nginx",
                    "target": proxy,
                    "type": "routes_to"
                })

        return relationships