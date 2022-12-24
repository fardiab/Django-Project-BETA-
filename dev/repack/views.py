from django.http import JsonResponse
from django.shortcuts import render, redirect, resolve_url
from repack.models import Item
from repack.forms import ItemRequestForm, ItemForm, ContactForm
from django.views.generic import View, TemplateView, CreateView
from rest_framework.decorators import api_view
from .serializers import ItemSerializer, ContactSerializer
from rest_framework.response import Response
from django.db.models import QuerySet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status

def index(request):
    # context = {
    #     'title': 'First',
    #     'header': "Title of Site",
    #     'items': Item.objects.all(),
    # }
    response = render(request, 'index.html')
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

class ItemAPIView(APIView):
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        if kwargs.get('id'):
            items = Item.objects.get(id=kwargs.get('id'))
            serializer = self.serializer_class(items)
        else:
            items = Item.objects.all()
            serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)

class GetItemsAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class RetrieveItemAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CreateItemAPIView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        if Item.objects.filter(name=request.data.get('name')).exists():
            return Response(data={'message': 'Item already exists'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class UpdateItemAPIView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'

class DeleteItemAPIView(DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        if not Item.objects.filter(id=kwargs.get('id')).exists():
            return Response(data={'message': 'Item does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return Response(data={'message': 'Item deleted'}, status=status.HTTP_200_OK)


    