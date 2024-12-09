from collections import Counter


def calculate_similarity_score(left_list, right_list):
    # Count the frequency of each number in the right list
    right_count = Counter(right_list)

    # Initialize total similarity score
    total_similarity_score = 0

    # Iterate through each number in the left list
    for number in left_list:
        # Get the count of the current number from the right list
        count_in_right = right_count.get(number, 0)
        # Update the similarity score
        total_similarity_score += number * count_in_right

    return total_similarity_score


# Read input.txt from input.txt
def read_pairs_from_file(filename):
    left_list = []
    right_list = []
    with open(filename, 'r') as file:
        for line in file:
            # Parse each line into a pair of integers
            pair = tuple(map(int, line.strip().split()))
            left_list.append(pair[0])
            right_list.append(pair[1])
    return left_list, right_list


# Main execution
if __name__ == "__main__":
    # Specify the input.txt file name
    input_file = "input.txt"

    # Read pairs from the file
    left_list, right_list = read_pairs_from_file(input_file)

    # Calculate and print the result
    result = calculate_similarity_score(left_list, right_list)
    print("Similarity Score:", result)
