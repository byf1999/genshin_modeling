from abc import ABCMeta
from enum import Enum
from typing import Dict

from sys_core import Weapon, WeaponType, Artifact, ArtifactPos, Skill, SkillType


MAX_LEVEL = 90


class ElementType(Enum):
    Pyro = 0
    Hydro = 1
    Dendro = 2
    Electro = 3
    Anemo = 4
    Cryo = 5
    Geo = 6
    Physical = 7

class Character(metaclass=ABCMeta):
    def __init__(self, level: int, element_type: ElementType,
                 hp: int, atk: int, defense: int, ele_mastery: int,
                 crit_rate: float, crit_dmg: float,
                 ele_dmg_bonus: Dict[ElementType: float], energy_recharge: float,
                 weapon_type: WeaponType, skills: Dict[SkillType, Skill],
                 cd_reduce: float = 0, shield_strength: float = 0,
                 healing_bonus: float = 0, income_heal_bonus: float = 0):
        assert level >= 1 and level <= MAX_LEVEL
        self._level = level
        self._element_type = element_type
        self._hp = hp
        self._atk = atk
        self._defense = defense
        self._ele_mastery = ele_mastery
        self._crit_rate = crit_rate
        self._crit_dmg = crit_dmg
        self._ele_dmg_bonus = ele_dmg_bonus
        self._energy_recharge = energy_recharge
        self._cd_reduce = cd_reduce
        self._shield_strength = shield_strength
        self._healing_bonus = healing_bonus
        self._income_healing_bonus = income_heal_bonus
        self._weapon_type = weapon_type

        self._skill = skills
        self._weapon: Weapon = None
        self._artifact: Dict[ArtifactPos: Artifact] = None

    @property
    def level(self):
        return self._level

    @property
    def element_type(self):
        return self._element_type

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    @property
    def defense(self):
        return self._defense

    @property
    def ele_mastery(self):
        return self._ele_mastery

    @property
    def crit_rate(self):
        return self.crit_rate

    @property
    def crit_dmg(self):
        return self._crit_dmg

    @property
    def ele_dmg_bonus(self):
        return self._ele_dmg_bonus

    @property
    def energy_recharge(self):
        return self._energy_recharge

    @property
    def cd_reduce(self):
        return self._cd_reduce

    @property
    def shield_strength(self):
        return self._shield_strength

    @property
    def healing_bonus(self):
        return self._healing_bonus

    @property
    def income_healing_bonus(self):
        return self._income_healing_bonus

    @property
    def weapon_type(self):
        return self._weapon_type

    @property
    def skill(self):
        return self._skill

    @property
    def weapon(self):
        return self._weapon

    @property
    def artifact(self):
        return self._artifact

    def skill_damage(self, skill_type: SkillType):
        assert skill_type in (SkillType.NormalAttack, SkillType.E, SkillType.Q)
        skill = self.skill.get(skill_type)
        ele_dmg_bonus = self.ele_dmg_bonus.get(skill.dmg_type, 0)
        dmg = skill.damage(self.atk) * (1 + ele_dmg_bonus)
        print(f"期望伤害: {dmg * (1 - self.crit_rate + self.crit_rate * self._crit_dmg)}")
        print(f"暴击伤害: {dmg * self._crit_dmg}")
        return

    def add_weapon(self, weapon: Weapon):
        assert weapon.weapon_type == self.weapon_type
        self._weapon = weapon

