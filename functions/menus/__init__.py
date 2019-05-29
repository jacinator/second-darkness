from . import bases


class ActionMenu(bases.MainMenu):

    def __init__(self, object):
        actions = filter(lambda n: n.startswith("action_"), dir(object))
        choices = [getattr(object, action) for action in actions]
        super().__init__(choices)


class ObjectMenu(bases.MainMenu):

    def __init__(self, object_list, filter_func=None):
        choices = tuple(filter(filter_func, object_list))
        super().__init__(choices)


class NationActionMenu(ActionMenu):

    def __init__(self, nation):
        self.nation = nation
        super().__init__(nation)

    def choose(self):
        action = super().choose()
        return action(self.nation)


class RegionActionMenu(ActionMenu):

    def __init__(self, nation, region):
        self.nation = nation
        self.region = region
        super().__init__(region)

    def choose(self):
        action = super().choose()
        return action(self.region, self.nation)


class UnitObjectMenu(ObjectMenu):

    def __init__(self, nation, region):
        super().__init__(nation.army, lambda u: u.developed <= region.developed)
