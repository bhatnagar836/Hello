from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


# Create your view here
def index(request):
    # context : set of variables we send on our template
    context = {
        'var1': 'Pooja',
        'var2': 'Aditi',

    }
    messages.success(request, 'This is a test message')
    # return HttpResponse("This is home page")
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        contact_num = request.POST.get('contact_num')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')
        contact_details = Contact(firstname=firstname, lastname=lastname, contact_num=contact_num, email=email,
                                  address=address, message=message, date=datetime.today())
        contact_details.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')

