from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image,Category,Location


def gallery_today(request):
    gallery = Image.objects.all()
    return render(request, 'all-galleries/today-gallery.html', {"gallery": gallery}) 


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        # searched_categories = Category.search_by_name(search_term)
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-galleries/search.html',{"message":message,"images": searched_images})#,"categories": searched_categories

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-galleries/search.html',{"message":message})    



# def delete_image(request, pk):
#     gallery = get_object_or_404(Cat, pk=pk)  

#     if request.method == 'POST':         
#         gallery.delete()                     
#         return redirect('/')             

#     return render(request, 'all-galleries/today-gallery.html', {"gallery": gallery})