import mysql.connector
import tkinter as tk

def registerUser(username,password,mydb):
    print("a")
    sql_string = "INSERT INTO user (username,password) VALUES (%s,%s)"
    values = (username,password)
    cursor = mydb.cursor()

    try:
        cursor.execute(sql_string,values)

        mydb.commit()

        print("Operation Successfull")
    except mysql.connector.Error as error:
        print({error})

    cursor.close()
    return
def loginUser(username,password,mydb):
    sql_string = "SELECT * FROM user WHERE username = %s AND password = %s"
    values = (username,password)
    cursor = mydb.cursor()

    cursor.execute(sql_string,values)
    result = cursor.fetchone()

    if result:
        print("Login successfull")
    else:
        print("Invalid user")

    cursor.close()
    return
if __name__ == '__main__':
    print("b")
    mydb = mysql.connector.connect(
        host= "localhost",
        user= "root",
        password="password",
        database= "userauth"
    )

    window = tk.Tk()
    window.title("User Auth Python")

    tk.Label(window,text="Username").grid(row=0,column=0,sticky=tk.W)
    username_entry = tk.Entry(window)
    username_entry.grid(row=0,column=1)

    tk.Label(window,text="Password").grid(row=1,column=0,sticky=tk.W)
    password_entry = tk.Entry(window)
    password_entry.grid(row=1,column=1)

    tk.Button(window,text="Sign In",command= lambda : loginUser(username_entry.get(),password_entry.get(),mydb)).grid(row=2,column=0,sticky=tk.W)

    tk.Button(window,text="Sign Up",command= lambda : registerUser(username_entry.get(),password_entry.get(),mydb)).grid(row=2,column=1,sticky=tk.W)


    window.mainloop()
    mydb.close()
