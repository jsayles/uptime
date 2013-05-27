from django.core.management.base import NoArgsCommand, CommandError

from uptime import tasks

class Command(NoArgsCommand):
   help = "Runs the billing calculator."

   requires_model_validation = True

   def handle_noargs(self, **options):
      tasks.update_snapshots()	
