# bind = "0.0.0.0:8000"
# gunicorn.conf.py
# gunicorn.conf.py
import os

bind = "0.0.0.0:" + os.environ.get("PORT", "8000")
workers = 3
reload = True
# module = "TaskTalesDeployment.wsgi:application"
module = "tracker.wsgi:application"

