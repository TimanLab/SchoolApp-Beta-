# bustrack/admin.py

from django.contrib import admin
from .models import Parent, BusMileage, Exclusion, Operator, Bus, BusTrack, Feedback, PopRegister, Child, BusStop

admin.site.register(Parent)
admin.site.register(BusMileage)
admin.site.register(Exclusion)
admin.site.register(Operator)
admin.site.register(Bus)
admin.site.register(BusTrack)
admin.site.register(Feedback)
admin.site.register(PopRegister)
admin.site.register(Child)
admin.site.register(BusStop)
