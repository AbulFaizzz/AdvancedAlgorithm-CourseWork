import multiprocessing

def count_frequency(args):
    name, text = args
    return name, text.lower().count(name.lower())

def parallel_frequency_count(names, text):
    with multiprocessing.Pool() as pool:
        return dict(pool.map(count_frequency, [(name, text) for name in names]))

def read_file(filename):
    try:
        with open(filename, 'r', errors='ignore') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"Error reading '{filename}': {e}")

def write_result(filename, result):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines([f"{name}: {count}\n" for name, count in result.items()])
        print(f"Result has been written to '{filename}'.")
    except IOError as e:
        print(f"Error writing to '{filename}': {e}")

def main():
    names = read_file("task1_3_names.txt")
    text = read_file("task1_3_text.txt")

    if not all([names, text]):
        print("Aborting operation due to file read errors.")
        return

    names = names.splitlines()
    if not names:
        print("Error: No names found in 'names.txt'.")
        return

    result = parallel_frequency_count(names, text)
    write_result("result.txt", result)

    print("Frequency Count Result:", result)

if __name__ == "__main__":
    main()
