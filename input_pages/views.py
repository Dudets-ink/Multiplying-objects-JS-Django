from django.shortcuts import render, redirect
from .forms import InputForm, InputFormset
from .models import DataModel
# Create your views here.

def index(request):
    """"""

    model_data = {}
    
    if request.method == 'POST':
        print(request.POST)
        formset = InputFormset(data = request.POST)
        if  formset.is_valid():
            for key, value in formset.data.items():
                if 'input_field' in key:
                    model_data[f'{key}'] = value
            formset_model= DataModel(data = model_data)
            formset_model.save()
            return redirect('/')
        else:
            print(formset.non_form_errors())
  
    formset = InputFormset()
        
    context = {'formset': formset}

    return render(request, 'index.html', context)
