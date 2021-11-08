from django.shortcuts import render


def projects(request):
    """ A view to show Case Studies """
    return render(request, 'projects/projects.html')
