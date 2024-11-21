from django.http import HttpResponse
from django.shortcuts import render


def home(request):
   context={
      "first_name":"athira",
      "second_name":"surya",
   }
   return render(request,'home.html',context)

def demo(request):
     number={
        'num':0,
     }
     return render(request,'demo.html',number)

def books(request):
    books=[
        {"tittle":"wings of fire","author":"Abdul kalam",'year':1998},
        {"tittle":"reinventing leadership","author":"Prathibha devisingh patil",'year':2016},
        {"tittle":"changing india","author":"Manmohan singh",'year':2019},
    ]
    context={
        'books':books
    }
    return render(request,'books.html',context)