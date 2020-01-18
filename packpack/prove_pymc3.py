import pymc3 as pm

import pymc3 as pm
import numpy as np


def build_proof_model():
    np.seterr(invalid='raise')

    data = np.random.normal(size=(2, 20))

    with pm.Model() as model:
        x = pm.Normal('x', mu=.5, sigma=2., shape=(2, 1))
        z = pm.Beta('z', alpha=10, beta=5.5)
        d = pm.Normal('data', mu=x, sigma=.75, observed=data)

    return model