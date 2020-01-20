import pymc3 as pm

from packpack.datamodels import Mace


def test_mace():
    """Test that we can initialize a Mace"""
    with pm.Model() as model:
        mace = Mace(eye_sting=pm.Exponential('eye_sting', 1.0), nose_burn=pm.Exponential('nose_burn', 1.0))

    sting = mace.eye_sting.random()
    burn = mace.nose_burn.random()
    assert sting > 0
    assert burn > 0