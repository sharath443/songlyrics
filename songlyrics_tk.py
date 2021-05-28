import tkinter as tk
frame = tk.Tk()
frame.geometry('900x600')
frame.title("songlyrics")
title = tk.Label(frame,bg="silver",text = "Select Song for lyrics",font =('times new roman',30,'bold'))
title.pack(side=tk.TOP,fill=tk.X)
listbox = tk.Listbox(frame,bg= "light blue")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@123",
  database="lyrics"
)
curr = mydb.cursor()
curr.execute("SELECT songid,sname FROM songlyrics order by songid asc")
myresult=curr.fetchall()
for x in myresult:
    listbox.insert(x[0],x[1])
def displaylyrics(event):
    action=event.widget
    Select = action.curselection()
    curr.execute("SELECT lyrics FROM songlyrics WHERE songid ="+str(Select[0]+1))
    result = curr.fetchall()
    for x in result:
        lable.configure(text =x[0])
listbox.bind("<<ListboxSelect>>",displaylyrics)
listbox.pack(side=tk.LEFT,fill=tk.Y)
lable= tk.Label(frame,bg = "white",text ="here we go.......")
lable.pack(side=tk.TOP,fill="both")
frame.mainloop()
