import sqlite3

CONN = sqlite3.connect('students.sqlite')
CURSOR = CONN.cursor()