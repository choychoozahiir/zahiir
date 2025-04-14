from django.shortcuts import render
from Courses.models import Course
# Create your views here.

def home(request):
   return render(request, 'courses/home.html')

def academics(request):
   courses = Course.objects.all()
   return render(request, 'courses/academics.html', {'courses': courses})



