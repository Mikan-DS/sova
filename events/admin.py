from django.contrib import admin

from . import models as m

for i in [m.Event, m.EventType, m.EventLevel, m.Plan, m.Result]:
    admin.site.register(i)
