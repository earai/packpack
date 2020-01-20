from packpack.tool_threat_interaction.bear_mace_model import BearMaceModel
from packpack.tool_threat_interaction.bear_mace_model_runner import BearMaceModelRunner


def main():

    bear_mace_model = BearMaceModel(make_environment=BearMaceModel.make_environment,
                                    make_mace=BearMaceModel.make_mace,
                                    make_bear = BearMaceModel.make_bear,
                                    make_encounter_result= BearMaceModel.crude_bear_mace_interaction
                                    )

    bear_mace_runner = BearMaceModelRunner(bear_mace_model)
    bear_mace_runner.run_model(2000, 2000)
    bear_mace_runner.visualize_trace()

if __name__=='__main__':
    main()