import random
import math


def random_approximation(accuracy):
    inside_unit_circle = 0
    for i in range(accuracy):
        # print(i)
        x = random.random()*2 - 1
        y = random.random()*2 - 1
        # print("x: " + str(x))
        # print("y: " + str(y))
        magnitude = x*x + y*y  # no sqrt needed since radius is 1, thus comparison result will not change
        # print(magnitude)
        if -1 <= magnitude <= 1:
            inside_unit_circle += 1
            # print("is inside unit circle")
    pi = 4 * inside_unit_circle / accuracy
    print(pi)
    return pi


def riemann_approximation(accuracy):
    sum = 0
    for i in range(accuracy):
        sum += 1/((i+1)*(i+1))
    pi = math.sqrt(sum*6)
    print(pi)
    return pi


# riemann_approximation(10000000)
random_approximation(100000000)
