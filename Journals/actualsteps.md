1. Import TaskTales to TaskTalesDeployment on Github.
2. Create sarinawu/dev branch for deployment testing.
3. Run `python manage.py collectstatic` to generate staticfiles folder.
4. download and run cli
   #Below are code changes for backend deploy
5. Make sure to have a root route that returns success. (I defined the view in project-level urls.py)
   def project_root_view(request):
   return HttpResponse("This is the project root view.")
6.
