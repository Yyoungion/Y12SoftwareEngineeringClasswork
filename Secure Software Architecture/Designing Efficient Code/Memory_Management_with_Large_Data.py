def read_all_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())

read_all_lines('Secure Software Architecture\Designing Efficient Code\large_data.txt')

# Task:
# - Rewrite this function to process the file line-by-line instead of loading everything at once.
# - Use a generator or iterate directly over the file object for memory efficiency.