from django.shortcuts import get_object_or_404, render, redirect
import json
from .forms import InputFormset
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

def saved_text(request):
    """"""
    
    database = DataModel.objects.all()


    number = 0
    entries = {}
    for table in database:
        number += 1
        entries[str(number)] = []
        for value in table.data.values():
            print(entries)
            entries[str(number)] += [value]
            
    context = {'entries': entries}
    
    return render(request, 'data-page.html', context)

    