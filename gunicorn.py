import os

chdir = "."
bind = "0.0.0.0:8001"
access_logfile = "./logs/access.logs"
error_logfile = "./logs/errors.logs"
log_level = "info"
proc_name = "gunicorn %s" % os.getpid()
backlog = 2048

worker_class = "eventlet"
worker_connections = 2048
max_requests = 0