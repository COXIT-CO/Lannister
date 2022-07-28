from django.contrib import admin

from .models import Bonus_request, Bonus_request_history, User

admin.site.register(User)
admin.site.register(Bonus_request)
admin.site.register(Bonus_request_history)
