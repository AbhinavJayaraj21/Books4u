from decimal import Decimal

from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse

from TestApp.models import *


# Create your views here.
def home(request):
    data = BookModel.objects.all()
    category = BookCategoryModel.objects.all()
    if request.method == 'POST':
        value = request.POST.get('search')
        price = request.POST.get('sort')
        cat = request.POST.get('category')
        if value:
            data = data.filter(Q(title__icontains=value))
            # return render(request, 'home.html', {'data': data1})
        if price == 'lowest':
            data = data.order_by('price')
            # return render(request, 'home.html', {'data': data})
        if price == 'highest':
            data = data.order_by('-price')
            # return render(request, 'home.html', {'data': data})
        if cat:
            data = data.filter(category__id=cat)
            # return render(request, 'home.html', {'data': data})

    return render(request, 'home.html', {'data': data, 'category': category})


def views(request, id):
    datas = ReviewModel.objects.filter(book_id=id)
    data = BookModel.objects.filter(id=id)
    return render(request, 'shop.html', {'data': data, 'datas': datas})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = UserModel.objects.filter(name=username, password=password)
        if user:
            request.session['user'] = username
            return redirect('/')
        else:
            return redirect('/login')
    return render(request, 'login.html')


def add_to_cart(request):
    if 'user' in request.session:
        print('add to_cart session')
        if request.method == 'POST':
            user_id = request.session.get('user')
            print(user_id)
            book_id = request.POST.get('book_id')
            quantity = request.POST.get('Quantity')

            user = UserModel.objects.get(name=user_id)
            book = BookModel.objects.get(id=book_id)

            cart_item = CartModel(user_id=user, book_id=book, quantity=quantity)
            cart_item.save()
            print(cart_item)
            return redirect('/add')
    return redirect('/')


def cart(request):
    if 'user' in request.session:
        print(request.session['user'])
        user_id = request.session['user']
        cart_items = CartModel.objects.filter(user_id__name=user_id)
        for item in cart_items:
            item.total_price = item.quantity * int(item.book_id.price)
        return render(request, 'cart.html', {'book': cart_items})

    return redirect('/login')


def shopping(request):
    if 'user' in request.session:
        user = request.session['user']
        book_id = request.POST.get('book_id')
        print(book_id)
        data = BookModel.objects.filter(id=book_id)
        return render(request, 'buy.html', {'data': data})
    else:
        return redirect('/login')


def add_review(request):
    if 'user' in request.session:
        if request.method == 'POST':
            review_text = request.POST.get('review')
            book_id = request.POST.get('book_id')
            print(book_id)
            user = request.session['user']
            user_instance = UserModel.objects.get(author=user)
            new_review = ReviewModel()
            new_review.book_id = book_id
            new_review.rating = review_text
            new_review.user = user_instance
            new_review.save()
            return HttpResponse('<h1>Review Added</h1>')
        else:
            return redirect('/')
    return redirect('/login')


def addbook(request):
    categories = BookCategoryModel.objects.all()
    if 'user' in request.session:
        if request.method == 'POST':
            book_name = request.POST.get('book_name')
            book_image = request.FILES['book_image']
            book_price = request.POST.get('book_price')
            book_description = request.POST.get('book_description')
            book_category = BookCategoryModel.objects.get(category=request.POST.get('book_category'))
            user_id = request.session['user']
            user_instance = UserModel.objects.get(name=user_id)

            new_book = BookModel()
            new_book.title = book_name
            new_book.image = book_image
            new_book.price = book_price
            new_book.description = book_description
            new_book.category = book_category
            new_book.author = user_instance
            new_book.save()
            return redirect('/')
        return render(request, 'add_book.html', {'category': categories})
    return redirect('/')


def profile(request):
    user_id = request.session['user']
    user = UserModel.objects.get(name=user_id)
    uploaded_books = BookModel.objects.filter(author=user)
    return render(request, 'userprofile.html', {'books': uploaded_books, 'user': [user]})


def delete_book(request, id):
    data = BookModel.objects.get(id=id)
    data.delete()
    return redirect('user_profile/')


def edit_book(request, id):
    datas = BookModel.objects.filter(id=id)
    if request.method == 'POST':
        d1 = BookModel.objects.get(id=id)
        d1.title = request.POST.get('title')
        d1.description = request.POST.get('desc')
        d1.price = request.POST.get('price')
        d1.save()
        return redirect('/')
    return render(request, 'update.html', {'data': datas})
