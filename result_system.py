students = {
"S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
"S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
"S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
"S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
"S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}},
}


from result_system_fns import (
    calculate_total,
    calculate_average,
    get_grade,
    check_result,
    student_summary,
    add_student,
    update_marks,
    remove_student,
    print_report,
    class_statistics
)

def main():
  print("Task 1: One student")
  print(student_summary(students["S101"]))
  print(check_result(students["S102"]["marks"]))
  print(check_result(students["S102"]["marks"], pass_mark=35))
  print(check_result(students["S102"]["marks"], 35))
  print("")
  print("Task 2: Report")
  print_report(students)
  print("")
  print("Task 3: Update Marks")
  print(update_marks(students, "S102", Maths=55))
  print(update_marks(students, "S999", Maths=55))

  corrections = {"Python": 50, "Stats": 58}
  print(update_marks(students, "S102", **corrections))
  print(student_summary(students["S102"]))
  print("")
  print("Task 4: Add student")
  print(add_student(data=students, student_id="S106", name="Farhan",Python=70, Maths=35, Stats=74 ))
  print(add_student(data=students, student_id="S101", name="Zara",Python=70, Maths=35, Stats=74 ))
  print(students["S106"])
  print("")
  print("Task 5: Remove student")
  print(remove_student(students, "S104"))
  print(remove_student(students, "S104"))
  print(len(students))
  print("")
  stats = class_statistics(students)
  print("Task 6: Final report and statistics")
  print_report(students)

  print(f"Topper: {stats["topper"]}")
  print(f"Pass percentage: {stats["pass_percentage"]}")
  print(f"Subject averages: {stats["sub_avg"]}")

  print(f"Python and Stats only: {class_statistics(students, "Python", "Stats")["sub_avg"]}")


main()