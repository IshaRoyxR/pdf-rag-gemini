import os
import re


class SecurityAnalyzer:

    def analyze_repository(self, repo_path):

        issues = []

        for root, dirs, files in os.walk(repo_path):

            for file in files:

                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf-8") as f:
                        text = f.read()

                    issues.extend(
                        self.scan_file(path, text)
                    )

                except Exception:
                    pass

        return issues

    def scan_file(self, filepath, text):

        issues = []

        # Hardcoded passwords
        password_patterns = [
            r"password\s*=",
            r"passwd\s*=",
            r"secret\s*=",
            r"token\s*=",
            r"apikey",
            r"api_key",
        ]

        for pattern in password_patterns:

            if re.search(pattern, text, re.IGNORECASE):

                issues.append(
                    {
                        "severity": "High",
                        "issue": "Possible hardcoded credential",
                        "file": filepath,
                        "recommendation":
                            "Move secrets to Kubernetes Secret or .env"
                    }
                )

        # Docker latest image
        if "FROM" in text and ":latest" in text:

            issues.append(
                {
                    "severity": "Medium",
                    "issue": "Docker image uses latest tag",
                    "file": filepath,
                    "recommendation":
                        "Pin a specific image version"
                }
            )

        # Root user
        if re.search(r"USER\s+root", text):

            issues.append(
                {
                    "severity": "High",
                    "issue": "Container runs as root",
                    "file": filepath,
                    "recommendation":
                        "Run container as non-root user"
                }
            )

        # Wildcard IAM
        if '"*"' in text:

            issues.append(
                {
                    "severity": "Critical",
                    "issue": "Wildcard IAM permission",
                    "file": filepath,
                    "recommendation":
                        "Grant least privilege"
                }
            )

        # Public S3 bucket
        if "public-read" in text.lower():

            issues.append(
                {
                    "severity": "Critical",
                    "issue": "Public S3 bucket detected",
                    "file": filepath,
                    "recommendation":
                        "Disable public bucket access"
                }
            )

        # Missing HTTPS
        if "listen 80;" in text:

            issues.append(
                {
                    "severity": "Medium",
                    "issue": "HTTP only configuration",
                    "file": filepath,
                    "recommendation":
                        "Enable HTTPS"
                }
            )

        return issues