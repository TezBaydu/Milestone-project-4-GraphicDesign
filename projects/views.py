from django.shortcuts import render, get_object_or_404
from .models import Project, Company


def all_projects(request):
    """ A view to show Case Studies including filtering """

    projects = Project.objects.all()
    companies = None

    if request.GET:
        if 'company' in request.GET:
            companies = request.GET['company']
            projects = projects.filter(company__name__in=companies)
            companies = Company.objects.filter(name__in=companies)

    context = {
        'projects': projects,
        'current_companies': companies,
    }

    return render(request, 'projects/projects.html', context)
