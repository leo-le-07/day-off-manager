from django.shortcuts import render
from .models import User

# Create your views here.
def request_list(request):
  user = User.objects.first()
  return render(request, 'app/request_list.html', {'user': user})