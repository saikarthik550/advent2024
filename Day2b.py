def is_safe_report(report):
    """Checks if the report is safe (increasing or decreasing and all differences between 1 and 3)."""
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


def can_be_fixed_by_removing_one_level(report):
    """Checks if removing one level from the report can make it safe."""
    for i in range(len(report)):
        # Remove the i-th level
        new_report = report[:i] + report[i + 1:]

        # Check if the new report is safe
        if is_safe_report(new_report):
            return True  # It can be fixed by removing one level

    return False  # If no level can be removed to make it safe


def count_safe_reports(input_data):
    safe_count = 0

    for line in input_data:
        # Convert the line into a list of integers (levels)
        report = list(map(int, line.strip().split()))

        # Check if the report is safe or can be made safe by removing one level
        if is_safe_report(report) or can_be_fixed_by_removing_one_level(report):
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
