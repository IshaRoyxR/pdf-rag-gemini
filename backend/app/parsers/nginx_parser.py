import re


class NginxParser:

    def parse(self, filepath):

        config = {
            "listen": [],
            "server_name": [],
            "proxy_pass": [],
            "upstreams": [],
            "ssl": False,
            "file": filepath
        }

        try:

            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            # Listen ports
            config["listen"] = re.findall(
                r"listen\s+([^;]+);",
                text
            )

            # Server names
            config["server_name"] = re.findall(
                r"server_name\s+([^;]+);",
                text
            )

            # Proxy pass
            config["proxy_pass"] = re.findall(
                r"proxy_pass\s+([^;]+);",
                text
            )

            # Upstream blocks
            config["upstreams"] = re.findall(
                r"upstream\s+([^{\s]+)",
                text
            )

            # SSL
            if (
                "ssl_certificate" in text
                or "listen 443" in text
            ):
                config["ssl"] = True

        except Exception:
            pass

        return config