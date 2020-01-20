from pymc3.model import PyMC3Variable
from dataclasses import dataclass


@dataclass
class Mace:
    """Mace tool"""

    eye_sting: PyMC3Variable
    nose_burn: PyMC3Variable

