from django.shortcuts import render,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from .models import Event,Project,Future_plans,Bursary,News
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .forms import BursaryForm
def home(request):
    return render(request,'home.html')

def event(request):
    events = Event.objects.all()
    return render(request,'events.html',{'events':events})

def project(request):
    projects = Project.objects.all()
    return render(request,'projects.html',{'projects':projects})

def future_plan(request):
    plans = Future_plans.objects.all()
    return render(request,'plans.html',{'plans':plans})


def news(request):
    news = News.objects.all()
    return render(request,'news.html',{'news':news})

def bursary(request):

    if request.method == 'POST':
        form = BursaryForm(request.POST)
        if form.is_valid():
            bursary = form.save(commit=False)
            bursary.save()
            return redirect('home')
    else:
        form = BursaryForm()

    return render(request, 'bursary.html', locals())

def contact(request):
    return render(request,'contact.html')
