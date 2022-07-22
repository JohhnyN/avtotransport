import sqlite3

con = sqlite3.connect(r'D:\avtotransport\avtotransport\db.sqlite3')
cursor = con.cursor()
print(cursor)
cursor.execute("""
            UPDATE avto_automobile
            SET allowed=0
            WHERE limitation < CURRENT_DATE
            """)
rows = cursor.fetchall()
con.close()



UPDATE avto_automobile
SET allowed=0
WHERE limitation < CURRENT_DATE