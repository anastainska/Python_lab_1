class Turtle:
    colour = "Colour of all the turtles is green"

    def __init__(self, scientific_name, speed, weight, age, length):
        self.scientific_name = scientific_name
        self.speed = speed
        self.weight = weight
        self.age = age
        self.length = length

    def __del__(self):
        return

    def __str__(self):
        return f"Scientific_name: {self.scientific_name}\n" \
               f"Speed: {self.speed}\n" \
               f"Weight: {self.weight}\n" \
               f"Age: {self.age}\n" \
               f"Length: {self.length}"

    @staticmethod
    def get_turtle_colour():
        return Turtle.colour


def main():
    turtle_1 = Turtle("Rafaello", "30 km/h", "24 kg", "3 years", "29 cm")
    turtle_2 = Turtle("Michelangelo", "45 km/h", "19 kg", "5 years", "45 cm")

    print(turtle_1)


if __name__ == "__main__":
    main()