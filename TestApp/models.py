from django.db import models


# Create your models here.
class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'User_table'


class BookCategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    class Meta:
        db_table = 'Book_category_table'


class BookModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=400)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(BookCategoryModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Media')
    price = models.CharField(max_length=50)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book_table'


class ReviewModel(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book_id = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    rating = models.TextField()


class CartModel(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    book_id = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'cart_table'
