import math
import os
import time

def print_heart(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    width = 80
    height = 24
    for y in range(height, -height, -1):
        row = ""
        for x in range(-width, width):
            if (x*0.05)**2 + (y*0.1)**2 <= 1:
                row += "*"
            else:
                row += " "
        print(row)
    print(text.center(width*2))

def move_text():
    text = "Tuyền"
    while True:
        for i in range(-10, 10):
            print_heart(" " * i + text)
            time.sleep(0.1)
        for i in range(10, -10, -1):
            print_heart(" " * i + text)
            time.sleep(0.1)

if __name__ == "__main__":
    move_text()
    
