from packpack.tool_threat_interaction.bear_mace_model import BearMaceModel
from packpack.tool_threat_interaction.bear_mace_model_runner import BearMaceModelRunner
from matplotlib import pyplot as plt


def make_model(bear_mace_interaction):
    return BearMaceModel(make_environment=BearMaceModel.make_environment,
                                    make_mace=BearMaceModel.make_mace,
                                    make_bear = BearMaceModel.make_bear,
                                    make_encounter_result= bear_mace_interaction
                                    )

def main():

    crude_bear_mace_model = make_model(BearMaceModel.crude_bear_mace_interaction)
    fancy_bear_mace_model = make_model(BearMaceModel.fancy_bear_mace_interaction)


    crude_bear_mace_runner = BearMaceModelRunner(crude_bear_mace_model)
    crude_bear_mace_runner.run_model(4000, 12000)
    crude_bear_mace_runner.visualize_trace()


    fancy_bear_mace_runner = BearMaceModelRunner(fancy_bear_mace_model)
    fancy_bear_mace_runner.run_model(4000, 12000)
    fancy_bear_mace_runner.visualize_trace()

    plt.show()

if __name__=='__main__':
    main()