class Creature:
    health_points: int = 0

class EarthCreature(Creature):
    pass

class SeaCreature(Creature):
    pass

class AirCreature(Creature):
    pass

class Troll(EarthCreature):
    health_points: int = 100

class Elf(EarthCreature):
    health_points: int = 80

class Mermaid(SeaCreature):
    health_points: int = 60

class Siren(SeaCreature):
    health_points: int = 75

class Dragon(AirCreature):
    health_points: int = 120

class Pegasus(AirCreature):
    health_points: int = 85
