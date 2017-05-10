"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import  url, include
from django.contrib import admin
from user.views import login_view,reg_view,regok_view,loginok_view
# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]

urlpatterns = [
        #"",
    url('^login/$', login_view),
    url('^reg/$', reg_view),
    url('^regok/$', regok_view),
    url('^loginok/$', loginok_view),
]
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns  
      

      
#urlpatterns += staticfiles_urlpatterns()  

#!/usr/bin/env python
# 
# import MySQLdb
# 
# print "Content-Type: text/html\n"
# print "<html><head><title>Books</title></head>"
# print "<body>"
# print "<h1>Books</h1>"
# print "<ul>"
# 
# connection = MySQLdb.connect(user='me', passwd='letmein', db='my_db')
# cursor = connection.cursor()
# cursor.execute("SELECT name FROM books ORDER BY pub_date DESC LIMIT 10")
# 
# for row in cursor.fetchall():
#     print "<li>%s</li>" % row[0]
# 
# print "</ul>"
# print "</body></html>"
# 
# connection.close()

# models.py (the database tables)
# 
# from django.db import models
# 
# class Book(models.Model):
#     name = models.CharField(max_length=50)
#     pub_date = models.DateField()
# 
# 
# # views.py (the business logic)
# 
# from django.shortcuts import render_to_response
# from models import Book
# 
# def latest_books(request):
#     book_list = Book.objects.order_by('-pub_date')[:10]
#     return render_to_response('latest_books.html', {'book_list': book_list})
# 
# 
# # urls.py (the URL configuration)
# 
# from django.conf.urls.defaults import *
# import views
# 
# urlpatterns = patterns('',
#     (r'^latest/$', views.latest_books),
# )
# 
# 
# # latest_books.html (the template)
# 
# <html><head><title>Books</title></head>
# <body>
# <h1>Books</h1>
# <ul>
# {% for book in book_list %}
# <li>{{ book.name }}</li>
# {% endfor %}
# </ul>
# </body></html>