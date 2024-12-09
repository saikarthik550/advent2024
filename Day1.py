def calculate_total_distance_from_pairs(pairs):
    # Split the pairs into two separate lists
    left_list = [pair[0] for pair in pairs]
    right_list = [pair[1] for pair in pairs]

    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    # Calculate the sum of absolute differences
    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

    return total_distance

# Read input.txt from input.txt
def read_pairs_from_file(filename):
    pairs = []
    with open(filename, 'r') as file:
        for line in file:
            # Parse each line into a pair of integers
            pair = tuple(map(int, line.strip().split()))
            pairs.append(pair)
    return pairs

# Main execution
if __name__ == "__main__":
    # Specify the input.txt file name
    input_file = "input.txt"

    # Read pairs from the file
    pairs = read_pairs_from_file(input_file)

    # Calculate and print the result
    result = calculate_total_distance_from_pairs(pairs)
    print("Total Distance:", result)
