from django.contrib.auth import authenticate
from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from ..models import lockers,users
from django.db import connection
def index(request):
    #학부 별 남은라커 수/라커 수 구해서 띄워줄 것임.
    cs_left=lockers.objects.filter(department="CS",reserved=0).count()
    cs_lockers=lockers.objects.filter(department="CS").count()
    ee_left=lockers.objects.filter(department="EIE",reserved=0).count()
    ee_lockers=lockers.objects.filter(department='EIE').count()
    gm_left=lockers.objects.filter(department='GM',reserved=0).count()
    gm_lockers=lockers.objects.filter(department='GM').count()
    sw_left=lockers.objects.filter(department='SW',reserved=0).count()
    sw_lockers=lockers.objects.filter(department="SW").count()
    AIC_left=lockers.objects.filter(department="AIC",reserved=0).count()
    AIC_lockers=lockers.objects.filter(department="AIC").count()
    locker_context={"cs_left":cs_left,"cs_lockers":cs_lockers,'eie_left':ee_left,'eie_lockers':ee_lockers,
    'gm_left':gm_left,'gm_lockers':gm_lockers,'sw_left':sw_left,'sw_lockers':sw_lockers,
    'AI_left':AIC_left,'AI_lockers':AIC_lockers}
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/locker/lockerlist')
        else:
            locker_context['error']=1
            return render(request,'locker/index.html',locker_context)
    else:
        if request.user.is_authenticated:
            return redirect('/locker/lockerlist')
        else:
            return render(request,'locker/index.html',locker_context)

@login_required(login_url='locker:login')
def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('/locker/login')