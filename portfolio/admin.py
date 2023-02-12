from django.contrib import admin

from . import models as m


for i in dir(m):
    i = getattr(m, i)

    try:
        # print(i.__module__, __name__)
        if hasattr(i, 'id') and issubclass(i, m.models.Model) and i.__module__==__name__.replace('.admin', '.models'):
            admin.site.register(i)
    except:
        pass