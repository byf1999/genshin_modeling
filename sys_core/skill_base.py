from abc import ABCMeta
from enum import Enum

from sys_core import ElementType


MAX_LEVEL = 15


class SkillType(Enum):
    NormalAttack = 0
    E = 1
    Q = 2
    Passive = 3


class Skill(metaclass=ABCMeta):
    def __init__(self, skill_type: SkillType, dmg_type: ElementType,
                 level: int, ):
        assert level >= 1 and level <= MAX_LEVEL
        self._skill_type = skill_type
        self._dmg_type = dmg_type
        self._level = level

    @property
    def damage(self, *args):
        return 0

    @property
    def skill_type(self):
        return self._skill_type

    @property
    def dmg_type(self):
        return self._dmg_type

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        assert level >= 1 and level <= MAX_LEVEL
        self._level = level
