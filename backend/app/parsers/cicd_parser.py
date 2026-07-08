import yaml


class CICDParser:

    def parse(self, filepath):

        pipelines = []

        try:

            with open(filepath, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            if not data:
                return pipelines

            # GitHub Actions
            if "jobs" in data:

                for job_name, job in data["jobs"].items():

                    pipelines.append({
                        "platform": "GitHub Actions",
                        "job": job_name,
                        "runs_on": job.get("runs-on"),
                        "steps": len(job.get("steps", [])),
                        "file": filepath,
                    })

            # GitLab CI
            elif "stages" in data:

                pipelines.append({
                    "platform": "GitLab CI",
                    "stages": data.get("stages", []),
                    "file": filepath,
                })

        except Exception:
            pass

        return pipelines