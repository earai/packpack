from pymc3.model import PyMC3Variable
from dataclasses import dataclass


@dataclass
class Environment:

    latitude: PyMC3Variable
