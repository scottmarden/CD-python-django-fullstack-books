# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Book

# Create your views here.
def index(request):
	#Adding data to books model in python shell
	books = Book.objects.all()
	for book in books:
		print book.title, book.author, book.published_date, book.category, book.in_print
	return render(request, 'book_app/index.html')
