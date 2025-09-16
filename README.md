Name: Shelia Vellicita
Student ID: 2406453606
Class: PBD KI

Deployment link: https://shelia-vellicita-penaltee.pbp.cs.ui.ac.id/

1. Explain how you implemented the checklist above step-by-step (not just by following the tutorial).

My first step was to create and set up the Django project in a new GitHub repository:

I. Firstly, I created a new directory/folder on my laptop with my application name, which is "penaltee".

II. I opened Windows Powershell, typed 'cd', then dragged my penaltee folder to the Windows Powershell so it would change the directory into the penaltee directory. To initialise my Django project, I created a virtual enviroment by typing 'python -m venv env' so the application is independent meaning that it will not clash with other versions on the same computer. This virtual environment can be activated by typing the command 'env\Scripts\activate' and deactivated using 'deactivate'. Since I needed to set up the Django project, I activated the virtual environment in the Windows Powershell.

III. In the penaltee directory, I made a requirements.txt file filled with some dependencies. Then, I installed the dependencies by using the command 'pip install -r requirements.txt' in the Windows Powershell. Finally, I created the Django project using the command 'django-admin startproject penaltee .'

IV. For the next step, I opened the penaltee folder in Visual Studio Code to create a ".env" file for local development with 'PRODUCTION=False' and '.env.prod' file for production that includes PostgreSQL credentials (DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, SCHEMA) and PRODUCTION=True. Then, I modified settings.py to load these environment variables, set up ALLOWED_HOSTS for access control, added a PRODUCTION flag to switch between environments, and updated the database configuration.

V. Then, I ran the server by typing the migration command 'python manage.py migrate' in the Windows Powershell to set up the database. After the migration finished, I started the Django development server using the command 'python manage.py runserver'. Finally, I opened http://localhost:8000 in the browser to check whether it succeeded or not.

VI. After that, I created a GitHub repository named "penaltee" with public visibility. Then, I initialised the penaltee directory as a git repository using the command 'git init' in the Windows Powershell, which created the ".git" folder for tracking changes. After that, I added a ".gitignore" file to exclude unnecessary or sensitive files from version control. Next, I connected the local repository to the GitHub repository with the remote URL using 'git remote add origin <URL link>', created a main branch named master using 'git branch -M master', and performed 'git add .', 'git commit -m "Initial project"', 'git push origin master' which are commands to add, commit, add push so the project is uploaded to GitHub.

VII. Then, I logged in to PWS website to create a project named penaltee. In the project's Environment tab, I opened the Raw Editor, put the contents of my '.env.prod' file. Then, I updated my Django settings.py to include the PWS deployment URL in ALLOWED_HOSTS. I used the add, commit, push again to save the changes to GitHub. When I pushed to PWS, there is a window opened for us to fill the username and password from the project credentials. Finally, when my project's deployment status was 'Running', I can access my project on my deployment URL.


After finished setting up my Django project, I continued to create the inside of the project and decorated the template:

I. I started by creating a new application "main" inside the penaltee project using the command 'python manage.py startapp main'. Then, I added 'main' to the INSTALLED_APPS in the settings.py inside the penaltee directory to register the main application on the project.

II. Next, I made a new directory named "templates" inside the main application directory. Then, inside the templates directory, I created "main.html" file and filled the file with html codes to decorate the display.

III. After that, I modified the models.py inside the main application directory. I added the required attributes with their type from the assignment checklist. Then, I did migrations using the command 'python manage.py makemigrations' then 'python manage.py migrate'.

IV. The next step was to connect the view to the template. At the very top of the code in views.py inside the main application directory, I imported the render function from django.shortcuts and I created the "show_main" function, which takes a request as input, prepares a context dictionary containing values for the app_name, name, and class. Then I returned to the main.html to put the template variables.

V. Then, I needed to configure the URL routing. I created "urls.py" inside the main application directory where I typed the code to first import the path function from django.urls and the show_main view then define a URL pattern that mapped to the show_main function by setting app_name = 'main'. Next, I opened the urls.py inside the penaltee directory and typed the code to import the include function from django.urls then add the following URL route in the urlpatterns variable to direct requests to the main view.

VI. I ran the Django project using the command 'python manage.py runserver' then I viewed the page by opening http://localhost:8000

VII. Finally, I save all changes to GitHub and PWS by add, commit, and push to both origin master and pws master. Hence, my Django project was completed with the deployment url: https://shelia-vellicita-penaltee.pbp.cs.ui.ac.id/


2. Create a diagram showing the client request to the Django-based web application and its response, and explain the relationship between urls.py, views.py, models.py, and the HTML file in the diagram.
![alt text](diagram_num2.jpg)
The diagram shows how a client request is handled in Django. First, when the user makes a URL request, then the urls.py checks the URL and forwards it to the right view in views.py. The view now will interact with the model (models.py) to read then write the necessary data from the database. Once the data is ready, the view returns the user an appropriate template from the HTML file which formats the retrieved data for display. Finally, Django gives the rendered HTML as an HTTP response to the client's browser.


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



Assignment 3


