import blueprint.common
import logging
import yaml

log = logging.getLogger(__name__)

__type__ = "resource"

def fetch_all():
    lxc_profiles = blueprint.common.cmd(
        "lxc profile list --format yaml",
        yaml_output=True,
    )

    return {
        profile["name"]:profile
        for profile in lxc_profiles
    }


def create(profile):
    blueprint.common.cmd(f"lxc profile create {profile['name']}")


def update(profile):
    blueprint.common.cmd(
        f"lxc profile edit {profile['name']}",
        input=yaml.dump(profile),
    )

def delete(definition):
    blueprint.common.cmd(f"lxc profile delete {definition['name']}")
