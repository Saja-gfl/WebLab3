from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name="books.index"),
    path('books/', views.book_list, name='book_list'),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links_page, name='links_page'),
    path('html5/formatting/', views.formatting_page, name='formatting_page'),
    path('html5/listing/', views.listing_page, name='listing_page'),
    path('html5/tables/', views.tables_page, name='tables_page'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('books/simple/query', views.simple_query, name='simple_query'),
    path('books/complex/query', views.complex_query, name='complex_query'),
    path('books/task1/', views.task1, name='task1'),
    path('books/task2/', views.task2, name='task2'),
    path('books/task3/', views.task3, name='task3'),
    path('books/task4/', views.task4, name='task4'),
    path('books/task5/', views.task5, name='task5'),
    path('books/listbooks', views.list_books, name='list_books'),
    path('books/addbook', views.add_book, name='add_book'),
    path('books/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('books/deletebook/<int:id>', views.delete_book, name='delete_book'),
    path('students/', views.student_list, name='student_list'),
    path('add_student/', views.add_student, name='add_student'),
    path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),  

    # path('search/', views.search_page, name='search_page'),
]

urlpatterns += [
    path('html5/listing/', views.listing_page, name='listing_page'),
    path('html5/tables/', views.tables_page, name='tables_page'),
    path('search/', views.search_page, name='search_page'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('books/complex/query', views.complex_query, name='complex_query'),
#     path('books/lab9_part1/addbook', views.add_book, name='add_book'),
#     path('books/lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
#     path('books/lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
]



