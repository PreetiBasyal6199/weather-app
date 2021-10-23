from django.shortcuts import render
import urllib.request
import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
def home (request):
    if request.method=="POST":
        city=request.POST['city']
        try:
            source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=c845447bfa35466d943b8a346dbd948c').read()
       
            list_of_data=json.loads(source)
            data={
                "city_name":str(list_of_data['name']),
                "temp":(list_of_data['main']['temp']),
                "pressure":str(list_of_data['main']['pressure']),
                "humidity":str(list_of_data['main']['humidity']),
                "description":str(list_of_data['weather'][0]['description']),
                "icon":str(list_of_data['weather'][0]['icon']),
                "min":str(list_of_data['main']['temp_min']),
                "max":str(list_of_data['main']['temp_max']),
                "feels_like":str(list_of_data['main']['feels_like']),

            }
            return render(request,'index.html',data)
        except :
            messages.error(request,'The city you entered is not found')
            return render(request,'index.html')


        # except: 
        #     messages.error(request, 'City not found.')
        #     return render(request,'home2.html')
            
        
        
        
    else:
        data={}
    
    return render(request,'index.html',data)