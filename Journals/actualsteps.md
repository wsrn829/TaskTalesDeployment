1. Import TaskTales to TaskTalesDeployment on Github.
2. Create sarinawu/dev branch for deployment testing.
3. Run `python manage.py collectstatic` to generate staticfiles folder.
4. download and run cli
   #Below are code changes for backend deploy
5. Make sure to have a root route that returns success. (I defined the view in project-level urls.py)
   def project_root_view(request):
   return HttpResponse("This is the project root view.")
6. Hebrew Install
   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
7. `(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/s/.zprofile`
8. `eval "$(/opt/homebrew/bin/brew shellenv)"`
9. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
10. `brew tap heroku/brew && brew install heroku`
11. `curl https://cli-assets.heroku.com/install.sh | sh`
12. `heroku login`
13. Deploy an Application:

- If you have a web application that you want to deploy on Heroku, follow these general steps:
- Ensure your application has a Procfile specifying how to run your application. `touch Procfile`
- In above file: `web: gunicorn yourapp.wsgi`
- Commit your code to a version control system like Git.

14. `heroku git:remote -a tasktales`
15. `git add .`
16. `git commit -am "make it better"`
17. `git push heroku main`
