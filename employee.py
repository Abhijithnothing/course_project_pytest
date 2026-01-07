import sys

def process_employee_data(argv=None):
    if argv is None:
        argv = sys.argv

    # Check command-line arguments
    if len(argv) == 7:
        script_name = argv[0]
        emp_name = argv[1]
        emp_id = argv[2]
        department = argv[3]
        s1 = argv[4]
        s2 = argv[5]
        s3 = argv[6]
    else:
        script_name = argv[0]
        emp_name = "Rahul Verma"
        emp_id = "EMP1023"
        department = "Finance"
        s1 = "45000"
        s2 = "47000"
        s3 = "46000"

    # Calculate total and average salary
    total_salary = int(s1) + int(s2) + int(s3)
    average_salary = total_salary / 3

    # Performance category
    if average_salary >= 50000:
        category = "Excellent Performer"
    elif average_salary >= 40000:
        category = "Good Performer"
    elif average_salary >= 30000:
        category = "Average Performer"
    else:
        category = "Needs Improvement"

    return {
        "script_name": script_name,
        "employee_name": emp_name,
        "employee_id": emp_id,
        "department": department,
        "salary": (int(s1), int(s2), int(s3)),
        "total": total_salary,
        "average": average_salary,
        "category": category
    }

if __name__ == "__main__":
    result = process_employee_data()

    print("Script Name:", result["script_name"])
    print("Employee Name:", result["employee_name"])
    print("Employee ID:", result["employee_id"])
    print("Department:", result["department"])
    print("Salary for 3 Months:", *result["salary"])
    print("Total Salary:", result["total"])
    print("Average Salary:", result["average"])
    print("Performance Category:", result["category"])
