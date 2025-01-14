from django.contrib import admin
from .models import User, Book, Member, Borrow

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Borrow)