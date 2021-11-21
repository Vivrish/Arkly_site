from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Item, Stock
from .forms import DDMenuForm


def index(request):
    main_stock = Stock.objects.get(name='Main')
    items = main_stock.item_set.all().order_by('price', '-name')
    length = len(items)

    context = {
        'items': items,
        'length': length,
    }
    return HttpResponse(render(request, 'showcase/index.html', context))


# class CreateMyModelView(generic.CreateView):
# model = Stock
# form_class = DDMenuForm
# template_name = 'showcase/index.html'
# success_url = 'showcase/detail.html'

def ddformview(request):
    stock = Stock.objects.get(name='Main')
    form = DDMenuForm(request.POST or None)
    if form.is_valid():
        form = DDMenuForm(request.POST, instance=stock)
        form.save()
    context = {
        'form': form,
        'method': stock.sort,
    }
    return render(request, 'showcase/create.html', context)


class DetailView(generic.DetailView):
    model = Item
    template_name = 'showcase/detail.html'
