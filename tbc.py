""Hero attributes"
HP:30
Hit chance:60
hitDamage:5
Armor:4""
""Enemy
HP:40
hitChance:40
hitDamage:5
Armor:2""

class Character(object)
  def__init__(self, name: str, hitPoint: int, hitChance: int, hitDamage: int, armor: int):
    self.name = name
    self.hitPoint = hitPoint
    self.hitDamage = hitDamage
    self.chance = hitChance
    self.armor = armor
