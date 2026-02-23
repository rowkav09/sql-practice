import sqlite3
from faker import Faker
import random

# Connect to database
conn = sqlite3.connect("student.sqlite")
cursor = conn.cursor()


insert_query = """
INSERT INTO students (firstname, lastname, age, gender)
VALUES ('Hermione', 'Grainger', 14, 'female');
"""
cursor.execute(insert_query)
conn.commit()

parameterised_insert_query = """
INSERT INTO students (firstname, lastname, age, gender)
VALUES (?, ?, ?, ?);
"""
cursor.execute(parameterised_insert_query, ("Harry", "Potter", 13, "male"))
conn.commit()


fake = Faker('en_GB')
random.seed(4321)
fake.random.seed(4321)

for _ in range(10):
    f_name = fake.first_name()
    l_name = fake.last_name()
    age = random.randint(11, 18)
    gender = random.choice(('male', 'female'))
    cursor.execute(parameterised_insert_query,
                   (f_name, l_name, age, gender))
conn.commit()

data = [(fake.first_name(),
         fake.last_name(),
         random.randint(11, 18),
         random.choice(('male', 'female')))
        for _ in range(20)]

cursor.executemany(parameterised_insert_query, data)
conn.commit()

update_query = """
UPDATE students
SET lastname = ?
WHERE id = 4;
"""
cursor.execute(update_query, ('Smith',))
conn.commit()


conn.close()

print("Data written and updated successfully.")
