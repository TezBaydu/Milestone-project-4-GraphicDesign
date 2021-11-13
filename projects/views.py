from django.shortcuts import render, get_object_or_404
from .models import Project, Company


def all_projects(request):
    """ A view to show Case Studies including filtering """

    projects = Project.objects.all()
    companies = None

    if request.GET:
        if 'company' in request.GET:
            companies = request.GET['company']
            projects = projects.filter(company__name=companies)
            company = Company.objects.filter(name=companies)[0]

    context = {
        'projects': projects,
        'company': company,
    }

    return render(request, 'projects/projects.html', context)
