class Character:
    def __init__(self, name, health, speed):
        self.name = name
        self.health = health
        self.speed = speed
    def double_speed(self):
        self.speed = self.speed * 2
    def halfhealth(self):
        self.health = self.health * 0.5
warrior = Character(name="Warrior", health=100,speed=10)
ninja = Character(name="Ninja", health=100, speed=10)

print("Warrior health = ", warrior.health)
print("Ninja speed = ", ninja.speed)
print("Warrior speed = ", warrior.speed)
warrior.double_speed()
print("Warrior speed = ", warrior.speed)
ninja.halfhealth()
print("Ninja health = ", ninja.health)