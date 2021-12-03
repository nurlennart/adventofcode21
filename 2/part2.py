import json


class submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def forward(self, x):
        self.horizontal += x
        self.depth += self.aim * x

    def up(self, x):
        self.aim -= x
    
    def down(self, x):
        self.aim += x
    
def commandSubmarine():
    sub = submarine()
    with open('input.txt') as r:
        lines = r.read().splitlines()
        for line in lines:
            command = line.split(' ')
            if command[0] == 'forward':
                sub.forward(int(command[1]))
            if command[0] == 'up':
                sub.up(int(command[1]))
            if command[0] == 'down':
                sub.down(int(command[1]))
    r.close()
    print(sub.horizontal * sub.depth)

commandSubmarine()