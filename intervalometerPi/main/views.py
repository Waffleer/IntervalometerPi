from django.shortcuts import render, redirect
from . models import Type, Setting, Cycle, Run
import subprocess

def takePictures(context: dict):
    subprocess.run(["dir"])

def cancelPictures():
    pass

def index(request):
    context = { 
        "pLenSelector": "",
        "intervalSelector": "",
        "pLen": "",
        "interval": "",
        "count": "",
        "bulb": "",
    }

    if request.method == 'POST':
        context["pLenSelector"] = request.POST.get("pLenSelector")
        context["intervalSelector"] = request.POST.get("intervalSelector")
        context["pLen"] = request.POST.get("pLen")
        context["interval"] = request.POST.get("interval")
        context["count"] = request.POST.get("count")
        context["bulb"] = request.POST.get("bulb")

        if(context["pLenSelector"] == "sec"): pLenSelector = True
        else: pLenSelector = False
        if(context["intervalSelector"] == "sec"): intervalSelector = True
        else: intervalSelector = False
        if(context["bulb"] == "true"): bulb = True
        else: bulb = False
        if 'submit' in request.POST:
            settings = Setting.objects.create(pLen=int(context["pLen"]), pLenSeconds=pLenSelector, interval=int(context["interval"]), intervalSeconds=intervalSelector, count=context["count"], bulb=bulb)
            settings.save()
            run = Run.objects.create(top=0, settings=settings)
            run.save()
            takePictures(context)
            return redirect(f'/running')

        if 'clear' in request.POST:
            pass

        print(request.POST)
        print(context)
    return render(request, 'dashboard/index.html', context)

def running(request):
    context = { 
        "top": 0,
        "bottom": 0,
    }

    run = Run.objects.get()
    context["top"] = run.top
    context["bottom"] = run.settings.count
    print(run)


    if request.method == 'POST':

        if 'index' in request.POST:
            if(context["top"] == context["bottom"]):
                run.delete()
                return redirect("index")

        if 'cancel' in request.POST:
            cancelPictures()
            run.delete()
            return redirect("index")
            

        print(request.POST)
        print(context)









    return render(request, 'dashboard/running.html', context)