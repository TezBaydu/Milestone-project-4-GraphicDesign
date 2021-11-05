from django.shortcuts import render


def index(request):
    """ A view to return indexpage """
    return render(request, 'home/index.html')
