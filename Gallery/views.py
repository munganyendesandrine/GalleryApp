from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image


def gallery_today(request):
    gallery = Image.objects.all()
    return render(request, 'all-galleries/today-gallery.html', {"gallery": gallery}) 


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-galleries/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-galleries/search.html',{"message":message})    