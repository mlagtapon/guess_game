from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'randomNum' not in request.session:
        request.session['randomNum'] = random.randint(1, 100)
    
    print(request.session['randomNum'])

    return render(request, "index.html")

def process(request):
    
    if int(request.POST['guess']) < request.session['randomNum']:
        request.session['message'] = "Your guess is too low!!"
        return redirect('/')

    if int(request.POST['guess']) > request.session['randomNum']:
        request.session['message'] = "Your guess is too high!!"
        return redirect('/')
    
    if int(request.POST['guess']) == request.session['randomNum']:
        request.session['message'] = "Your guess is right!!"
        return redirect('/')

    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')