from django.contrib import admin

# Register your models here.
from.models import *

admin.site.register(Guest)
admin.site.register(Post)

admin.site.register(Movie)
admin.site.register(Reservation)