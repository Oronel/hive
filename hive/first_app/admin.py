from django.contrib import admin
from first_app.models import Feed, User
# Register your models here.

admin.site.register(User)
admin.site.register(Feed)