from collections import defaultdict

def remove_duplicates(num_file):
    numbers = num_file.split()
    d = defaultdict(list)
    
    for i, k in enumerate(numbers):
        d[k].append(i)
    
    sorted_numbers = [numbers[i] for i in sorted(d[k][len(d[k]) // 2] for k in sorted(d.keys()))]
    return sorted_numbers

if __name__ == "__main__":
    with open("task1_1_numbers.txt", "r") as file:
        num_file = file.read()
    
    sorted_numbers = remove_duplicates(num_file)
  
    with open("result.txt", "w") as file:
        file.write(" ".join(sorted_numbers))


