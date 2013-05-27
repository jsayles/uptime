from django.db import models
from django.utils import timezone

import urllib

class SiteManager(models.Manager):
	def fake(self):
		return

class Site(models.Model):
	objects = SiteManager()
	
	name = models.CharField(max_length = 128, blank = True)
	url = models.URLField(blank=True, null=True)
	
	def __unicode__(self):
		return '%s: %s' % (self.name, self.url)

	def update_snapshot(self):
		success = False
		last_snapshot = Snapshot.objects.filter(site=self.id).order_by('-timestamp')[0:][0]
		data = None
		net = urllib.urlopen(self.url)
		try:
			data = net.read()
			success = True
		finally:
			net.close()
		if not success:
			print('%s: %s') % (self.name, 'Failed to download')
		if (not last_snapshot or last_snapshot.data != data):
			new_snapshot = Snapshot.objects.create(site=self, data=data, success=success)
			print('%s: %s') % (self.name, 'Found new data')
		else:
			print('%s: %s') % (self.name, 'No change')

class Snapshot (models.Model):
	site = models.ForeignKey(Site)
	timestamp = models.DateTimeField(auto_now_add=True, default=timezone.now())
	data = models.TextField(blank=True, null=True)
	success = models.NullBooleanField(blank=False, null=False, default=False)
	
	def __unicode__(self):
		return '%s: %s = %s' % (self.timestamp, self.site.name, self.success)
	
