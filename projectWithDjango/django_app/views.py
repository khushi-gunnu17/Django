from django.shortcuts import render
from .models import fruitVariety, Store
from django.shortcuts import get_object_or_404
from .forms import FruitVarietyForm

# Create your views here.
def all_app(request) :

    # arrays will come as the response here for fruits
    fruits = fruitVariety.objects.all()

    return render(request, 'django_app/all_app.html', {'fruits' : fruits})



def fruit_detail(request, fruit_id) : 
    fruit = get_object_or_404(fruitVariety, pk=fruit_id)
    return render(request, 'django_app/fruit_detail.html', {'fruit' : fruit})



def fruit_stores(request) :
    stores = None

    if request.method == 'POST' :
        form = FruitVarietyForm(request.POST)

        if form.is_valid() :
            fruit_variety = form.cleaned_data['fruit_variety']
            stores = Store.objects.filter(fruit_varities=fruit_variety)

    else :
        form = FruitVarietyForm()

    return render(request, "django_app/fruit_stores.html", {'stores' : stores, 'form': form}) 