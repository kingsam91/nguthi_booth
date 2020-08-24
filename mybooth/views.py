  
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt

def welcome(request):
    # return render(request, 'welcome.html')
    return render(request, 'all-photos/past_photos.html', {"date": "xxx"})

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