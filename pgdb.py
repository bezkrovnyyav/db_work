import psycopg2

con = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="", 
  host="127.0.0.1", 
  port="5432"
)

print("Database opened successfully")
cur = con.cursor()  

cur.execute("SELECT admission, name, age, course, department from STUDENT")
  
rows = cur.fetchall()
print(rows)
'''
for row in rows:  
   print("ADMISSION =", row[0])
   print("NAME =", row[1])
   print("AGE =", row[2])
   print("COURSE =", row[3])
   print("DEPARTMENT =", row[4], "\n")
'''
print("Operation done successfully")  
con.close()  