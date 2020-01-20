from pymc3.model import Model
from packpack.datamodels import Bear, Environment, Mace, EncounterResult
from typing import Callable


class BearMaceModel(object):

    def __init__(self,
                 environment: Environment,
                 mace: Mace,
                 make_bear: Callable[[Environment], Bear],
                 bear_mace_interaction: Callable[[Bear, Mace], EncounterResult]):
        self.environment = environment
        self.mace = mace
        self.make_bear = make_bear
        self.bear_mace_interaction = bear_mace_interaction

    def build_model(self) -> Model:
        pass