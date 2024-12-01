from abc import ABCMeta
from enum import Enum


MAX_LEVEL = 90
class WeaponType(Enum):
    SWORD = 0
    CLAYMORE = 1
    CATALYST = 2
    POLEARM = 3
    BOW = 4



class Weapon(metaclass=ABCMeta):
    def __init__(self, weapon_type: WeaponType, level: int, ):
        assert level >= 1 and level <= MAX_LEVEL
        self._weapon_type = weapon_type
        self._level = level

    @property
    def weapon_type(self):
        return self._weapon_type

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        assert level >= 1 and level <= MAX_LEVEL
        self._level = level
