import numpy as np
import pymc3 as pm
import theano.tensor as tt
from pymc3.model import Model


def build_model() -> Model:
    n_patient = 1
    n_sick = 1
    n_vaccines = 1
    n_well = int(n_patient - n_sick)
    p_fp = .01
    p_fn = .35
    p_precede_sick = np.full(n_sick+1, 1. / (n_sick + 1.))
    with Model() as model:
        n_i = pm.Multinomial("well", n_well, p_precede_sick, shape=(n_sick+1,))
        x_i = pm.Binomial("vaccines_wasted", n_i, p_fp, shape=(n_sick+1,))
        y_j = pm.Bernoulli("failed_to_vaccinate", p_fn, shape=(n_sick+1,))
        did_not_use_too_much_vaccine = pm.Deterministic("did_not_use_too_much_vaccine", tt.sum(x_i[:-1]) <= n_vaccines - n_sick)
        vaccinated_every_sickie = pm.Deterministic('vaccinated_every_sickie', tt.prod(1. - y_j[:-1]))
        live = pm.Deterministic(name="alive", var=did_not_use_too_much_vaccine * vaccinated_every_sickie)
    return model


def main():
    """
    n_sick placed at random
    i_0     is the index of the first sick patient eq if i=3, the number of nonsick patients preceding the first
            sick patient is i_0
    n_vaccines expended before we get to the first sick person is:
                x_0 ~ Binomial(i_0, P_fp) vaccines spent on non sick patients before encountering first sick patient
                x_1 ~ Binomial(i_1 - i_0, P_fp) is the number of vaccines spent between the first sick and the second sick
                etc until a sick patient has got us all sick or we vaccinated all the sick patients.

    y_j ~ Bernoulli(P_fn) - if we failed to vaccinate the jth sick patient

    * (sum_j(x_j) <= n_vaccines-n_sick)*product_j(1-y_j)  - if this is 1 then we live, 0 we die
    * is a deterministic function of the three random variables x_i, y_j

    Multinomial(n_patients-n_sick, (1/n_sick)*(ones_likes(n_patients)+1))
    """
    # with Model() as m:
    #     y_j = pm.Normal("y", .1, .1, shape=1)
    #     prod_y = pm.Normal('prod_y', 1.0-y_j , 1.0, shape=1)
    #     # prod_y = pm.Deterministic('prod_y', tt.prod(tt.concatenate([tt.ones((1,)), tt.reshape(y_j, (1,))], axis=-1), keepdims=True))
    # yy = pm.sampling.sample_prior_predictive(10, model=m)
    #
    # print(yy)
    model = build_model()
    x = pm.sampling.sample_prior_predictive(samples=5000, model=model)
    print(x.keys())
    print(x)
    print(np.mean(x['alive']))


if __name__ == '__main__':
    main()