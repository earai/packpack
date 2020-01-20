import pymc3 as pm
from matplotlib import pyplot as plt
import numpy as np
from pandas.plotting import scatter_matrix
import pandas as pd

class BearMaceModelRunner(object):

    def __init__(self, bear_mace_model):
        self.bear_mace_model = bear_mace_model
        self.prior_samples = None
        self.trace = None

    def run_model(self, n_samples, n_tuning_samples):
        m = self.bear_mace_model.build_model()
        with m:
            self.prior_samples = pm.sample_prior_predictive(10000, m)
            self.prior_samples_as_df = pd.DataFrame(self.prior_samples)
            self.trace = pm.sample(n_samples, tune=n_tuning_samples)
            self.trace_as_df = pm.trace_to_dataframe(self.trace)
        return self.trace

    def plot_marginal(self, variable_name):
        var_pri = self.prior_samples[variable_name]
        var_post = self.trace_as_df[variable_name]

        def bins(x_prior, x_posterior, n=200):
            return np.linspace(min(np.min(x_prior), np.min(x_posterior)), max(np.max(x_prior), np.max(x_posterior)), 200)

        these_bins = bins(var_pri, var_post)

        plt.hist(var_pri, these_bins, alpha=.4, label='prior', density=True)
        plt.hist(var_post, these_bins, alpha=.4, label='posterior', density=True)
        plt.xlabel(variable_name)
        plt.legend()


    def visualize_trace(self, include_scatters=False):
        df = self.trace_as_df
        bear = self.bear_mace_model.bear
        mace = self.bear_mace_model.mace
        environment = self.bear_mace_model.environment
        encounter_result = self.bear_mace_model.encounter_result

        plt.figure(figsize=(12,12))
        keys = set(df.columns).intersection(set(self.prior_samples.keys()))
        for i,k in enumerate(keys):
            plt.subplot(2, 3, i+1)
            self.plot_marginal(k)

        if include_scatters:
            scatter_matrix(self.trace_as_df, figsize=(12,12), alpha=.05)
            scatter_matrix(self.prior_samples_as_df[list(keys)], figsize=(12, 12), alpha=.05)


