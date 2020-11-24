from django.shortcuts import render, HttpResponse, redirect
import random
def index(request):
    if 'my_num' not in request.session:
        request.session['my_num'] = random.randint(1,100)
        print(request.session['my_num'])
    
    return render(request,'index.html')

def guess(request):
    request.session["estimate"] = request.POST['the_guess']
    print(request.session['my_num'])
    print(request.POST['the_guess'])
    if int(request.POST['the_guess']) == int(request.session['my_num']):
        return redirect('/correct')
        
    if int(request.POST['the_guess']) < int(request.session['my_num']):
        return redirect('/wrong')
    if int(request.POST['the_guess']) > int(request.session['my_num']):
        return redirect('/wrong2')
    
    return redirect('/')
def correct_answer(request):
    return render(request,'guess.html')
def wrong_answer(request):
    return render(request,'wrong.html')
def wrong2(request):
    return render(request, 'wrong2.html')