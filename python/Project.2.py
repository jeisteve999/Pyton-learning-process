def calculate_average(values):
    # Validate that the list is not empty
    assert len(values) > 0, "The list is empty"

    # Validate that all elements are numbers
    for element in values:
        assert isinstance(element, (int, float)), f"Non-numeric element found: {element}"

    # Calculate and return average
    return sum(values) / len(values)

# Try/except block for error handling
try:
    average = calculate_average(values=["Text"])  # test case with error
    # average = calculate_average(values=[10, 20, 30])  # correct test case
    print(f"The average is: {average}")
except AssertionError as assert_error:
    print("Validation error:", assert_error)
except Exception as e:
    print("The function could not calculate the average:")
    print(e)