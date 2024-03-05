from django.http import HttpResponse
from django.template import loader
def home_views(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def myfirst_views(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
def accounts_view(request):
    template = loader.get_template('accounts.html')
    return HttpResponse(template.render())
def access_view(request):
    template = loader.get_template('access.html')
    return HttpResponse(template.render())
def skin_hair_view(request):
    template = loader.get_template('skin_hair.html')
    return HttpResponse(template.render())
def novelties_view(request):
    template = loader.get_template('novelties.html')
    return HttpResponse(template.render())
def bags_view(request):
    template = loader.get_template('bags.html')
    return HttpResponse(template.render())
from django.shortcuts import render
def search_results(request):
    query = request.GET.get('query')
    products = None 
    if query:
        products = products.objects.filter(name__icontains=query)
    else:
        products = products.objects.all()

    context = {
        'query': query,
        'products': products
    }
    return render(request, 'search_results.html', context)


