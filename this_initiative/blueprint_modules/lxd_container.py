import blueprint.common
import logging
import yaml

log = logging.getLogger(__name__)

__type__ = "resource"

def fetch_all():
    resources = blueprint.common.cmd(
        "lxc list --format yaml",
        yaml_output=True,
    )

    return {
        resource["name"]:resource
        for resource in resources
    }


def create(definition):
    os = definition.get("os", "ubuntu:20.04")
    profiles = definition.get("profiles", [])
    profiles_arg = ""
    for profile_name in profiles:
        profiles_arg += f" --profile {profile_name}"
    target_node = definition.get("target")
    target_arg = ""
    if target_node:
        target_arg = f"--target {target_node}"
    blueprint.common.cmd(
        f"lxc launch {os} {definition['name']} {target_arg} {profiles_arg}"
    )


def update(definition):
    # not implemented
    pass


def delete(definition):
    blueprint.common.cmd(f"lxc stop {definition['name']}")
    blueprint.common.cmd(f"lxc delete {definition['name']}")
