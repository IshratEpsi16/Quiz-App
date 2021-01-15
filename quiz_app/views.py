from django.shortcuts import render
from .models import table
# Create your views here.


def home(request):
    test = table.objects.all()
    context = {'test': test}
    return render(request, 'quiz_app/index.html', context)
