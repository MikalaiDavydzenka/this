from dataclasses import dataclass
import logging

log = logging.getLogger(__name__)

@dataclass
class Resource:
    definition: dict

    def apply(self, existing_resoureces=None):
        log.info(f"apply {self}")
        # def ensure(profile, existing_profiles=None):
        if not existing_resoureces:
            existing_resoureces = self.fetch_all()

        if self.definition["name"] not in existing_resoureces:
            self.create()

        self.update()

    @property
    def state(self):
        return self.read()

    def destroy(self):
        log.info(f"destroy {self}")
        self.delete()

    def __str__(self):
        return f"<{self.__class__.__module__}.{self.__class__.__name__} {self.definition['name']}>"
