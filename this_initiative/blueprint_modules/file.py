import blueprint.common
from blueprint.resource import Resource
import logging
import yaml
from pathlib import Path

log = logging.getLogger(__name__)

__type__ = "resource"

class file(Resource):
    def fetch_all(self):
        return {}


    def create(self):
        Path(self.definition['path']).write_text(self.definition['content'])


    def update(self):
        Path(self.definition['path']).write_text(self.definition['content'])


    def delete(self):
        Path(self.definition['path']).unlink(missing_ok=True)
