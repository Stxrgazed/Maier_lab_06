def insertion_sort(arr):
    for current in range(1, len(arr)):
        key = arr[current]
        left = current - 1
        while left >= 0 and arr[left] > key:
            arr[left + 1] =  arr[left]
            left = left - 1 
        arr[left + 1] = key
    return arr

def selection_sort(arr):
    for current in range(len(arr)):
        minimum = current
        for other in range(current + 1, len(arr)):
            if arr[other] < arr[minimum]:
                minimum = other
        arr[current], arr[minimum] = arr[minimum], arr[current]
    return arr

def main():
    try:
        with open("date.txt", "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        print("File does not exist.")
        return

    if len(lines) != 2:
        print("File must contain exactly two input lines.")
    else:
        try:
            numbers = list(map(int, lines[0].split()))

            if len(numbers) == 0:
                print("No numbers provided.")
            else:
                algorithm = lines[1].strip()

                if algorithm == "Insertion":
                    result = insertion_sort(numbers.copy())
                elif algorithm == "Selection":
                    result = selection_sort(numbers.copy())
                else:
                    print("Invalid sorting algorithm.")
                    result = None

                if result is not None:
                    with open("date.txt", "a") as file:
                        file.write(f"Sorted using {algorithm}: {result}\n")
                
        except ValueError:
            print("Invalid numbers.")


main()
