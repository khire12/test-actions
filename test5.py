import sys
import random


class Apple:
    def __init__(self, color):
        self.color = color

    def repeat_color(self, num=10):
        for i in range(num):
            print(self.color)


k = 1
apple = Apple("red")
apple.repeat_color()
break
