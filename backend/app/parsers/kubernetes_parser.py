import yaml


class KubernetesParser:

    def parse(self, filepath):

        resources = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                docs = list(yaml.safe_load_all(f))

            for doc in docs:

                if not doc:
                    continue

                metadata = doc.get("metadata", {})
                spec = doc.get("spec", {})

                resource = {
                    "kind": doc.get("kind"),
                    "name": metadata.get("name"),
                    "namespace": metadata.get("namespace", "default"),
                    "labels": metadata.get("labels", {}),
                    "file": filepath,
                }

                # Deployment / Pod
                template = spec.get("template", {})
                pod_spec = template.get("spec", {})

                containers = pod_spec.get("containers", [])

                images = []
                ports = []

                for container in containers:

                    if "image" in container:
                        images.append(container["image"])

                    for port in container.get("ports", []):
                        ports.append(port.get("containerPort"))

                resource["images"] = images
                resource["ports"] = ports

                resources.append(resource)

        except Exception:
            pass

        return resources