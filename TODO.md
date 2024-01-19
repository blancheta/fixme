# Fixme: Bash Memo

We are the company Bash Corporation LLC and we created a tool to help developers to keep and retrieve useful commands, they use daily.

So far, we were working with a Python developer. Yesterday, the developer won the lottery and left the project. We are now looking for someone else to complete the project.

As a Python expert, we are hiring you to fix bugs on the current application.

### To run the backend project
Open a new project by selecting backend
```
cd backend
python -m venv venv
source venv/bin/activate
python manage.py runserver
```

Open a new project by selecting frontend
```
cd frontend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/bashmemo/main.py
```

We identified the following bugs on the application.

#### [X] 1 - BACKEND: Site matching query does not exit
#### [X] 2 - BACKEND: No such column
#### [X] 3 - FRONTEND: Redirect to prod instead of local backend server
#### [X] 4 - FRONTEND: Raise error if local command does not exist, should return "Please install this program locally before using it"
#### [X] 5 - FRONTEND: Cannot save a command bookmarked
#### [X] 6 - FRONTEND: Cannot see a command bookmarked when search by keyword after creating it
"Command bookmark has not been created because of an error"
#### [X] 7 - Wait 2 seconds instead of 3 before opening webpage to login
#### [X] 8 - Simplify the storing of keywords from a list of dictionaries to a list of strings
#### [X] 9 - Fix "No command found" when searching for existing commands by keywords