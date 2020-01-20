import pymc3 as pm
from matplotlib import pyplot as plt
import numpy as np

class BearMaceModelRunner(object):

    def __init__(self, bear_mace_model):
        self.bear_mace_model = bear_mace_model
        self.prior_samples = None
        self.trace = None

    def run_model(self, n_samples, n_tuning_samples):
        m = self.bear_mace_model.build_model()
        with m:
            self.prior_samples = pm.sample_prior_predictive(10000, m)
            self.trace = pm.sample(n_samples, tune=n_tuning_samples)
        return self.trace

    def visualize_trace(self):
        df = pm.trace_to_dataframe(self.trace)
        bear = self.bear_mace_model.bear
        mace = self.bear_mace_model.mace
        environment = self.bear_mace_model.environment
        encounter_result = self.bear_mace_model.encounter_result

        bear_sight_pri = self.prior_samples['sight']
        bear_sight_post = df.sight

        def bins(x_prior, x_posterior, n=200):
            return np.linspace(min(np.min(x_prior), np.min(x_posterior)), max(np.max(x_prior), np.max(x_posterior)), 200)

        bear_bins = bins(bear_sight_pri, bear_sight_post)

        plt.figure(figsize=(12, 12))

        plt.subplot(2, 2, 1)
        plt.hist(bear_sight_pri, bear_bins, alpha=.4, label='prior', density=True)
        plt.hist(bear_sight_post, bear_bins, alpha=.4, label='posterior', density=True)
        plt.xlabel('bear sight')
        plt.legend()


        # plt.subplot(2, 2, 3)
        # #plt.plot(jitter(n_items_pri), item_size_pri, 'k.', alpha=.04, label='prior')
        # plt.xlabel('n_items (jittered for display purposes)')
        # plt.ylabel('item_size')
        # plt.legend()
        #
        # plt.subplot(2, 2, 4)
        # #plt.plot(jitter(n_items_post), item_size_post, 'k.', alpha=.04, label='posterior')
        # plt.xlabel('n_items ')
        # plt.ylabel('item_size')
        # plt.legend()

        # plt.plot()
        # scatter_matrix(df, figsize=(12, 12))
        plt.show()
        print('stop')

