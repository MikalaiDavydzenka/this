import importlib
import importlib.util
import importlib.machinery
import sys
from pathlib import Path
import yaml

def load(module_path, exec_module=True):
    # spec = importlib.util.spec_from_file_location(module_name, module_path)
    spec = importlib.util.spec_from_loader(
        name=module_path.stem,
        loader=importlib.machinery.SourceFileLoader(
            fullname=module_path.stem,
            path=str(module_path),
        )
    )
    module = importlib.util.module_from_spec(spec)
    if exec_module:
        spec.loader.exec_module(module)
    return module


def load_all(dir_path, exec_module=True):
    modules = {}
    for module_path in dir_path.glob("*.py"):
        module = load(module_path, exec_module)
        modules[module.__name__] = module
    return modules


def ensure(profile, existing_profiles=None):
    if not existing_profiles:
        existing_profiles = fetch_all()

    if profile["name"] not in existing_profiles:
        create(profile)

    update(profile)



def ensure_all(profiles):
    existing_profiles = fetch_all()

    for profile in profiles:
        ensure(
            profile,
            existing_profiles,
        )

def fetch(name):
    return fetchall()[name]