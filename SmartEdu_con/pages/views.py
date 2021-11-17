from django.shortcuts import render
# from django.http import HttpResponse

# Index View
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Index Sayfasi</h1>")

# About View
def about(request):
    return render(request, 'about.html')

# Contact View
def contact(request):
    return render(request, 'contact.html')