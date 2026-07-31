# 📝 Python Todo App (CRUD with MySQL)

## 📌 Project Overview

The Python Todo App is a simple command-line application that allows users to manage their daily tasks. It performs CRUD (Create, Read, Update, Delete) operations and stores task data permanently in a MySQL database.

## 🚀 Features

* ➕ Add a new task
* 📋 View all tasks
* ✏️ Update an existing task
* 🗑️ Delete a task
* 💾 Store tasks in a MySQL database
* 🔄 Menu-driven console interface

## 🛠️ Technologies Used

* Python 3
* MySQL
* mysql-connector-python

## 📂 Project Structure

```
Todo_App/
│── todo.py
│── README.md
└── todo_db.sql
```

## ⚙️ Prerequisites

* Python 3.x
* MySQL Server
* mysql-connector-python package

Install the required package:

```bash
pip install mysql-connector-python
```

## 🗄️ Database Setup

Create the database and table:

```sql
CREATE DATABASE todo_db;

USE todo_db;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(255) NOT NULL
);
```

Update the database connection details in `todo.py`:

```python
host="localhost"
user="root"
password="your_password"
database="todo_db"
```

## ▶️ How to Run

1. Start the MySQL server.
2. Create the database and table.
3. Update the database credentials in the Python file.
4. Run the application:

```bash
python todo.py
```

## 📸 Sample Menu

```
===== TODO APP =====
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
```

## 📖 CRUD Operations

* **Create** – Add a new task.
* **Read** – Display all tasks.
* **Update** – Modify an existing task.
* **Delete** – Remove a task from the database.

## 🎯 Future Enhancements

* User authentication
* Task priority levels
* Due dates and reminders
* Search and filter tasks
* Graphical User Interface (GUI)
* Web-based version using Flask or Django

## 👩‍💻 Author

**Sowmiya Sureshkannan**

---

⭐ If you found this project useful, consider giving it a star on GitHub!

