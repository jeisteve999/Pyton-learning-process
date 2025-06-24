def calculate_average(values):
    assert len(values) > 0, "The list is empty"
    return sum(values) / len(values)

try:
    average = calculate_average(values=["Text"])
    print(average)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print("The function didn't calculate the average")
    print(e)