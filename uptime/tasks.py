from celery.task import task
from models import *

@task()
def update_snapshots():
	for site in Site.objects.all():
		site.update_snapshot()
		# If it gets one we should send an email
