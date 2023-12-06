from lib.students import Students

# Students.drop_table()

# print("===========Creating Table=========")
# Students.create_table()
# print("===========Table Created=========")

# print("===========Inserting Students=========")
# Students.create("Mike", 10000)
# Students.create("Pat", 5000)
# Students.create("Joan", 11000)
# Students.create("Caleb", 10000)
# Students.create("Nick", 11000)

print("===========Fetching Students=========")
Students.fetch_students()

print("===========Fetching Students by name=========")
Students.fetch_students_by_name("Caleb")

print("===========Fetching Students by fees=========")
Students.fetch_students_by_fees(10000, ">")


# Students.update_students(10, "Michael", 25000)

# Students.delete_students(1)