from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpRequest , HttpResponse , JsonResponse
from .models import Member,Book , Borrow

# Create your views here.
def home(request):
    return render(request,'home.html')

def books(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            title = request.POST.get('title')
            author = request.POST.get('author')
            category = request.POST.get('category')
            ISBNNo = request.POST.get('ISBNNo')
            qty = request.POST.get('qty')  # Added for quantity
            status = request.POST.get('status')
            Book.objects.create(BookName=title, author_name=author, category=category, ISBN=ISBNNo, Qty=qty, bookstatus=status)
            return JsonResponse({'success': True})

        elif action == 'edit':
            bookID = request.POST.get('bookID')
            book = get_object_or_404(Book, pk=bookID)
            book.BookName = request.POST.get('title')
            book.author_name = request.POST.get('author')
            book.category = request.POST.get('category')
            book.ISBN = request.POST.get('ISBNNo')
            book.Qty = request.POST.get('qty')  # Update quantity
            book.bookstatus = request.POST.get('status')
            book.save()
            return JsonResponse({'success': True})

        elif action == 'delete':
            bookID = request.POST.get('bookID')
            book = get_object_or_404(Book, pk=bookID)
            book.delete()
            return JsonResponse({'success': True})

    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def contact(request):
    return render(request,'contact.html')

def loans(request):
    if request.method == 'POST':
        if 'book-title' in request.POST:
            # Handle borrowing a book
            book_id = request.POST.get('book-title')
            member_id = request.POST.get('member-name')
            borrow_date = request.POST.get('borrow-date')

            if book_id and member_id and borrow_date:
                book = Book.objects.get(BookID=book_id)
                member = Member.objects.get(MID=member_id)
                Borrow.objects.create(BookID=book, MID=member, b_date=borrow_date)
        elif 'return_book_id' in request.POST:
            # Handle returning a book
            borrow_id = request.POST.get('return_book_id')
            Borrow.objects.filter(BID=borrow_id).delete()

        return redirect('loans')

    books = Book.objects.all()
    members = Member.objects.all()
    borrows = Borrow.objects.select_related('BookID', 'MID').all()
    return render(request, 'loans.html', {'books': books, 'members': members, 'borrows': borrows})

def members(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            name = request.POST.get('name')
            email = request.POST.get('email')
            contact_no = request.POST.get('phone')
            Member.objects.create(Name=name, email=email, contact_no=contact_no)
        
        elif action == 'edit':
            mid = request.POST.get('mid')
            member = get_object_or_404(Member, pk=mid)
            member.Name = request.POST.get('name')
            member.email = request.POST.get('email')
            member.contact_no = request.POST.get('phone')
            member.save()
        
        elif action == 'delete':
            mid = request.POST.get('mid')
            member = get_object_or_404(Member, pk=mid)
            member.delete()
        
        return JsonResponse({'success': True})
    
    members = Member.objects.all()
    return render(request, 'members.html', {'members': members})