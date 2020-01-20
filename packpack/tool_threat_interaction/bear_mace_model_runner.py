import pymc3 as pm

class BearMaceModelRunner(object):

    def __init__(self, bear_mace_model):
        self.bear_mace_model = bear_mace_model

    def run_model(self, n_samples, n_tuning_samples):
        m = self.bear_mace_model
        with m:
            trace = pm.sample(n_samples, tune=n_tuning_samples)
        print(trace.report.ok)



