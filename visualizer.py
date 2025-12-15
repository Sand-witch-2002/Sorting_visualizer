import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def visualize(arr, i=None, j=None):
    clear()
    for idx, val in enumerate(arr):
        if idx == i or idx == j:
            print(f"[{val}]", end=" ")
        else:
            print(val, end=" ")
    print()
    time.sleep(0.2)
