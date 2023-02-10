from django.contrib import admin

from . import models as m

# for i in [
#     m.Event,
#     m.EventType,
#     m.EventLevel,
#     m.Plan,
#     m.Shedule,
#     m.Month,
#
#
#           ]:
#     admin.site.register(i)
for i in dir(m):
    i = getattr(m, i)

    if hasattr(i, 'id') and issubclass(i, m.models.Model):
        admin.site.register(i)
