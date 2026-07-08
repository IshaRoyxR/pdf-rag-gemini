import re


class TerraformParser:

    def parse(self, filepath):

        resources = []

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            matches = re.findall(
                r'resource\s+"([^"]+)"\s+"([^"]+)"',
                text
            )

            for resource_type, resource_name in matches:

                resources.append({
                    "type": resource_type,
                    "name": resource_name,
                    "file": filepath
                })

        except Exception:
            pass

        return resources