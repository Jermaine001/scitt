from django.shortcuts import render, redirect
from .models import Enrollment
from django.contrib import messages

# Create your views here.
def home(request):
    return render (request, 'scittapp/index.html')

def about(request):
    return render(request, 'scittapp/about.html')

def courses(request):
    return render(request, 'scittapp/courses.html')

def partner(request):
    return render(request, 'scittapp/partner.html')

def alumnis(request):
    return render(request, 'scittapp/alumni.html')

def contact(request):
    return render(request, 'scittapp/contact.html')

def partner(request):
    return render(request, 'scittapp/partner.html')

def alumnis(request):
    return render(request, 'scittapp/alumnis.html')

def contact(request):
    return render(request, 'scittapp/contact.html')

def enroll(request):
    if request.method == 'POST':
        # Capture form data and save it to the database
        enrollment = Enrollment(
            firstname=request.POST.get('firstname'),
            lastname=request.POST.get('lastname'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            age=request.POST.get('age'),
            education=request.POST.get('education'),
            programming=request.POST.get('programming'),
            availability=request.POST.get('availability'),
            computer_access=request.POST.get('computer_access'),
            internet_access=request.POST.get('internet_access')
        )
        enrollment.save()
        
        # success message after enrollment
        return render(request, 'scittapp/enroll_success.html', {'firstname': enrollment.firstname})

    return render(request, 'scittapp/enroll.html')  # Render the form template

