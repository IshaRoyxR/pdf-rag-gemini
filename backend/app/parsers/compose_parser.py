import yaml


class ComposeParser:

    def parse(self, filepath):

        services = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                compose = yaml.safe_load(f)

            if not compose:
                return services

            for service_name, service in compose.get("services", {}).items():

                services.append({
                    "service": service_name,
                    "image": service.get("image"),
                    "build": service.get("build"),
                    "ports": service.get("ports", []),
                    "volumes": service.get("volumes", []),
                    "environment": service.get("environment", []),
                    "depends_on": service.get("depends_on", []),
                    "networks": service.get("networks", []),
                    "file": filepath
                })

        except Exception:
            pass

        return services