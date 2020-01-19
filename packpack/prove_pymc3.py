import pymc3 as pm
import numpy as np


def build_proof_model():
    np.seterr(invalid='raise')

    data = np.random.normal(size=(2, 20))

    with pm.Model() as model:
        x = pm.Normal('x', mu=.5, sigma=2., shape=(2, 1))
        z = pm.Beta('z', alpha=10, beta=5.5)
        d = pm.Normal('data', mu=x, sigma=.75, observed=data)


class PymcShieldSwordInteractor(object):
    def __init__(self, shield, sword):
        pass

    def interact(self):
        pass

class PyroShieldSwordInteractor(object):
    pass

class Shield(object):
    def __init__(self, thickness):
        self.thickness = thickness

    def defend(self, sword):
        logit_p = self._its_complicated(sword.sharpness)
        p_survive = pm.Bernoulli(logit_p=logit_p)
        return p_survive

    def _its_complicated(self, sharpness):
        pass


def build_dumb_packer_model(backpack, tool, threat):
    with pm.Model() as model:
        n_items = pm.Geometric(.5, name='n_items')
        item_size = pm.Beta(10, 10, name='item_size')
        pack_size = pm.Deterministic('pack_size', 1.0)

        # dumbest packing function
        occupied_volume = n_items * item_size

        stiffness = pm.Deterministic('pack_stiffness', 10.0)
        fits = pm.Bernoulli(logit_p=stiffness*(pack_size - occupied_volume), observed=1.0)

    return model