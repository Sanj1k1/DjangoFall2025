from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from datetime import datetime
import pytz

counter_value = 0
# Create your models here.
def welcome(request:HttpResponse,*args:tuple[any,...],**kwargs:dict[str,any]) -> HttpResponse:
    """Return HTML page where there are 3 buttons 
       
        Parameters:
            request: HttpRequest
                The request object.
            *args: list
                Additional positional arguments.
            **kwargs: dict
                Additional keyword arguments.
    
        Returns:
            HttpResponse
                Rendered HTML page with 3 links in it.
    """ 
    return render(request=request,template_name="index.html")


def users_list(request:HttpResponse,*args:tuple[any,...],**kwargs:dict[str,any]) -> HttpResponse:
    """Returns HTML page with users lists
    
         Parameters:
            request: HttpRequest
                The request object.
            *args: list
                Additional positional arguments.
            **kwargs: dict
                Additional keyword arguments.
    
        Returns:
            HttpResponse
                Rendered HTML page with user lists.   
    """
    users = [
        {"fullname":"Amirgli Sanjar","age":20},
        {"fullname":"Nauryz Abylai","age":20},
        ]
    return render(request=request,template_name="users.html",context={'users':users})

def city_time(request:HttpResponse,*args:tuple[any,...],**kwargs:dict[str,any]) -> HttpResponse:
    """Returns HTML page city times
    
         Parameters:
            request: HttpRequest
                The request object.
            *args: list
                Additional positional arguments.
            **kwargs: dict
                Additional keyword arguments.
    
        Returns:
            HttpResponse
                Rendered HTML page with city times.   
    """
    utc_time = datetime.now(pytz.UTC)
    cities = {
        "UTC": utc_time.strftime("%b %d, %Y, %I:%M %p"),
        "Almaty": utc_time.astimezone(pytz.timezone("Asia/Almaty")).strftime("%b %d, %Y, %I:%M %p"),
        "Calgary": utc_time.astimezone(pytz.timezone("Canada/Mountain")).strftime("%b %d, %Y, %I:%M %p"),
        "Moscow": utc_time.astimezone(pytz.timezone("Europe/Moscow")).strftime("%b %d, %Y, %I:%M %p"),
    }
    
    return render(request=request,template_name="cities.html",context={"cities":cities})

def counter(request:HttpResponse,*args:tuple[any,...],**kwargs:dict[str,any]) -> HttpResponse:
    """Returns HTML page city times
    
         Parameters:
            request: HttpRequest
                The request object.
            *args: list
                Additional positional arguments.
            **kwargs: dict
                Additional keyword arguments.
    
        Returns:
            HttpResponse
                Rendered HTML page with city times.   
    """
    #Берем текущее значение из сессий если его нет ставим 0
    global counter_value
    
    if request.method =="POST":
        if "plus" in request.POST:
            counter_value+=1
        elif "minus" in request.POST:
            counter_value-=1
        elif "reset" in request.POST:
            counter_value=0
        
        return redirect("counter")

    return render(request=request,template_name="counter.html",context={"counter":counter_value})