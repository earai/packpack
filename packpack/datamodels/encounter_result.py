from pymc3.model import PyMC3Variable
from dataclasses import dataclass


@dataclass
class EncounterResult:

    # A Beroulli random variable that is true if we survived the encounter
    survived: PyMC3Variable
