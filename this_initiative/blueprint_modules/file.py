import blueprint.common
import logging
import yaml
from pathlib import Path

log = logging.getLogger(__name__)

__type__ = "resource"

def fetch_all():
    return {}


def create(definition):
    Path(definition['path']).write_text(definition['content'])


def update(definition):
    Path(definition['path']).write_text(definition['content'])


def delete(definition):
    Path(definition['path']).unlink(missing_ok=True)
