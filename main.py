import random
from visualizer import visualize
from algorithms.bubble_sort import bubble_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_ import insertion_sort

def main():
    # Generate a random array of 10 numbers between 1 and 50
    arr = random.sample(range(1, 50), 10)
    print("Original array:", arr)
    input("Press Enter to start sorting...")

    # Choose sorting algorithm
    print("\nChoose sorting algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    
    choice = input("> ")

    if choice == "1":
        bubble_sort(arr, visualize)
    elif choice == "2":
        selection_sort(arr, visualize)
    elif choice == "3":
        insertion_sort(arr, visualize)
    else:
        print("Invalid choice")
        return

    print("\nSorted array:", arr)

if __name__ == "__main__":
    main()
