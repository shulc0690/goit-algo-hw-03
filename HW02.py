import turtle

TTL = turtle.Turtle()
screen = turtle.Screen()  # Create the screen.
# screen.setup(620, 620)  # Set Window size.


def koch_snowflake(TTL, length, level, angle):
    if level == 0:
        TTL.forward(length)
        return
    length /= 3.0
    koch_snowflake(TTL, length, level - 1, angle)
    TTL.left(angle)
    koch_snowflake(TTL, length, level - 1, angle)
    TTL.right(angle * 2)
    koch_snowflake(TTL, length, level - 1, angle)
    TTL.left(angle)
    koch_snowflake(TTL, length, level - 1, angle)


def draw_snowflake(TTL, length, level, angle):
    for _ in range(3):
        koch_snowflake(TTL, length, level, angle)
        TTL.right(120)


if __name__ == "__main__":
    TTL.speed(0)  # Максимальна швидкість малювання
    TTL.penup()
    TTL.goto(-450, 250)
    TTL.pendown()
    angle = 50
    level = int(input("Введіть рівень рекурсії: "))
    draw_snowflake(TTL, 400, level, angle)
    screen.exitonclick()  # Exit screen
