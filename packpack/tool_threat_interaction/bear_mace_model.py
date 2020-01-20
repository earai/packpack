from pymc3.model import Model, Deterministic
import pymc3 as pm
from packpack.datamodels import Bear, Environment, Mace, EncounterResult
from typing import Callable
import theano.tensor as tt

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
        self.bear = None
        self.encounter_result = None

    def build_model(self) -> Model:
        with Model() as model:
            self.bear = self.make_bear(self.environment)
            self.encounter_result = self.bear_mace_interaction(self.bear, self.mace)
        return model

    @classmethod
    def make_bear(cls, environment: Environment) -> Bear:
        latitude = environment.latitude
        sight = Deterministic('sight', latitude**2.)
        smell = Deterministic('smell', 1./(latitude**2.+1.))
        return Bear(sight=sight, smell=smell)

    @classmethod
    def crude_bear_mace_interaction(cls, bear: Bear, mace: Mace):
        logit_p = mace.nose_burn+mace.eye_sting-bear.smell-bear.sight
        encounter_result = pm.Bernoulli('encounter_result', logit_p=logit_p, observed=1.)
        return EncounterResult(encounter_result=encounter_result)

    @classmethod
    def fancy_bear_mace_interaction(cls, bear: Bear, mace: Mace):
        logit_p_nose = mace.nose_burn-bear.smell
        logit_p_eyes = mace.eye_sting-bear.sight
        logit_p = tt.max(logit_p_eyes, logit_p_nose)
        encounter_result = pm.Bernoulli('encounter_result', logit_p=logit_p, observed=1.)
        return EncounterResult(encounter_result=encounter_result)
