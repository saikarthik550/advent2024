def is_safe_report(report):
    # Check if the levels are either all increasing or all decreasing
    increasing = True
    decreasing = True
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        # Check if the difference is between 1 and 3
        if not (1 <= abs(diff) <= 3):
            return False  # Unsafe because difference is out of bounds

        # Check if increasing or decreasing condition holds
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

    # If it's either increasing or decreasing, the report is safe
    return increasing or decreasing


def count_safe_reports(input_data):
    safe_count = 0

    for line in input_data:
        # Convert the line into a list of integers (levels)
        report = list(map(int, line.strip().split()))

        # Check if the report is safe
        if is_safe_report(report):
            safe_count += 1

    return safe_count


# Read the input.txt data from the file
def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


# Main execution
if __name__ == "__main__":
    # Specify the input.txt file name (change this as needed)
    input_file = "input.txt"

    # Read the input.txt data from the file
    input_data = read_input_file(input_file)

    # Calculate and print the result
    result = count_safe_reports(input_data)
    print(f"Number of safe reports: {result}")
