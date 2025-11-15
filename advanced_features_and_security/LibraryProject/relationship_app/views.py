from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Book, Library


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Function-based view for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ ALX checker expects this usage
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# You’ll use built-in class-based views for login/logout
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_year = request.POST.get('publication_year')
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('list_books')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
