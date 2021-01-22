# import this.lxd.profile
import blueprint
import blueprint.common
import blueprint.modules
import logging
from pathlib import Path

log = logging.getLogger(__name__)


def apply(resources):
    for resource in resources:
        log.info(f"apply {resource.type} {resource.definition['name']}")
        resource.apply()

def destroy(resources):
    for resource in reversed(resources):
        log.info(f"destroy {resource.type} {resource.definition['name']}")
        resource.destroy()

def run(action="apply"):
    logging.basicConfig(level=logging.INFO)

    modules = blueprint.modules.load_all(Path("./blueprint_modules"))
    bp_module = blueprint.modules.load(Path("Blueprint"), exec_module=False)

    inject = {**blueprint.__exposed__, **modules}
    for name, value in inject.items():
        setattr(bp_module, name, value)
    bp_module.__spec__.loader.exec_module(bp_module)

    if action == "apply":
        if hasattr(bp_module, action):
            bp_module.apply()
        else:
            apply(bp_module.resources)

    if action == "destroy":
        if hasattr(bp_module, action):
            bp_module.destroy()
        else:
            destroy(bp_module.resources)
