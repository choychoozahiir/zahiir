from django.shortcuts import render
from Courses.models import Course
# Create your views here.

def home(request):
   courses = Course.objects.all()
   return render(request, 'courses/home.html', {'courses': courses})



