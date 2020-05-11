from django.contrib import admin
from library_app.models import Books, Student, BookUser
# Register your models here.

admin.site.register(Books)
admin.site.register(Student)
admin.site.register(BookUser)