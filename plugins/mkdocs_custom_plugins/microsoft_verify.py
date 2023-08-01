import os
import json
import mkdocs.plugins
import mkdocs.config.base
import mkdocs.config.config_options
from mkdocs.config.defaults import MkDocsConfig


class VerifyConfig(mkdocs.config.base.Config):
    id = mkdocs.config.config_options.Type(str, default="")


class MicrosoftVerifyPlugin(mkdocs.plugins.BasePlugin[VerifyConfig]):
    def on_post_build(self, *, config: MkDocsConfig) -> None:
        if not self.config["id"]:
            return

        os.mkdir(f"{config.site_dir}/.well-known")

        payload = {"associatedApplications": [{"applicationId": self.config["id"]}]}

        with open(
            f"{config.site_dir}/.well-known/microsoft-identity-association.json", "w"
        ) as f:
            f.write(json.dumps(payload))
