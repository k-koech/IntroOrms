# models/class - tables
# CRUD operations
# Fetch data - 
# Test cases

# SqlAchemy

from .config import CONN, CURSOR

class Students:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees
        self.id = None
        

    @classmethod
    def create_table(cls):
        sql = "CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,name STRING,fees FLOAT )"
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS students"
        CURSOR.execute(sql)
        CONN.commit()

    # CREATE
    def save(self):
        sql = "INSERT INTO students(name, fees) Values(?, ?)"
        CURSOR.execute(sql, (self.name, self.fees))
        # self.id = CURSOR.execute("SELECT ")
        CONN.commit()

    @classmethod
    def create(cls, name, fees):
        students = cls(name, fees)
        students.save()
        print(f"{students.name}  created successfully!" )
        

    # Fetch 
    @classmethod
    def fetch_students(cls):
        sql = "SELECT * FROM students"
        CURSOR.execute(sql)
        rows =  CURSOR.fetchall()
        
        students = []
        for row in rows:
            student = cls(name = row[1], fees = row[2])
            student.id = row[0]
            students.append(student)
            # print(f"Stud. Name => {student.name} Fees => {student.fees}")
        return students
    # Fetch by name
    @classmethod
    def fetch_students_by_name(cls, name):
        sql = "SELECT * FROM students where name=?"
        CURSOR.execute(sql, (name,))
        rows =  CURSOR.fetchall()
        
        students = []
        for row in rows:
            student = cls(name = row[1], fees = row[2])
            student.id = row[0]
            students.append(student)

            print(f"Stud. Name => {student.name} Fees => {student.fees}")

# Fetch by fees
    @classmethod
    def fetch_students_by_fees(cls, fees, operand):
        if operand == "<":
            sql = "SELECT * FROM students where fees < ?"
            CURSOR.execute(sql, (fees,))
            rows =  CURSOR.fetchall()
            
            students = []
            for row in rows:
                student = cls(name = row[1], fees = row[2])
                student.id = row[0]
                students.append(student)
                
                print(f"Stud. Name => {student.name} Fees => {student.fees}")
       
        elif operand == ">":
            sql = "SELECT * FROM students where fees > ?"
            CURSOR.execute(sql, (fees,))
            rows =  CURSOR.fetchall()
            
            students = []
            for row in rows:
                student = cls(name = row[1], fees = row[2])
                student.id = row[0]
                students.append(student)
                
                print(f"Stud. Name => {student.name} Fees => {student.fees}")

    # Update
    @classmethod
    def update_students(cls, id, name, fees):
        sql = "SELECT COUNT(*) FROM students WHERE id=?"
        CURSOR.execute(sql, (id,))
        count_students = CURSOR.fetchone()[0]

        if count_students >0:
            sql = "UPDATE students SET name=?, fees=? WHERE id =?"
            CURSOR.execute(sql, (name, fees,id))
            CONN.commit()
            print("Updated successfully")
        
        else:
            print("The student doesnt exists!")

    # DELETE
    @classmethod
    def delete_students(cls, id):
        sql = "SELECT COUNT(*) FROM students WHERE id=?"
        CURSOR.execute(sql, (id,))
        count_students = CURSOR.fetchone()[0]

        if count_students >0:
            sql = "DELETE FROM students WHERE id =?"
            CURSOR.execute(sql, (id, ))
            CONN.commit()
            print("DELETED successfully")
        
        else:
            print("The student doesnt exists!")





