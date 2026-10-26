#problem 1
resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    if not resources:
        print("No resources found.")
        return

    for resource in resources:
        resource_id, name, category, quantity = resource

        if quantity < 0:
            print("Invalid quantity for", name)
            continue

        print(resource_id, name, category, quantity)


def search_by_category(resources, category):
    found = False

    for resource in resources:
        resource_id, name, resource_category, quantity = resource

        if resource_category.lower() == category.lower():
            if quantity < 0:
                print("Invalid quantity for", name)
                continue

            print(resource_id, name, resource_category, quantity)
            found = True

    if not found:
        print("No resources found in this category.")

def find_unavailable(resources):
    found = False

    for resource in resources:
        resource_id, name, category, quantity = resource

        if quantity == 0:
            print("Unavailable:", name, "ID:", resource_id)
            found = True

    if not found:
        print("No unavailable resources found.")


def search_by_id(resources, resource_id):
    for resource in resources:
        if resource[0] == resource_id:
            print("Resource found:", resource)
            return

    print("Resource ID not found.")


print("\nAll Resources:")
display_resources(resources)

print("\nElectronics Resources:")
search_by_category(resources, "Electronics")

print("\nUnavailable Resources:")
find_unavailable(resources)

print("\nTest 1: Unknown Resource ID")
search_by_id(resources, 999)

print("\nTest 2: Negative Quantity")
display_resources([[106, "Printer", "Electronics", -2]])

print("\nTest 3: Zero Quantity")
find_unavailable([[102, "Projector", "Electronics", 0]])

print("\nTest 4: Empty Resource List")
display_resources([])


#problem 2

students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]

def calculate_average(marks):
    if len(marks) != 3:
        return None

    for mark in marks:
        if not isinstance(mark, (int, float)) or mark < 0 or mark > 100:
            return None

    average = sum(marks) / len(marks)
    return average

def classify_performance(average):
    if average is None:
        return "Invalid Data"

    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    if not students:
        print("No student records found.")
        return

    for student in students:
        student_id, name, marks = student

        average = calculate_average(marks)

        if average is None:
            print("ID:", student_id,
                  "Name:", name,
                  "Invalid or missing marks")
        else:
            performance = classify_performance(average)

            print("ID:", student_id,
                  "Name:", name,
                  "Average:", round(average, 2),
                  "Performance:", performance)

print("\nStudent Performance Report:")
display_report(students)

print("\nTest 1: Equal Marks")
display_report([[205, "Tania", [80, 80, 80]]])


print("\nTest 2: Tied Averages")
display_report([
    [205, "Tania", [80, 80, 80]],
    [206, "Karim", [70, 80, 90]]
])


print("\nTest 3: Invalid Mark")
display_report([[207, "Samira", [90, 110, 70]]])


print("\nTest 4: No Marks")
display_report([[208, "Rafi", []]])
