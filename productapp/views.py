from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
from productapp.models import District, Community, Product
from datetime import datetime

def hello(request):
    return HttpResponse("hello, Products!")

def list_communities(request):
    district_list = District.objects.all()
    return render(request, 'community_list.html', locals())

def list_product(request, community_id=None):
    if community_id:
        community = Community.objects.get(id = community_id)
        product_list = community.products.all()
    else:
        product_list = Product.objects.all()
    #product_list = Product.objects.filter(date_available__lt=datetime.now().datetime()).order_by("-date_available")
    '''
    paginator = Paginator(product_list, 2)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        product_list = paginator.page(page)
    except :
        product_list = paginator.page(paginator.num_pages)
    '''
    return render(request, 'product_list.html', locals())

def view_product(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'product_view.html', locals())

