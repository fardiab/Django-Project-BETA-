from django.shortcuts import render, redirect, resolve_url
from repack.models import Item
from repack.forms import ItemRequestForm, ItemForm, ContactForm
from django.views.generic import View, TemplateView, CreateView


def index(request):
    context = {
        'title': 'First',
        'header': "Title of Site",
        'items': Item.objects.all(),
    }
    response = render(request, 'index.html', context=context)
    return response

def about(request):
    response = render(request, 'about.html')
    return response

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    response = render(request, 'contact.html', {'form': ContactForm()})
    return response



# class About(TemplateView):
#     template_name = 'about.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'About'
#         return context

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create_item.html', {'form': ItemForm()})


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'update_item.html', context=context)

def delete_item(request, id):
    items = Item.objects.all()
    item = Item.objects.get(id=id)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request, 'delete_item.html', {'item': item, 'items': items})

