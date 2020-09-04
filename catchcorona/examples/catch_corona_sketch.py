from packpack.tool_threat_interaction.bear_mace_model import BearMaceModel
from packpack.tool_threat_interaction.bear_mace_model_runner import BearMaceModelRunner
from matplotlib import pyplot as plt


def build_model(self) -> Model:
        with Model() as model:
            self.bear = self.make_bear(self.make_environment())
            self.encounter_result = self.make_encounter_result(self.bear, self.make_mace())
        return model

def main():
    """
    n_sick placed at random
    i_0     is the index of the first sick patient eq if i=3, the number of nonsick patients precending the first
            sick patient is i_0
    n_vaccines expended before we get to the first sick person is:
                x_0 ~ Binomial(i_0, P_fp) vaccines spent on non sick patients before encountering first sick patient
                x_1 ~ Binomial(i_1 - i_0, P_fp) is the number of vaccines spent between the first sick and the second sick
                etc until a sick patient has got us all sick or we vaccinated all the sick patients.

    y_j ~ Bernoulli(P_fn) - if we failed to vaccinate the jth sick patient

    (sum_j(x_j) <= n_vaccines-n_sick)*product_j(1-y_j)  - if this is 1 then we live, 0 we die
    """
    bear_mace_model = make_model(BearMaceModel.fancy_bear_mace_interaction)

    fancy_bear_mace_runner = BearMaceModelRunner(bear_mace_model)
    fancy_bear_mace_runner.run_model(4000, 12000)
    fancy_bear_mace_runner.visualize_trace()

    plt.show()

if __name__=='__main__':
    main()