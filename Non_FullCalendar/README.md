# [Flask-ToDoList-Backend]

Install the necessary tools

```python
pip install -r requirements.txt
```

# [Project - Outline]


    └── project
        ├── __init__.py       # setup the app
        ├── auth.py           # the auth routes for the app
        ├── database.db       # the database(MySQLite)
        ├── main.py           # the non-auth routes for the app
        ├── models.py         # the user model
        ├── views.py          # function
        └── templates       
            ├── main.html                       # show the main(home) page
            ├── login.html                      # show the login form
            ├── task_list.html                  # show the task_list form
            ├── task_confirm_delete.html        # show the task_confirm_delete form(remove schedule)
            ├── task_list.html                  # show the task_list form(add schedule)
            ├── task_form.html                  # show the task_form form(look at the schedule list)
            └── task_update.html                # show the sign_up form(update schedule)
        └── static
            ├── style.css     # cascading style sheets

SQLite 데이터베이스와 Python의 SQLAlchemy 패키지를 사용해서 TCP 연결을 보장
