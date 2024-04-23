from django.shortcuts import render, redirect
from . models import Type, Setting, Cycle, Run
from subprocess import Popen, PIPE
process = 'process'

def takePictures(context: dict):
    global process
    pLen = 0
    interval = 0
    count = 0
    bulb = 0
<<<<<<< HEAD
    report = context['report']
=======
>>>>>>> 1bb2a7d7cd934a6288b626b9799099d842a62509
    if(context["pLenSelector"] == "sec"):
        pLen = int(float(context["pLen"])*1000)
    else:
        pLen = int(1000/float(context["pLen"]))

    if(context["intervalSelector"] == "sec"):
        interval = int(float(context["interval"])*1000)
    else:
        interval = int(1000/float(context["interval"]))

    if(context["bulb"] == 'true'):
        bulb = 1
    else:
        bulb = 0

<<<<<<< HEAD
    process = Popen(["../a.out",str(pLen),str(interval),str(context["count"]),str(report)])
    #process = Popen(["../a.out",str(pLen),str(interval),str(context["count"]),str(bulb)])
=======
    process = Popen(["../a.out",str(pLen),str(interval),str(context["count"]),str(bulb)])
>>>>>>> 1bb2a7d7cd934a6288b626b9799099d842a62509
    #print(process)

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


    try:
        run = Run.objects.get()
        return redirect('/running')
    except Run.DoesNotExist:
        pass

    if request.method == 'POST':
        context["pLenSelector"] = request.POST.get("pLenSelector")
        context["intervalSelector"] = request.POST.get("intervalSelector")
        context["pLen"] = request.POST.get("pLen")
        context["interval"] = request.POST.get("interval")
        context["count"] = request.POST.get("count")
        context["bulb"] = request.POST.get("bulb")
<<<<<<< HEAD
        context["report"] = 1
=======
>>>>>>> 1bb2a7d7cd934a6288b626b9799099d842a62509
        print(context['bulb'])
        if(context["pLenSelector"] == "sec"): pLenSelector = True
        else: pLenSelector = False
        if(context["intervalSelector"] == "sec"): intervalSelector = True
        else: intervalSelector = False
        if(context["bulb"] == "true"): bulb = True
        else: bulb = False
        if 'submit' in request.POST:
            settings = Setting.objects.create(pLen=float(context["pLen"]), pLenSeconds=pLenSelector, interval=float(context["interval"]), intervalSeconds=intervalSelector, count=context["count"], bulb=bulb)
            settings.save()
            run = Run.objects.create(top=0, settings=settings)
            run.save()
            takePictures(context)
            return redirect(f'/running')

        if 'clear' in request.POST:
            pass

        if 'click' in request.POST:
            return redirect(f'/clicking')



        print(request.POST)
        print(context)
    return render(request, 'dashboard/index.html', context)

def clicking(request):

    context = {
        "pLenSelector": "",
        "intervalSelector": "",
        "pLen": "",
        "interval": "",
        "count": "",
        "bulb": "",
    }

    try:
        run = Run.objects.get()
        return redirect('/running')
    except Run.DoesNotExist:
        pass



    if request.method == 'POST':
        if 'clicking' in request.POST:
            context["pLenSelector"] = "sec"
            context["intervalSelector"] = "sec"
            context["pLen"] = 0
            context["interval"] = 0
            context["count"] = 1
            context["blub"] = ""
            context["report"] = 0
            takePictures(context)


        if 'home' in request.POST:
            return redirect(f'/')



        #print(request.POST)
        #print(context)
    return render(request, 'dashboard/clicking.html', context)





def running(request):
    context = { 
        "top": 0,
        "bottom": 0,
        "pLenSelector": "",
        "intervalSelector": "",
        "pLen": "",
        "interval": "",
        "count": "",
        "bulb": "",
<<<<<<< HEAD
        "report": 1,
=======
>>>>>>> 1bb2a7d7cd934a6288b626b9799099d842a62509
    }
    global process
    run = Run.objects.get()
    context["top"] = run.top
    context["bottom"] = run.settings.count
    context["pLenSelector"] = run.settings.pLenSeconds
    context["intervalSelector"] = run.settings.intervalSeconds
    context["pLen"] = run.settings.pLen
    context["interval"] = run.settings.interval
    context["count"] = run.settings.count
    context["bulb"] = run.settings.bulb

    if(run.settings.pLenSeconds):
        context["pLen"] = str(float(run.settings.pLen))
    else:
         context["pLen"] = "1 / " + str(float(run.settings.pLen))

    if(run.settings.intervalSeconds):
        context["interval"] = str(float(run.settings.interval))
    else:
         context["interval"] = "1 / " + str(float(run.settings.interval))


    if request.method == 'POST':

        if 'index' in request.POST:
            if(context["top"] == context["bottom"]):
                run.delete()
                return redirect("index")

        if 'cancel' in request.POST:
            try:
                process.kill()
            except:
                pass
            run.delete()
            return redirect("index")

<<<<<<< HEAD
        if 'again' in request.POST:
            run.top = 0
            run.save()
            takePictures(context)
            return redirect(f'/running')
=======
>>>>>>> 1bb2a7d7cd934a6288b626b9799099d842a62509
        #print(request.POST)
        print(context)

    return render(request, 'dashboard/running.html', context)
