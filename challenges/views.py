from django.shortcuts import render
from .models import Employee
from django.db.models import Q
from challenges.models import Employee

def welcome(request):
    return render(request, 'index.html')

def showtable(request):
    posts = Employee.objects.all()
    print(posts)
    return render(request, 'index2.html', {'post': posts})

def SaveData(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name', 'default')
        last_name = request.POST.get('last_name', 'default')
        inputCity = request.POST.get('inputCity', 'default')
        data = Employee(first_name = first_name, last_name = last_name, middle_name = inputCity)
        data.save()
    return render(request, 'index2.html')

def Showbyfilter(request):
    posts = Employee.objects.filter( Q(middle_name__startswith="S") | Q(middle_name__startswith="J"))
    return render(request, "index2.html", {'post': posts})
 
def analyse(request):
    first_name = request.POST.get('first_name', 'default')
    last_name = request.POST.get('last_name', 'default')
    birthdate = request.POST.get('birthdate', 'default')
    email = request.POST.get('email', 'default')
    phone = request.POST.get('phone', 'default')
    inputCity = request.POST.get('inputCity', 'default')
    holidayplace = request.POST.get('holidayplace', 'default')
    radio = request.POST.get('radio')
    Range = request.POST.get('range')
    appt = request.POST.get('appt')
    checkbox = request.POST.get('checkbox')
    textarea = request.POST.get('textarea')
    password = request.POST.get('password')
    multiselection = request.POST.getlist('multiselection')
    print(multiselection)
    params = {"First_Name":first_name, "Last_Name":last_name,"Gender": radio, "Birthdate": birthdate,
        "Email_id": email, "Contact_Number": phone, "Travel_From": inputCity,
        "Holiday_Destination": holidayplace, "Range": Range, "appt":appt, "checkbox": checkbox,
        "textarea": textarea, "password": password, "multiselection": multiselection}
    
    return render(request, 'analyse.html', params)