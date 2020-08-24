from django.http import HttpResponse
from django.shortcuts import render
from .models import Image

# Create your views here.

def all_photos(request):
    images = Image.get_images()

    return render(request, 'all-photos/photos.html', {"images": images, })

def search_results(request):
    return render(request, 'all-photos/search-results.html')

# def today_photos(request):
#     # return HttpResponse('Welcome to the Nguthi booth')
#     date = dt.date.today()
#     return render(request, 'all-photos/base.html', {"date": date,})

# def past_photos(request, past_date):
#     # return HttpResponse('Welcome to the Nguthi booth')
#     try:
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(today_photos)

#     return render(request, 'all-photos/base.html', {"date": date,})