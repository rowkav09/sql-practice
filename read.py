import sqlite3

conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()

select_students = """
SELECT id, firstname, lastname, age
FROM students
WHERE age >= 15
"""
cursor.execute(select_students)

first_student = cursor.fetchone()
more_students = cursor.fetchmany(10)
other_students = cursor.fetchall()

print("First student:", first_student)
print("Next 10 students:", more_students)
print("Remaining students:", other_students)


query_j = """
SELECT *
FROM students
WHERE firstname LIKE 'J%'
LIMIT 5;
"""
cursor.execute(query_j)
students_j = cursor.fetchall()
print("\nStudents with firstname starting with 'J':", students_j)


count_by_gender = """
SELECT gender, COUNT(*)
FROM students
GROUP BY gender;
"""
cursor.execute(count_by_gender)
gender_counts = cursor.fetchall()
print("\nNumber of students by gender:", gender_counts)


sum_by_letter = """
SELECT substr(firstname, 1, 1) AS first_letter, SUM(age)
FROM students
GROUP BY first_letter;
"""
cursor.execute(sum_by_letter)
age_sums = cursor.fetchall()
print("\nSum of ages by first letter:", age_sums)


average_query = """
SELECT avg(age)
FROM students
WHERE gender = ?
"""
average_female_age = cursor.execute(average_query, ('female',)).fetchone()[0]
print("\nAverage age of female students:", average_female_age)

group_by_query = """
SELECT gender, avg(age)
FROM students
GROUP BY gender
"""
average_by_gender = cursor.execute(group_by_query).fetchall()
print("\nAverage age by gender:", average_by_gender)

conn.close()
