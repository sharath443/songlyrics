import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@123",
  database="lyrics"
)
print("**Song - Lyrics**")
print('-------------------')
curr = mydb.cursor()
curr.execute("SELECT songid,sname FROM songlyrics order by songid asc")
myresult=curr.fetchall()
for x in myresult:
    print(x[0],x[1])
print('-----------------------------------------')
ssong = input("ENTER UR CHOICE: ")
print('-----------------------------------------')
print('Here you go.........\n')
curr.execute("SELECT lyrics FROM songlyrics WHERE songid ="+ ssong)
result = curr.fetchone()
for x in result:
    print(x)



