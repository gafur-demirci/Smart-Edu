from django.shortcuts import render
# from django.http import HttpResponse

#Index View
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Index Sayfasi</h1>")
