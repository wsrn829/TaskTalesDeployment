# TaskTales (Solo Project - My First Full Stack App)

---

Deployment Steps of Django App (On-Going)

1. Prepare Your Django App:

- Ensure that your Django app is ready for deployment by verifying that all dependencies are listed in the requirements.txt file.
- Remove any unnecessary development-specific settings and configurations from your Django project settings.

2. Configure Database and Media Files:

- Set up your production database and configure the appropriate settings in the Django project.
- Configure media and static file handling for production using a reliable storage solution, such as Amazon S3 or a similar service.

3. Secure Your Django App:

- Update the Django SECRET_KEY for security reasons.
- Disable the debug mode in your Django settings for production environments.
- Choose a Web Server:

4. Select a web server such as Nginx or Apache to serve your Django application.

- Configure the web server to forward requests to the Gunicorn or uWSGI application server.

5. Set Up Gunicorn or uWSGI:

- Install and configure Gunicorn or uWSGI to serve your Django app.
- Use a process manager like Supervisor to ensure the continuous operation of the application server.

6. Configure Domain and SSL/TLS:

- Set up a domain for your Django app and configure DNS settings.
- Implement SSL/TLS for secure communication by obtaining and configuring an SSL certificate from a trusted certificate authority.

7. Include HTML and CSS Files:

- Ensure that all HTML and CSS files for your frontend are included in the appropriate directories within your Django project.

8. Collect Static Files:
   Run the collectstatic management command to gather all static files (including CSS and JavaScript) into a single directory.

   `python manage.py collectstatic`

9. Serve Static Files:

- Configure your production web server to serve static files directly or use a dedicated service like Amazon S3 or a CDN for improved performance.

10. Automate Deployment with Fabric or Ansible:

- Streamline the deployment process by creating automation scripts using tools like Fabric or Ansible.

11. Implement Continuous Integration/Continuous Deployment (CI/CD):

- Integrate your Django app with a CI/CD system, such as Jenkins or GitLab CI, to automate testing and deployment processes.

12. Monitor and Scale:

- Implement monitoring tools to keep track of your Django app's performance and identify potential issues.
- Configure automatic scaling mechanisms to handle increased traffic efficiently.

13. Backup and Recovery Planning:

- Implement regular backups of your production database and critical files.
- Develop a comprehensive recovery plan to quickly restore your Django app in case of any unforeseen issues.

14. Update Environment Variables:

- Manage sensitive information and configuration settings using environment variables.

15. Documentation:

- Maintain clear and up-to-date documentation for your deployment process, making it easier for future updates or troubleshooting.

---

This is a Django application implemented with Python, utilizing Django's authentication system and a built-in SQLite database.
The front end is developed using HTML and CSS.

The following steps and terminal commands guide you through creating a new virtual environment
and installing the dependencies for Django and software development.

1.  Change the directory to the desired location where you want to clone the repository:

    cd replace/with/path/to/your/local/directory

2.  Now, you can use the git clone command to clone the repository:

    git clone 'replace_with_actual_repository_url'

3.  Create a new virtual environment in the repository directory for the project:

    python -m venv venv

4.  Activate the virtual environment (on Unix or MacOS):

    source venv/bin/activate

5.  Activate the virtual environment (on Windows):

    .\venv\Scripts\activate

6.  Upgrade pip (optional, but recommended):

    pip install --upgrade pip

7.  Install Django:

    pip install Django

8.  Install black:

    pip install black

9.  Install flake8:

    pip install flake8

10. Install djlint:

    pip install djlint

11. Deactivate your virtual environment:

    deactivate

12. Activate your virtual environment:

    python -m venv venv

13. Use pip freeze to generate a requirements.txt file:

    pip freeze > requirements.txt

14. Run migrations to apply model changes to the database:

    python manage.py makemigrations

15. Apply migrations to update the database schema:

    python manage.py migrate

16. Run the Django development server:

    python manage.py runserver

17. Starting the Development Server:

    The development server has been initiated, and you can access your application at http://127.0.0.1:8000/.

18. Quitting the Server:

    To stop the server, use CONTROL-C. If you need to restart it, use the command mentioned in step 16 above.

---

This Django application has a Django project named 'tracker', which includes three Django apps named 'accounts', 'projects', and 'tasks'.

The following is the implementation process. In the repository directory:

1. Create a Django project named tracker so that the manage.py file is in the top directory;
2. Create a Django app named accounts and install it in the tracker Django project in the INSTALLED_APPS list;
3. Create a Django app named projects and install it in the tracker Django project in the INSTALLED_APPS list;
4. Create a Django app named tasks and install it in the tracker Django project in the INSTALLED_APPS list;
5. Run the migrations;
6. Create a super user.
