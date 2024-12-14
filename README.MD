1. Enter these commands 
django-admin startproject airline
cd airline
code .
python3 manage.py startapp flights

2. Go to airline project > setting.py 
Add the flights app as installed app in the settings.py file 

INSTALLED_APPS = [
    'flights',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

3. Go ahead to airline project > urls.py file 
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include("flights.urls"))
]

4. Go to flights app > create the urls.py file 
from django.urls import path

from . import views

urlpatterns = [
    
]

5. Create the models for tables for CRUB operations 
Go to flights app > models.py file 
from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

6. Now run the command to make the migrations inside the app 
Migrations for 'flights':
  flights/migrations/0001_initial.py
    + Create model Flight

7. Now run the command 
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, flights, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying flights.0001_initial... OK
  Applying sessions.0001_initial... OK

8.   Applying flights.0001_initial... OK
Now had this file in the migrations 

9. Now, if i add the ls command then we will see 
ls
README.MD       airline         db.sqlite3      flights         manage.py

10. Enter into python shell 
 python3 manage.py shell 
Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
 from flights.models import Flight
>>> f = Flight(origin="New York", destination= "London",duration=415)
>>> f.save()
>>> Flight.objects.all()
<QuerySet [<Flight: Flight object (1)>]>

11. Go back to models.py file of flights ap
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

12. flights = Flight.objects.all()
>>> flights
<QuerySet [<Flight: 1: New York to London>]>

>>> flight = flights.first()
>>> flight
<Flight: 1: New York to London>
>>> flight.id
1
>>> flight.origin
'New York'
>>> flight.destination
'London'
>>> flight.duration
415
>>> flight.delete()
(1, {'flights.Flight': 1})
>>> 

13. Go to models.py file of flights app 
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

14. Go to models.py file of flights app

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") 
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
Add teh foreign key to maintain the realtionship 


15. Now, make the migrations 
Migrations for 'flights':
  flights/migrations/0002_airport_alter_flight_destination_alter_flight_origin.py
    + Create model Airport
    ~ Alter field destination on flight
    ~ Alter field origin on flight

16. Now run the command 
python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, flights, sessions
Running migrations:
  Applying flights.0002_airport_alter_flight_destination_alter_flight_origin... OK

17. To back to shell by running the command 
python3 manage.py shell 
 from flights.models import *
 >>> jfk = Airport(code="JFK", city = "New York")
>>> jfk.save()
>>> lhr = Airport(code="LHR", city = "London")
>>> lhr.save()
>>> cdg = Airport(code="CDG", city = "Paris")
>>> cdg.save()
>>> nrt = Airport(code ="NRT", city="Tokoyo")
>>> nrt.save()
 jfk = Airport(code="JFK", city = "New York")

>>> f = Flight(origin=jfk,destination=lhr, duration=415)
>>> f.save()
>>> f
<Flight: 1: New York (JFK) to London (LHR)>
>>> f.origin
<Airport: New York (JFK)>
>>> f.origin.city
'New York'
>>> f.origin.code
'JFK'
>>> lhr.arrivals.all()
<QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>

18. Go to urls.py file of flights app
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
]

19. Go to views.py file of flights app
from django.shortcuts import render

# Create your views here.
from .models import Flight

#create your views here 
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

20. Create the folder templates > folder flights > layout.html,index.html
inside the index.html 
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Flights</title>
    </head>
    <body>
        <!-- Content block for child templates -->
        {% block body %}
        {% endblock %}
    </body>
</html>
 add this code in the layout.html file 

21. In the index.html file:
{% extends "flights/layout.html" %}

{% block body %}
  <h1>Flights</h1>
  <ul>
    {% for flight in flights %}
      <li>Flight {{ flight.id }}: {{ flight.origin }} to {{ flight.destination }}</li>
    {% endfor %}
  </ul>
{% endblock %}

22. Go to shell and type these command 
from flights.models import *
>>> Airport.objects.all()
<QuerySet [<Airport: New York (JFK)>, <Airport: London (LHR)>, <Airport: Paris (CDG)>, <Airport: Tokoyo (NRT)>]>
>>> Airport.objects.filter(city="New York")
<QuerySet [<Airport: New York (JFK)>]>
>>> Airport.objects.filter(city="New York").first()
<Airport: New York (JFK)>
>>> Airport.objects.get(city="New York")
<Airport: New York (JFK)>
>>> jfk = Airport.objects.get(city="New York")
>>> cdg = Airport.objects.get(city="Paris")
>>> cdg
<Airport: Paris (CDG)>
>>> f = Flight(origin=jfk, destination=cdg, duration=435)
>>> f.save()


23. Create the admin account in the own terminal 
python3 manage.py createsuperuser
Username (leave blank to use 'awanlaptop'): ayesha
Email address: ayeshaimtiaz9999@gmail.com
Password: 
Password (again): 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

24. Go to amdin.py file of flights app 
from django.contrib import admin

from .models import Flight, Airport

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)

25. Create the wsgi.py file inside the airline project 
and add this code 
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

application = get_wsgi_application()

26. Run the command 
python3 manage.py runserver 

27. Go to urls.py file of flights 
 path("<int:flight_id>", views.flight, name="flight")

28. Go to views.py file of flights app 

