from django.contrib import admin
from TestApp.models import *

# Register your models here.
admin.site.register(UserModel)
admin.site.register(BookCategoryModel)
admin.site.register(BookModel)
admin.site.register(ReviewModel)
admin.site.register(CartModel)
