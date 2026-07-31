import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="todo_db"
)

cursor = conn.cursor()

# CREATE
def add_task():
    task = input("Enter Task: ")
    sql = "INSERT INTO tasks (task) VALUES (%s)"
    cursor.execute(sql, (task,))
    conn.commit()
    print("Task Added Successfully!")

# READ
def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    result = cursor.fetchall()

    if result:
        print("\nTodo List")
        print("-" * 25)
        for row in result:
            print(f"{row[0]}. {row[1]}")
    else:
        print("No Tasks Found!")

# UPDATE
def update_task():
    view_tasks()
    task_id = int(input("\nEnter Task ID to Update: "))
    new_task = input("Enter New Task: ")

    sql = "UPDATE tasks SET task=%s WHERE id=%s"
    cursor.execute(sql, (new_task, task_id))
    conn.commit()

    print("Task Updated Successfully!")

# DELETE
def delete_task():
    view_tasks()
    task_id = int(input("\nEnter Task ID to Delete: "))

    sql = "DELETE FROM tasks WHERE id=%s"
    cursor.execute(sql, (task_id,))
    conn.commit()

    print("Task Deleted Successfully!")

# Menu
while True:
    print("\n===== TODO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")

cursor.close()
conn.close()
