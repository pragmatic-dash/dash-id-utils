from copy import copy
import json

from dash import ALL, Output, Input, State


__all__ = ["DashIDGenerator", "DashIDWrapper"]


class DashIDWrapper:
    def __init__(self, id):
        self.id = id

    def get_identifier(self):
        return self.id

    def get_output(self, property, allow_duplicate=True):
        return Output(self.get_identifier(), property, allow_duplicate=allow_duplicate)

    def get_input(self, property):
        return Input(self.get_identifier(), property)

    def get_state(self, property):
        return State(self.get_identifier(), property)
    
    def __str__(self):
        if isinstance(self.id, dict):
            return json.dumps(self.id, sort_keys=True, separators=(",", ":"))
        return str(self.id)


class DashIDGenerator:
    def __init__(
        self,
        page="default",
        type="default",
        name="default",
        id=None,
        extras=None,
    ):
        self.page = page
        self.type = type
        self.name = name
        self.id = id
        self.extra = extras

    def get_identifier(self, id=None):
        id = id or self.id
        identifier = copy(self.extra or {})
        identifier.update(
            {
                "page": self.page,
                "type": self.type,
                "name": self.name,
            }
        )
        if id is not None:
            identifier["id"] = id
        return identifier

    def get_pattern(self, pattern=ALL):
        identifier = self.get_identifier()
        identifier["id"] = pattern
        return identifier

    def get_output(self, property, pattern=None, allow_duplicate=True):
        if pattern:
            return Output(
                self.get_pattern(pattern), property, allow_duplicate=allow_duplicate
            )
        return Output(self.get_identifier(), property, allow_duplicate=allow_duplicate)

    def get_input(self, property, pattern=None):
        if pattern:
            return Input(self.get_pattern(pattern), property)
        return Input(self.get_identifier(), property)

    def get_state(self, property, pattern=None):
        if pattern:
            return State(self.get_pattern(pattern), property)
        return State(self.get_identifier(), property)

    def __str__(self):
        id_ = self.get_identifier()
        return json.dumps(id_, sort_keys=True, separators=(",", ":"))
