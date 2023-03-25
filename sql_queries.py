import sqlite3

conn = sqlite3.connect("Artistc.db")
cursor = conn.cursor()
# Запитання 1. Інформація про скількох художників представлена у базі даних?
cursor.execute(''' SELECT * FROM artists ''')
data = cursor.fetchall()
#print(data)
print(len(data))    # data about 460 artists is given

# Запитання 2. Скільки жінок (Female) у базі?
cursor.execute(''' SELECT * FROM artists WHERE Gender == "Female" ''')
data = cursor.fetchall()
#print(data)
print(len(data))    # 63 women


# Запитання 3. Скільки людей у базі даних народилися до 1900 року?

# NUMBERS SHOULD BE WITHOUT QUOTES
cursor.execute(''' SELECT * FROM artists WHERE "Birth Year" < 1900''')  # query should be in a such format cursor.execute('''query''')
data = cursor.fetchall()
#print(data)
print(len(data))    # 122 people were born before 1900

# Запитання 4*. Як звати найстаршого художника?

cursor.execute(''' SELECT * FROM artists ORDER BY "Birth Year" ''')
# 1) ORDER BY column - order by from the lowest number to the highest,
# 2) ORDER BY column - order from the A to Z letters (Capital letters) and then by a to z letters (small letters) then by numbers and 
# foreign letters (ü ö ä)
data = cursor.fetchall()    # fetchall() - get all data
print(data)
print(data[0][1])   # Thomas Bewick is the oldest artist
print(data[0][4])   # he was born in 1753
print(data[-1][1], data[-1][4]) # The Youngest Artist - Harry Allen 1964 year

cursor.execute(''' SELECT * FROM artists ORDER BY Nationality ''')
data = cursor.fetchall()
print(data) # First nationality  - American, last -  Yugoslav

conn.commit()   # commit changes - conn.commit()
conn.close()    # close connection - conn.close()