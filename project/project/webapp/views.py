from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import SignUp
# my import
import re
import datetime

# pre defined
current_time = datetime.datetime.now()
Pattern = re.compile(r"^\+(?:[0-9] ?){6,14}[0-9]$")

# Create your views here.

def dashboard(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email_address = request.POST['email']
        address = request.POST['address']
        contact = request.POST['contact']
        dob = request.POST['dob']
        doy = dob.split("-")
        
        # validation
        
        if current_time.year - int(doy[0]) >= 18:
            if Pattern.match(contact):
                try:
                    result  = SignUp.objects.create(name=full_name, email=email_address, address=address, contact=contact, dob=dob)
                    result.save()
                    send_mail(
                        'Testing Email',
                        'Thanks for connecting with us.',
                        email_address ,
                        ['revegrandsystems@gmail.com'],
                        fail_silently=False,
                    )
                    table = SignUp.objects.all()
                    success = "Form Submitted Successfully"
                    return render(request, "dashboard.html", {"success": success, "table":table})
                except Exception as e:
                    messages.error(request, "Error: "+e)
                    return redirect("/dashboard")

                
                
            else:
                messages.error(request, "Invalid Contact Number")
                return redirect("/dashboard")
                
        else:
            messages.error( request, "You are not 18 years old. Can't access this site.")
            return redirect("/dashboard")
    
    else:
        table = SignUp.objects.all()
        return render(request, "dashboard.html",{"table":table} )

def table(request):
    table = SignUp.objects.all()
    return render(request, "table.html", {"table":table})
    
  
