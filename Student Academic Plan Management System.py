# Function to calculate plan status
def calculate_plan_status(cgpa, total_credit_hours, plan_total_credit_hours):
    min_allowed_credits = 12 if 0 < cgpa < 2 else 15
    max_allowed_credits = 13 if 0 < cgpa < 2 else 19

    if plan_total_credit_hours < min_allowed_credits:
        return "Underload"
    elif plan_total_credit_hours > max_allowed_credits or total_credit_hours + plan_total_credit_hours > 120:
        return "Overload"
    elif total_credit_hours + plan_total_credit_hours == 120 and plan_total_credit_hours < min_allowed_credits:
        return "OK"
    else:
        return "OK"


# Function to create a plan
def create_plan(plans):
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    cgpa = float(input("Enter student's CGPA: "))
    total_credit_hours = int(input("Enter total credit hours: "))
    courses = []
    while True:
        course_code = input("Enter course code (or enter 'done' to finish): ")
        if course_code.lower() == 'done':
            break
        course_name = input("Enter course name: ")
        credit_hours = int(input("Enter credit hours: "))
        courses.append((course_code, course_name, credit_hours))
    plan_total_credit_hours = sum([course[2] for course in courses])
    plan_status = calculate_plan_status(cgpa, total_credit_hours, plan_total_credit_hours)
    if student_id in plans:
        print("Student already has a plan.")
    else:
        plans[student_id] = {
            'student_name': student_name,
            'cgpa': cgpa,
            'total_credit_hours': total_credit_hours,
            'courses': courses,
            'plan_total_credit_hours': plan_total_credit_hours,
            'plan_status': plan_status
        }
        print("Plan created successfully.")


# Function to list all plans
def list_all_plans(plans):
    print("List of all plans:")
    for student_id, plan in plans.items():
        print(f"Student ID: {student_id}, Student Name: {plan['student_name']}, Total Hours: {plan['plan_total_credit_hours']}, Status: {plan['plan_status']}")


# Function to view student plan
def view_student_plan(plans):
    student_id = input("Enter student ID to view plan: ")
    if student_id in plans:
        plan = plans[student_id]
        print("Student Plan Details:")
        print(f"Student Name: {plan['student_name']}")
        print(f"Student ID: {student_id}")
        print(f"CGPA: {plan['cgpa']}")
        print(f"Total Credit Hours: {plan['total_credit_hours']}")
        print("Courses:")
        for course in plan['courses']:
            print(f"Course Code: {course[0]}, Course Name: {course[1]}, Credit Hours: {course[2]}")
        print(f"Plan Total Credit Hours: {plan['plan_total_credit_hours']}")
        print(f"Plan Status: {plan['plan_status']}")
    else:
        print("Student plan not found.")


# Function to delete a plan
def delete_plan(plans):
    student_id = input("Enter student ID to delete plan: ")
    if student_id in plans:
        del plans[student_id]
        print("Plan deleted successfully.")
    else:
        print("Student plan not found.")


# Function to save plans to a file
def save_plans(plans):
    with open("plans.txt", "w") as file:
        for student_id, plan in plans.items():
            file.write(f"{student_id},{plan['student_name']},{plan['cgpa']},{plan['total_credit_hours']},{plan['plan_total_credit_hours']},{plan['plan_status']},")
            for course in plan['courses']:
                file.write(f"{course[0]}:{course[1]}:{course[2]},")
            file.write("\n")
    print("Plans saved to file.")


# Main function
def main():
    plans = {}

    while True:
        print("\nMenu:")
        print("1. Create Plan")
        print("2. List all Plans")
        print("3. View Student Plan")
        print("4. Delete Plan")
        print("5. Save Plans")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_plan(plans)
        elif choice == '2':
            list_all_plans(plans)
        elif choice == '3':
            view_student_plan(plans)
        elif choice == '4':
            delete_plan(plans)
        elif choice == '5':
            save_plans(plans)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
