from django.shortcuts import render, redirect
from .forms import InputForm
from .models import DataModel
# Create your views here.

def index(request):
    """"""

    if request.method == 'POST':
        input_form = InputForm(data = request.POST)
        if input_form.is_valid():
            data = DataModel(data={'data':input_form.data.get('input_field')})
            data.save()
            return redirect('/')
    else:
        input_form = InputForm()

    context = {'form': input_form}

    return render(request, 'index.html', context)
