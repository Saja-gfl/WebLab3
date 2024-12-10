from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Book
from django.db.models import Q
from django.db.models import Avg, Max, Min, Sum
from django.shortcuts import get_object_or_404
## views.py
from django.shortcuts import render, redirect
from .models import Student, Address
from .forms import StudentForm, AddressForm




def task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'task1.html', {'books': books})


def list_books(request):
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'bookmodule/book_list.html', {'books': books})

def index(request):
    return render(request, "bookmodule/index.html")

def book_list(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'book_list.html', {'books': books})  

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

def links_page(request):
    return render(request, 'bookmodule/html5/links.html')

def formatting_page(request):
    return render(request, 'bookmodule/html5/formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/html5/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/html5/tables.html')

def search_page(request):
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]
def search_page(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # Filter books
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')

def simple_query(request):
    # Retrieve books whose titles contain the word 'and' (case-insensitive)
    mybooks = Book.objects.filter(title__icontains='and')  # Multiple objects
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')



def task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(editions__gt=2) & 
        (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        ~Q(editions__gt=2) & 
        ~Q(title__icontains='qu') & ~Q(author__icontains='qu')
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})



def task5(request):
    # Perform aggregation calculations
    books = Book.objects.all()
    context = {'message': 'Welcome to Task 5 - Dynamic Content!'}

    # Aggregation functions
    total_price = books.aggregate(Sum('price'))['price__sum']
    average_price = books.aggregate(Avg('price'))['price__avg']
    max_price = books.aggregate(Max('price'))['price__max']
    min_price = books.aggregate(Min('price'))['price__min']
    count = books.count()

    # Passing the results to the template
    return render(request, 'bookmodule/task5.html', {
        'total_price': total_price,
        'average_price': average_price,
        'max_price': max_price,
        'min_price': min_price,
        'count': count
    })

def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        isbn = request.POST['isbn']
        page_count = request.POST['page_count']
        language = request.POST['language']

        Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            isbn=isbn,
            page_count=page_count,
            language=language,
        )
        return redirect('list_books')

    return render(request, 'bookmodule/addbook.html')


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.isbn = request.POST['isbn']
        book.page_count = request.POST['page_count']
        book.language = request.POST['language']
        book.save()
        return redirect('list_books')

    return render(request, 'bookmodule/editbook.html', {'book': book})



def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books')



# List students and their addresses
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Add a new student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

# Edit student details
def edit_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

# Delete student
def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('student_list')
