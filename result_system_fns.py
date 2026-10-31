students = {
"S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
"S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
"S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
"S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
"S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}},
}

def calculate_total(marks):
  return sum(marks.values())

def calculate_average(marks):
  avg = round((calculate_total(marks)/len(marks)), 2)
  return avg

def get_grade(average):
  if average >= 90:
    return "A"
  elif average >= 75 and average < 90:
    return "B"
  elif average >= 60 and average < 75:
    return "C"
  elif average >= 40 and average < 60:
    return "D"
  else:
    return "F"

def check_result(marks, pass_mark=40):
  for item in marks.values():
    if item < pass_mark:
      return "Fail"

  return "Pass"

def student_summary(student):
  marks = student["marks"]
  total = calculate_total(marks)
  avg = calculate_average(marks)
  grade = get_grade(avg)
  result = check_result(marks)
  return {
      "name": student["name"],
      "total": total,
      "average": avg,
      "grade": grade,
      "result": result
  }

def add_student(data, student_id, name, **marks):
  if student_id in data:
    return False
  
  data[student_id] = {"name": name, "marks": marks}
  return True

def update_marks(data, student_id, **changes):
  if student_id not in data:
    return False
  data[student_id]["marks"].update(changes)
  return True

def remove_student(data, student_id):
  if student_id not in data:
    return False
  data.pop(student_id)
  return True

def print_report(data):
 avg_id = []
 for item in data:
  avg_id.append((calculate_average(data[item]["marks"]), item))
 avg_id.sort(reverse=True)
 print(f"{"ID":<6}{"Name":<8}{"Total":>6}{"Avg":>8}{"Grade":>7}  {"Result"}")
 print(f"{"-"*42}")
 for avg,student_id in avg_id:
  stu_sum = student_summary(data[student_id])
  print(f"{student_id:<6}{stu_sum["name"]:<8}{stu_sum["total"]:>6}{avg:>8.2f}{stu_sum["grade"]:>7}  {stu_sum["result"]}")

def class_statistics(data, *subjects):
  avg_id = []
  for item in data:
    avg_id.append((calculate_average(data[item]["marks"]), item))
  avg_id.sort(reverse=True)
  topper = data[avg_id[0][1]]["name"]
  passed = 0
  for student_id in data:
    result = student_summary(data[student_id])["result"]
    if result == "Pass":
      passed += 1
  pass_percentage = round((passed/len(data))*100, 1)
  if not subjects:
    first_id = list(data)[0]
    subjects = list(data[first_id]["marks"])
  sub_avg = {}
  for sub in subjects:
    total = 0
    for student_id in data:
      total += data[student_id]["marks"][sub]
    sub_avg[sub] = round((total/len(data)), 1)
  return {
        "topper":topper,
        "pass_percentage":pass_percentage,
        "sub_avg":sub_avg
    }

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
