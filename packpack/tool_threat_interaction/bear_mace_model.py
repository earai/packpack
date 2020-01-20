from pymc3.model import Model, Deterministic
import pymc3 as pm
from packpack.datamodels import Bear, Environment, Mace, EncounterResult
from typing import Callable
import theano.tensor as tt
import numpy as np


class BearMaceModel(object):

    def __init__(self,
                 make_environment: Callable[[], Environment],
                 make_mace: Callable[[], Mace],
                 make_bear: Callable[[Environment], Bear],
                 make_encounter_result: Callable[[Bear, Mace], EncounterResult]):
        self.make_environment = make_environment
        self.make_mace = make_mace
        self.make_bear = make_bear
        self.make_encounter_result = make_encounter_result
        self.bear = None
        self.environment = None
        self.mace = None
        self.encounter_result = None

    def build_model(self) -> Model:
        with Model() as model:
            self.bear = self.make_bear(self.make_environment())
            self.encounter_result = self.make_encounter_result(self.bear, self.make_mace())
        return model

    @classmethod
    def make_environment(cls):
        return Environment(latitude=pm.Uniform('latitude', -90., 90.))

    @classmethod
    def make_mace(cls):
        eye_sting = pm.Uniform('eye_sting', 0., 1.)
        nose_burn = pm.Deterministic('nose_burn', .5-eye_sting**2)
        return Mace(eye_sting=eye_sting, nose_burn= nose_burn)

    @classmethod
    def make_bear(cls, environment: Environment) -> Bear:
        latitude = environment.latitude
        deg_to_rad = np.pi/180.
        sight = Deterministic('sight', tt.sin(latitude*deg_to_rad)**2.)
        smell = Deterministic('smell', tt.cos(latitude*deg_to_rad)**2.)
        return Bear(sight=sight, smell=smell)

    @classmethod
    def crude_bear_mace_interaction(cls, bear: Bear, mace: Mace):
        stiffness=20.
        logit_p = stiffness*(mace.nose_burn+mace.eye_sting-bear.smell-bear.sight)
        survived = pm.Bernoulli('survived', logit_p=logit_p, observed=1.)
        return EncounterResult(survived=survived)

    @classmethod
    def fancy_bear_mace_interaction(cls, bear: Bear, mace: Mace):
        stiffness = 20.
        logit_p_nose = (mace.nose_burn-bear.smell)*stiffness
        logit_p_eyes = (mace.eye_sting-bear.sight)*stiffness
        logit_p = tt.min(tt.stack([logit_p_nose, logit_p_eyes]))

        survived = pm.Bernoulli('survived', logit_p=logit_p, observed=1.)
        return EncounterResult(survived=survived)
