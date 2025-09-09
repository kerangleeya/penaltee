Name: Shelia Vellicita
Student ID: 2406453606
Class: PBD KI

1. Explain how you implemented the checklist above step-by-step (not just by following the tutorial).

My first step was to create and set up the Django project in a new GitHub repository:
I. Firstly, I created a new directory/folder on my laptop with my application name, which is "penaltee".
II. I opened Windows Powershell, typed 'cd', then dragged my penaltee folder to the Windows Powershell so it would change the directory into the penaltee directory. To initialise my django project, I created a virtual enviroment by typing 'python -m venv env' so the application is independent meaning that it will not clash with other versions on the same computer. This virtual environment can be activated by typing the command 'env\Scripts\activate' and deactivated using 'deactivate'. Since I needed to set up the django project, I activated the virtual environment in the Windows Powershell.
III. In the penaltee directory, I made a requirements.txt file filled with some dependencies. Then, I installed the dependencies by using the command 'pip install -r requirements.txt' in the Windows Powershell. Finally, I created the django project using the command 'django-admin startproject penaltee .'
IV. For the next step, I opened the penaltee folder in Visual Studio Code to create a ".env" file for local development with 'PRODUCTION=False' and '.env.prod' file for production that includes PostgreSQL credentials (DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, SCHEMA) and PRODUCTION=True. Then, I modified settings.py to load these environment variables, set up ALLOWED_HOSTS for access control, added a PRODUCTION flag to switch between environments, and updated the database configuration.
V. Then, I ran the server by typing the migration command 'python manage.py migrate' in the Windows Powershell to set up the database. After the migration finished, I started the django development server using the command 'python manage.py runserver'. Finally, I opened http://localhost:8000 in the browser to check whether it succeeded or not.
VI. After that, I created a GitHub repository named "penaltee" with public visibility. Then, I initialised the penaltee directory as a git repository using the command 'git init' in the Windows Powershell, which created the ".git" folder for tracking changes. After that, I added a ".gitignore" file to exclude unnecessary or sensitive files from version control. Next, I connected the local repository to the GitHub repository with the remote URL using 'git remote add origin <URL link>', created a main branch named master using 'git branch -M master', and performed 'git add .', 'git commit -m "Initial project"', 'git push origin master' which are commands to add, commit, add push so the project is uploaded to GitHub.
VII. Then, I logged in to PWS website to create a project named penaltee. In the project's Environment tab, I opened the Raw Editor, put the contents of my '.env.prod' file. Then, I updated my Django settings.py to include the PWS deployment URL in ALLOWED_HOSTS. I used the add, commit, push again to save the changes to GitHub. When I pushed to PWS, there is a window opened for us to fill the username and password from the project credentials. Finally, when my project's deployment status was 'Running', I can access my project on my deployment URL.

After finished setting up my Django project, I continued to create the inside of the project and decorated the template:
I. I started by creating a new application "main" inside the penaltee project using the command 'python manage.py startapp main'. Then, I added 'main' to the INSTALLED_APPS in the settings.py inside the penaltee directory to register the main application on the project.
II. Next, I made a new directory named "templates" inside the main application directory. Then, inside the templates directory, I created "main.html" file and filled the file with html codes to decorate the display.
III. After that, I modified the models.py inside the main application directory. I added the required attributes with their type from the assignment checklist. Then, I did migrations using the command 'python manage.py makemigrations' then 'python manage.py migrate'.
IV. The next step was to connect the view to the template. At the very top of the code in views.py inside the main application directory, I imported the render function from django.shortcuts and I created the "show_main" function, which takes a request as input, prepares a context dictionary containing values for the app_name, name, and class. Then I returned to the main.html to put the template variables.
V. Then, I needed to configure the URL routing. First, I created "urls.py" inside the penaltee directory

At the very top, I imported the render function from django.shortcuts, which is used to render HTML files along with the data passed into them. After that, I created the show_main function, which takes a request as input, prepares a context dictionary containing values for NPM, name, and class, and then returns the rendered main.html template together with this context.


2. Create a diagram showing the client request to the Django-based web application and its response, and explain the relationship between urls.py, views.py, models.py, and the HTML file in the diagram.




3. Explain the role of settings.py in a Django project!

The settings.py is like Django project's control center that determines how Django runs and integrates its different components. The settings.py contains all configurations for a Django project to manage the application's behaviour within development, testing, and production environments including database connection, middleware, and security settings such as ALLOWED_HOSTS. In addition, it also manages media file paths and templates. Therefore, settings.py is essential for ensuring the project runs consistently and securely across different environments.


4. How does database migration work in Django?

Migration is the process of propagating the model changes into the database schema without the need to delete or recreate the entire database. The three step guide to making model changes are:
I. Modifying the models in models.py
II. Run 'python manage.py makemigrations' to create migrations for those changes
III. Run 'python manage.py migrate' to apply the changes to the database. 
Makemigrations creates migration files based on the model changes, meanwhile migrate actually applies those migration files to the database, hence it updates the schema accordingly.


5. In your opinion, among all existing frameworks, why is the Django framework chosen as the starting point for learning software development?

From my perspective, Django framework has many built-in features so it is easier for beginners to understand the concepts first rather than worrying about complex setups. Django is a good development practice and provides clear documentations, making it very convenient to use while also helping developers monitor and manage their development progress.


6. Do you have any feedback for the teaching assistant for Tutorial 1 that you previously completed?

Overall, the tutorial sessions have been going really well! However, I did encounter some difficulties with certain instructions, particularly when an early step involved migrate/makemigrate then the second step is about creating unit tests, and when I attempted to run it, some errors occurred because it turned out that I needed to migrate it again. This difficulty may not be the same for all students, as I am still trying to get familiar with Django and web development. 
Aside from this, the tutorials are great and the teaching assistants are very helpful, responsive, and provide clear guidance! Thank you kakak-kakak! 