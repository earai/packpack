from packpack.prove_pymc3 import build_proof_model
import pymc3 as pm


def test_proof_model():
    """Just prove it runs"""
    m = build_proof_model()
    with m:
        trace = pm.sample(50, tune=50)
    assert trace.report.ok