1. Why do we need data delivery in implementing a platform?

Data delivery is the process of transferring data from one place to another. It is important in implementing a platform because it ensures that the right data gets to the right user in time. Platforms need real-time data delivery, timely updates, and efficient backend data retrieval. Those features cannot function without implementing a data delivery system. Data delivery also connects the frontend or user interface with the backend or database which is very crucial to create a dynamic and interactive platform. Therefore, data delivery acts like a backbone of functionality, performance, and user experience.


2. In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?

Based on readability, JSON is easier to understand and work with the data format as it has a clearer code structure which makes it easier to read, debug, and spot errors. The reason is because JSON uses key-value syntax meanwhile XML uses nested tags that can be hard to scan at first glance.
JSON is more lightweight, making it ideal for web and mobile applications. In addition, its native compatibility with JavaScript and modern APIs boosts its popularity. On the other hand, XML is more complex and less suited for modern data exchange even though it is still useful for certain legacy systems and document-based structures.


3. What is the purpose of the is_valid() method in Django forms, and why do we need it?

The is_valid() method in Django forms is used to check whether the data submitted through the form is valid. This means that it will ensure the correct data type is submitted for each input and every required input fields are filled. When it is called, it will perform a comprehensive validation process on the submitted data. Therefore, it prevents processing or saving invalid data, automatically gives feedback to users when the inputs are incorrect, and ensure that the application works with safe and clean data.


4. Why do we need a csrf_token when making forms in Django? What can happen if we don't include a csrf_token in a Django form? How can this be exploited by an attacker?

The csrf_token needs to be included in forms so the server can verify that the request is coming from the authenticated user and not from a malicious source. If we don't use csrf_token, it can lead to serious security issues. The server won't be able to distinguish between valid requests and forged requests, so it might process the malicious request. An attacker can send a link to the authenticated user to submit an information, since there is no csrf_token, it will not match with the token generated for the user at the starting of the session, so it will throw a 403 Forbidden error page. By including a csrf_token, the server can only accept request with a valid token, preventing attackers from tricking users into submitting unauthorized actions.


5. Explain how you implemented the checklist above step-by-step (not just following the tutorial).

Firstly, I created a base template for the website as a consistent skeleton across all pages by adding a 'templates' directory in the main project folder and creating a 'base.html' file inside it that contains the essential HTML structure. Hence, it helps maintain the visual throughout the website. Next, I updated the template settings to include the path to the templates folder. 

Then, I created a form to add a new product by making a new file 'forms.py' in the main directory that will receive new product data. The data are models that have been made from the previous assignment, which are name, price, description, thumbnail, category, is_featured, specifying the fields of product model that will be used in the form. Then, I opened views.py to update and add some functions, which are modifying show_main so it can fetch all product objects that are stored in the database, making create_product to generate a form that can automatically add product data when submitted, and show_product to fetch product object based on its primary key (product_id) and if no object is found, a 404 page is returned. Then, I added URL paths to the urlpatterns in the urls.py file. 

After that, I updated the code in the main.html and inside the content block to display the product data along with the buttons "Add Product" and "Details". Next, I created an input form and product details page under the main/templates directory. Then, I added my PWS project URL entry to CSRF_TRUSTED_ORIGINS inside the settings.py in the root project directory. 

Next, I turned my Django data into APIs using XML and JSON. In views.py, I imported HttpResponse and serializers, created a show_xml function that retrieves all product objects, serializes them to XML, and returns the data with the proper content type. I added a URL pattern for that function in the urls.py so the XML data can be accessed at /xml/. Then, I created a similar show_json function to serialize and return the product data in JSON format and added its URL pattern at /json/ in urls.py.

After that, I made two functions, show_xml_by_id and show_json_by_id, which accepts a product_id to return specific product data in XML or JSON. I used try-except blocks to handle cases where the ID doesn't exist by returning a 404 response. Then, I added URL petterns with ID parameters to access those endpoints. Finally, I ran the Django server to test the XML and JSON endpoints, both for all data and individual product items by the ID.

Then, I did add, commit, push for all changes. For the last checklist, I put those link into Postman to check the results.


6. Do you have any feedback for the teaching assistants for Tutorial 2?

Teaching assistants were helpful but there were a lot of typos in the code for Tutorial 2 which created many errors and delays. However, they are still very nice and good. :D

Postman Screenshots:
<img width="1920" height="1026" alt="Screenshot (469)" src="https://github.com/user-attachments/assets/de0dff0f-c439-4d03-86ec-8a3aad207f98" />
<img width="1920" height="1038" alt="Screenshot (472)" src="https://github.com/user-attachments/assets/cb8bcc6b-a2c1-4a88-acf3-7e3cc983ec05" />
<img width="1920" height="1026" alt="Screenshot (471)" src="https://github.com/user-attachments/assets/f13d8b84-fec8-4a44-a802-848daac00152" />
<img width="1920" height="1031" alt="Screenshot (470)" src="https://github.com/user-attachments/assets/9d08e090-0e3d-40b7-92f8-8009a7645d47" />
