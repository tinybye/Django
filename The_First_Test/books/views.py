from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.

def search_from(request):
    return render_to_response('books/search_form.html')

def search(request):
    error = False

    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('books/search_results.html', {'books': books, 'query': q})
    else:
        return render_to_response('books/search_form.html', {'error': True})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('books/contact_form.html',
        {'errors': errors})
