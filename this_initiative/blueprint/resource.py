from dataclasses import dataclass
import types

@dataclass
class Resource:
    type: types.ModuleType
    definition: dict

    def apply(self, existing_resoureces=None):
        # def ensure(profile, existing_profiles=None):
        if not existing_resoureces:
            existing_resoureces = self.type.fetch_all()

        if self.definition["name"] not in existing_resoureces:
            self.type.create(self.definition)

        self.type.update(self.definition)

    def destroy(self):
        self.type.delete(self.definition)