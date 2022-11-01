from turtle import *

color("red")
forward(200)
left(120)

color("blue")
forward(100)
left(200)


for i in range(3):
    color("blue")
    forward(256)
    left(120)

    for i in range(3):
        color("red")
        forward(128)
        left(120)
        
        for i in range(3):
            color("green")
            forward(64)
            left(120)

            for i in range(3):
                color("brown")
                forward(32)
                left(120)
                
                for i in range(3):
                    color("purple")
                    forward(16)
                    left(120)


exitonclick()