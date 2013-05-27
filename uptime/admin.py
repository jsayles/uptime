from django.contrib import admin

from models import *

# Register the objects with the admin interface
admin.site.register(Site)

class StyledAdmin(admin.ModelAdmin):
	class Media:
		css = { "all": ('local-admin.css', )}

class SnapshotAdmin(StyledAdmin):
	list_display = ('timestamp', 'site', 'success',)
	search_fields = ('site',)
admin.site.register(Snapshot, SnapshotAdmin)

