from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
import calendar,datetime
def timetable(request):
    if request.method == 'POST':
        time = request.POST
        if time.get('Date') and time.get('Month'):
            date=int(request.POST['Date'])
            month=int(request.POST['Month'])
            
            year=2020
            dayNumber = calendar.weekday(year, month, date) 
            return HttpResponseRedirect("http://localhost:8000/time1/"+str(dayNumber))
        else:
            return render(request,'timetable/value.html',{"error":1})
    else:
        return render(request,'timetable/value.html')
def day(request, album_id):
    day2=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    user1=day2[int(album_id)]
    return render(request,'timetable/day'+str(int(album_id)+1)+".html",{'User':user1,'Day':album_id})


