import this.common
import logging
import yaml

log = logging.getLogger(__name__)


def fetch_all():
    lxc_profiles = this.common.cmd(
        "lxc profile list --format yaml",
        yaml_output=True,
    )

    return {
        profile["name"]:profile
        for profile in lxc_profiles
    }


def fetch(name):
    return fetchall()[name]


def create(profile):
    this.common.cmd(f"lxc profile create {profile['name']}")


def update(profile):
    this.common.cmd(
        f"lxc profile edit {profile['name']}",
        input=profile,
    )


def ensure(profile, existing_profiles=None):
    if not existing_profiles:
        existing_profiles = fetchall()

    if profile["name"] not in existing_profiles:
        create(profile["name"])

    update(profile)



def ensure_all(profiles):
    existing_profiles = fetchall()

    for profile in profiles:
        ensure(
            profile,
            existing_profiles,
        )
