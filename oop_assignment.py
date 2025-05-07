"""
OOP Assignment: Superheroes and Movement Demonstration
Demonstrates class design, inheritance, and polymorphism
"""

# Base Class
class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self.secret_identity = secret_identity
        self.power_level = power_level
        self._secret_base = "Undisclosed Location"  # Encapsulated attribute

    def introduce(self):
        print(f"I am {self.name}! (Secret identity: {self.secret_identity})")

    def power_up(self):
        self.power_level += 10
        print(f"{self.name} powers up to {self.power_level}!")

    def move(self):
        print(f"{self.name} moves in a generic superhero way!")

    # Encapsulation example
    def reveal_secret_base(self, clearance_level):
        if clearance_level >= 3:
            return self._secret_base
        return "Access Denied"

# Inherited Classes (Polymorphism)
class FlyingHero(Superhero):
    def move(self):
        print(f"{self.name} soars through the sky! ✈")

class TeleportingHero(Superhero):
    def move(self):
        print(f"{self.name} vanishes in a puff of smoke! 💨")

class SwimmingHero(Superhero):
    def move(self):
        print(f"{self.name} swims at incredible speed! 🏊")

# Demonstration
def hero_movement_demo(heroes):
    print("\n=== Superhero Movement Demonstration ===")
    for hero in heroes:
        hero.move()  # Polymorphism in action

if __name__ == "__main__":
    # Create superhero instances
    superman = FlyingHero("Superman", "Clark Kent", 95)
    nightcrawler = TeleportingHero("Nightcrawler", "Kurt Wagner", 80)
    aquaman = SwimmingHero("Aquaman", "Arthur Curry", 85)

    # Demonstrate functionality
    superman.introduce()
    nightcrawler.introduce()
    aquaman.introduce()

    # Polymorphism demonstration
    hero_movement_demo([superman, nightcrawler, aquaman])

    # Encapsulation demonstration
    print(f"\nSecret base access (low clearance): {superman.reveal_secret_base(1)}")
    print(f"Secret base access (high clearance): {superman.reveal_secret_base(5)}")