from django.contrib import admin
from core.models import Cohort, Day, AgendaItem, GuestLecture, FieldTrip, Meme

# Register your models here.
admin.site.register(Cohort)
admin.site.register(Day)
admin.site.register(AgendaItem)
admin.site.register(GuestLecture)
admin.site.register(FieldTrip)
admin.site.register(Meme)