def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id)
    return render(request, "flights/flight.html",{
        "flight": flight
    })

29. Go to Flights folder and inside the templates folder create the flights.html file 
{% extends "flights/layout.html" %}

{% block body %}
   <h1> Flight {{ flight.id }} </h1>

   <ul>
      <li>Origin: {{ flight.origin }} </li>
      <li>Destination: {{ flight.destination }} </li>
      <li>Duration : {{ flight.duration }} </li>
   </ul>
{% endblock %}

30. Now, create the new class called passanger 
inside the models.py file 

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passanger")

    def __str__(self):
        return f"{self.first} {self.last}"

31. Go to terminal and run the command 
python3 manage.py makemigrations
Migrations for 'flights':
  flights/migrations/0003_passenger.py
    + Create model Passenger

32. Now run the command 
python3 manage.py migrate
Migrations for 'flights':
flights/migrations/0003_passenger.py
    + Create model Passenger
awanlaptop@awans-MacBook-Pro airline % python3 manage.py migrate
Operations to perform:
Apply all migrations: admin, auth, contenttypes, flights, sessions
Running migrations:
Applying flights.0003_passenger... OK

33. Go to models.py file of models
from django.contrib import admin

from .models import Flight, Airport, Passenger 

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)

34. Go to models.py file of flight app 
def flight(request, flight_id):
    flight = Flight.objects.get(pk = flight_id)
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passengers": flight.passengers.all()
    })

35. Go to flights.index file of filghts app 
 <h2>Passengers</h2>
  <ul>
      {% for passenger in passengers %}
          <li>{{ passenger }}</li>
      {% empty %}
          <li>{{ No passengers. }}</li>
      {% endfor %}
    
</ul>

36. Go to flight.html file and add this code
   <a href="{% url 'index' %}">Back to flight list</a>
   before the end of endblock code 


37. Go  to index.html file of flights app > index.html and click the anchor tag in it to move back and forth 

{% extends "flights/layout.html" %}

{% block body %}
  <h1>Flights</h1>
  <ul>
    {% for flight in flights %}
    <li>
       <a href="{% url 'flight' flight.id %}">
        Flight {{ flight.id }}: {{ flight.origin }} to {{ flight.destination }}
       </a>
      </li>
    {% endfor %}
  </ul>
{% endblock %}


38. Go back to urls.py file of flighs
 path("<int:flight_id>/book", views.book, name="book")

39. Go to views.py and add the passenger to book the flight 

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight",args=(flight.id,)))
and add two import 
from django.http import HttpResponseRedirect
from django.urls import reverse

and update the Flight function 

def flight(request, flight_id):
flight = Flight.objects.get(pk = flight_id)
return render(request, "flights/flight.html",
{
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flight=flight).all()
})

40. Go to flight.html file and add the form into it 
 <h2> Add Passenger </h2>
    <form action="{% url 'book' flight.id %}" method="post">
      {% csrf_token %}
      <select name="passenger">
         {% for passenger in non_passengers %}
         <option value="{{ passenger.id }}">{{ passenger }}</option>
         {% endfor %}
      </select>
           <input type="submit">
    </form>

Inorder to register the people who are not in the flight 



# Go to admin.py file 
from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger)

# Go back to admin.py file 
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)


#Authentication 
1. Go to terminal and create an another app called user 
 python3 manage.py startapp users

2. Go to airline project > settings.py file 

INSTALLED_APPS = [
    'flights',
    'airline',
    'users',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

3. Go to urls.py file 
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include("flights.urls")),
    path("users/", include("users.urls"))
]

4. Go to users app > create the urls.py file 
from django.urls import path 

from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.login_view, name="login"),
    path('logout',views.logout_view, name="logout")
]

5. Go to views.py file and create teh three function 
index, login, and logout 

if the user was not autheticitated then what will happen we will handle it here in the views.py file 
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 

# Create your views here.

def index(request): #if the user is not autheticiated 
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
def login_request(request):
    return render(request, 'user/login.html')


6. Go and create the templates > users > layout.html 
create the login.html file 
{% extends "users/layout.html" %}

{% block body %}

<form action="{% url 'login' %}" method="post">
    {% csrf_token%}
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <input type="submit" value="login">
</form>

{% endblock %}

layout.html:
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Users</title>
    </head>
    <body>
        {% block body %}
        
        {% endblock %}
    </body>
</html>

# Go to views.py file 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 

# Create your views here.

def index(request): #if the user is not autheticiated 
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, passowrd=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html",{
                "message": "Invalid credentials."
            })
    return render(request, 'users/login.html')
    
def logout_view(request):
    pass

# go to login.html file 
{% block body %}
{% if message %}
  <div>{{message}}</div>
{% endif%}

# if we make the user login successfully then 
go to views and update this code 

def index(request): #if the user is not autheticiated 
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

# create the users.html file inside the user app of airline project 
{% extends "users/layout.html" %}

{% block body %}
<h1>Welcome, {{ request.user.first_name}} </h1>
<ul>
    <li>Username: {{ request.user.username }}</li>
    <li>Email: {{ request.user.email }}</li>
</ul>


{% endblock %}


# go to views.py 
def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message": "lOGGED OUT."
    })

# add the click link inside the user.html 
<a href="{% url 'logout' %}">Log out</a>