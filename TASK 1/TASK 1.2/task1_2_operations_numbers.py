import os

def import_data(file_path):
    """Imports data from a file."""
    try:
        with open(file_path) as file:
            return [tuple(map(int, line.strip().split())) for line in file]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error importing data: {e}")
        return []

def perform_operations(numbers, operations):
    """Performs operations on the numbers list."""
    result = []
    for operation, value in operations:
        if operation == 1:
            result.append(f"Searching for {value}: {'Found' if value in numbers else 'Not Found'}")
        elif operation == 2:
            numbers.append(value)
            numbers.sort()
            result.append(f"Inserted {value}")
        elif operation == 3:
            if value in numbers:
                numbers.remove(value)
                result.append(f"Deleted {value}")
            else:
                result.append(f"Not found, deletion failed: {value}")
    return numbers, result

def main():
    """Main function to run the program."""
    numbers = sorted([int(num) for num in open("task1_2_numbers.txt").read().split()])
    operations = import_data("task1_2_operations.txt")
    if not numbers or not operations:
        print("Error: Unable to proceed due to missing data.")
        return
    numbers, operation_results = perform_operations(numbers, operations)
    with open("result.txt", 'w') as result_file:
        result_file.write('\n'.join(map(str, numbers)))
    print("Final Sorted Numbers:", numbers)
    print("Operation Results:")
    for result in operation_results:
        print(result)

if __name__ == "__main__":
    main()


