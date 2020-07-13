from enum import Enum

class BaseAttribute(Enum):
    STRENGTH = 1
    AGILITY = 2
    DEXTERITY = 3
    PERCEPTION = 4
    CONSTITUTION = 5
    INTELLIGENCE = 6
    WISDOM = 7
    CHARISMA = 8

class DerivedAttribute(Enum):
    SPEED = 1
    EVADE = 2
    HITPOINTS = 3
    PARRY = 4
    
    

class Character():
    def __init__(self, attributes = [10, 10, 10, 10, 10, 10, 10, 10]):
        self.base_attributes = attributes
        self.derived_attributes = [0, 0, 0, 0]
        self.calc_derived()

    def get_base_attribute(self, baseAttribute):
        return self.base_attributes[baseAttribute.value - 1]

    def set_base_attribute(self, baseAttribute, value):
        self.base_attributes[baseAttribute.value - 1] = value

    def get_derived_attribute(self, derivedAttribute):
        return self.derived_attributes[derivedAttribute.value - 1]

    def set_derived_attribute(self, derivedAttribute, value):
        self.derived_attributes[derivedAttribute.value - 1] = value

    def calc_derived(self):
        self.set_derived_attribute(DerivedAttribute.SPEED, self.get_base_attribute(BaseAttribute.AGILITY) * 2)
