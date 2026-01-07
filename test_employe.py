from employee import process_employee_data

def test_default_values():
    result = process_employee_data(["employee.py"])

    assert result["employee_name"] == "Rahul Verma"
    assert result["employee_id"] == "EMP1023"
    assert result["department"] == "Finance"
    assert result["total"] == 138000
    assert result["average"] == 46000
    assert result["category"] == "Good Performer"


def test_command_line_arguments():
    args = [
        "employee.py",
        "Abhijith",
        "EMP2001",
        "IT",
        "55000",
        "52000",
        "53000"
    ]

    result = process_employee_data(args)

    assert result["employee_name"] == "Abhijith"
    assert result["employee_id"] == "EMP2001"
    assert result["department"] == "IT"
    assert result["total"] == 160000
    assert result["average"] == 53333.333333333336
    assert result["category"] == "Excellent Performer"
