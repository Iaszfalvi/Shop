
import turtle, random

def move(person):
    person.left(random.randint(1,360))
    person.forward(random.randint(1,100))

def moveDirection(direction):
    bob.direction(50)


def direction(move):
        if move =='\x1b[A':
                moveDirection("forward")
        elif  move =='\x1b[B':
                moveDirection("backward")
        elif move =='\x1b[C':
                moveDirection("right")
        elif move =='\x1b[D':
                moveDirection("left")


bob = turtle.Turtle()
sarah = turtle.Turtle()
george = turtle.Turtle()
tom = turtle.Turtle()

bob.color("blue")
sarah.color("green")
george.color("red")
tom.color("purple")



# while True:
#     # move(random.choice([bob, sarah, george, tom]))
#     # move(bob)
bob.forward(100)

turtle.done()