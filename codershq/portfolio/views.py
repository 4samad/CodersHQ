from django.shortcuts import render

from codershq.portfolio.models.model_project import Project

from .forms import PortfolioForm, EducationForm, UserForm, ExperienceForm, ProjectForm
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Experience, JobProfile
from django.shortcuts import get_object_or_404
from codershq.users.models import User


@login_required
def portfolio_edit(request):

    # create portfolio if user doesnt have it
    user = request.user
    try:
        portfolio = Portfolio.objects.get(user=user)
        print("user had portfolio")
    except Portfolio.DoesNotExist:
        portfolio = Portfolio()
        portfolio.user = user
        portfolio.save()
        print("save user portfolio")

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # choose the right form
        if 'github_url' in request.POST:
            # create a form instance and populate it with data from the request:
            form = PortfolioForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                data = form.cleaned_data
                portfolio.twitter_handle = data['twitter_handle']
                portfolio.github_url = data['github_url']
                portfolio.website_url = data['website_url']
                portfolio.linkedin_url = data['linkedin_url']
                portfolio.description = data['description']
                portfolio.save()
                print("Portfolio save success")
            else:
                print(form.errors)

        if 'education_level' in request.POST:
            # create a form instance and populate it with data from the request:
            form = EducationForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                print("education success")
            else:
                print(form.errors)

        if 'name' in request.POST:

            form = UserForm(request.POST, request.FILES)

            if form.is_valid():
                print("user form success")
                data = form.cleaned_data
                user.name = data['name']
                user.bio = data['about']
                user.profile_image = data['profile_image']
                user.save()

            else:
                print("user form not success")
                print(form.errors)

        if 'job_title' in request.POST:

            form = ExperienceForm(request.POST)

            if form.is_valid():
                experience = Experience()
                data = form.cleaned_data
                experience.user_profile = portfolio
                experience.job_title = data['job_title']
                experience.start_date = data['start_date']
                experience.end_date = data['end_date']
                experience.is_current = data['is_current']
                experience.save()
                print("experiance form success")

            else:
                print("experience form not success")
                print(form.errors)

        # if 'project_name' in request.POST:

        #     form = ProjectForm(request.POST)

        #     if form.is_valid():
        #         project = Project()
        #         data = form.cleaned_data
        #         project.job_profile = portfolio
        #         project.job_title = data['job_title']
        #         project.start_date = data['start_date']
        #         project.end_date = data['end_date']
        #         project.is_current = data['is_current']
        #         project.save()
        #         print("experiance form success")

        #     else:
        #         print("experience form not success")
        #         print(form.errors)



    print(request.POST)
    context = {"portfolio": portfolio}
    return render(request, 'portfolio/portfolio_form.html', context)

def portfolio_show(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user': user}
    return render(request, 'portfolio/portfolio.html', context)
