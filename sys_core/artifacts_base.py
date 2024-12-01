from abc import ABCMeta
from enum import Enum


class ArtifactPos(Enum):
    FlowerOfLife = 0
    PlumeOfDeath = 1
    SandsOfEon = 2
    GobletOfEonothem = 3
    CircletOfLogos = 4


class Artifact(metaclass=ABCMeta):
    pass