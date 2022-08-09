from unicodedata import name
from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.

def index(request):
    
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
        return redirect('/')

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)
    return render(request, 'index.html', {'foods':foods, 'consumed_food':consumed_food})



def delete_consume(request, id):
    consume = Consume.objects.get(id=id)
    if request.method == "POST":
        consume.delete()
        return redirect('/')

    else:
        return render(request, 'delete.html')

