# cc105_MidtermProject

This is a simple task management web application built with Django. It allows you to create, edit, and delete tasks, and track their due dates and status.

## Features

* Create new tasks with titles, descriptions, and due dates.
* Edit existing tasks.
* Delete tasks.
* View tasks in a list format.
* Sort tasks by due date or status.
* Filter tasks by status.
* Search for tasks by title or description.



## Installation

1. Clone the repository:
 ```bash
   git clone <repository_url>

2. Create a virtual environment:
    #Open terminal -> 
        ctrl + ~
    #Install Pipenv (if you don't have it already)
        pip install pipenv

    # if already installed, run either command below to open virtual environment:
        python3 -m venv venv
        or
        pipenv shell
    #i prefer pipenv shell as it is much smoother in my experience 

3. Navigate to the project directory:
    cd <project_directory>

    #use "DIR" command to navigate 
    #locate manage.py file
        cd .\task_manager\task_manager\ 


4. Migrate Models
    #Run this 2 commands to migrate models
    1. manage.py makemigrations
    2. manage.py migrate

5. launch/run server using manage.py
    manage.py runserver
