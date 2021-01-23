import blueprint.common
from blueprint.resource import Resource
import logging
import yaml

log = logging.getLogger(__name__)


class profile(Resource):
    def fetch_all(self):
        lxc_profiles = blueprint.common.cmd(
            "lxc profile list --format yaml",
            yaml_output=True,
        )

        return {
            profile["name"]:profile
            for profile in lxc_profiles
        }

    def read(self):
        self.fetch_all()[self.definition["name"]]

    def create(self):
        blueprint.common.cmd(f"lxc profile create {self.definition['name']}")


    def update(self):
        blueprint.common.cmd(
            f"lxc profile edit {self.definition['name']}",
            input=yaml.dump(self.definition),
        )

    def delete(self):
        blueprint.common.cmd(f"lxc profile delete {self.definition['name']}")


class container(Resource):
    def fetch_all(self):
        resources = blueprint.common.cmd(
            "lxc list --format yaml",
            yaml_output=True,
        )

        return {
            resource["name"]:resource
            for resource in resources
        }


    def read(self):
        self.fetch_all()[self.definition["name"]]


    def create(self):
        os = self.definition.get("os", "ubuntu:20.04")
        profiles = self.definition.get("profiles", [])
        profiles_arg = ""
        for profile_name in profiles:
            profiles_arg += f" --profile {profile_name}"
        target_node = self.definition.get("target")
        target_arg = ""
        if target_node:
            target_arg = f"--target {target_node}"
        blueprint.common.cmd(
            f"lxc launch {os} {self.definition['name']} {target_arg} {profiles_arg}"
        )


    def update(self):
        # not implemented
        pass


    def delete(self):
        blueprint.common.cmd(f"lxc stop {self.definition['name']}")
        blueprint.common.cmd(f"lxc delete {self.definition['name']}")
