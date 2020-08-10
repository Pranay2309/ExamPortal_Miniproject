from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app.form import createuserform
from django.contrib.auth import authenticate,login,logout
from app.models import Questions
from app.models import Answerset
# Create your views here.
def index(request):
    if (request.user.is_authenticated):
        Answerset.objects.create(student=request.user)
        
        return redirect('/start/0')
    return render(request,"main.html")

def start(request,id):
    print(request.method)
    if request.method == 'POST':
        if (id==0):
            Answerset.objects.filter(student=request.user).update(Answer1=request.POST.getlist('check')[0])
            uanswer = Answerset.objects.filter(student=request.user).values('Answer1')[0]['Answer1']
            aanswer = Questions.objects.filter(Question_No=id).values('answer')[0]['answer']
            if (uanswer==aanswer):
                Answerset.objects.filter(student=request.user).update(correct1=True)
            else:
                Answerset.objects.filter(student=request.user).update(correct1=False)
                
            
        elif (id==1):
            Answerset.objects.filter(student=request.user).update(Answer2=request.POST.getlist('check')[0])
            uanswer = Answerset.objects.filter(student=request.user).values('Answer2')[0]['Answer2']
            aanswer = Questions.objects.filter(Question_No=id).values('answer')[0]['answer']
            if (uanswer==aanswer):
                Answerset.objects.filter(student=request.user).update(correct2=True)
            else:
                Answerset.objects.filter(student=request.user).update(correct2=False)

        elif (id==2):
            Answerset.objects.filter(student=request.user).update(Answer3=request.POST.getlist('check')[0])
            uanswer = Answerset.objects.filter(student=request.user).values('Answer3')[0]['Answer3']
            aanswer = Questions.objects.filter(Question_No=id).values('answer')[0]['answer']
            if (uanswer==aanswer):
                Answerset.objects.filter(student=request.user).update(correct3=True)
            else:
                Answerset.objects.filter(student=request.user).update(correct3=False)

        elif (id==3):
            Answerset.objects.filter(student=request.user).update(Answer4=request.POST.getlist('check')[0])
            uanswer = Answerset.objects.filter(student=request.user).values('Answer4')[0]['Answer4']
            aanswer = Questions.objects.filter(Question_No=id).values('answer')[0]['answer']
            if (uanswer==aanswer):
                Answerset.objects.filter(student=request.user).update(correct4=True)
            else:
                Answerset.objects.filter(student=request.user).update(correct4=False)

        elif (id==4):
            Answerset.objects.filter(student=request.user).update(Answer5=request.POST.getlist('check')[0])
            uanswer = Answerset.objects.filter(student=request.user).values('Answer5')[0]['Answer5']
            aanswer = Questions.objects.filter(Question_No=id).values('answer')[0]['answer']
            if (uanswer==aanswer):
                Answerset.objects.filter(student=request.user).update(correct5=True)
            else:
                Answerset.objects.filter(student=request.user).update(correct5=False)
        elif (id==5):
            Answerset.objects.filter(student=request.user).update(Answer6=request.POST.getlist('check')[0])
            uanswer = Answerset.objects.filter(student=request.user).values('Answer6')[0]['Answer6']
            aanswer = Questions.objects.filter(Question_No=id).values('answer')[0]['answer']
            if (uanswer==aanswer):
                Answerset.objects.filter(student=request.user).update(correct6=True)
            else:
                Answerset.objects.filter(student=request.user).update(correct6=False)
        elif (id==6):
            Answerset.objects.filter(student=request.user).update(Answer7=request.POST.getlist('check')[0])
            uanswer = Answerset.objects.filter(student=request.user).values('Answer7')[0]['Answer7']
            aanswer = Questions.objects.filter(Question_No=id).values('answer')[0]['answer']
            if (uanswer==aanswer):
                Answerset.objects.filter(student=request.user).update(correct7=True)
            else:
                Answerset.objects.filter(student=request.user).update(correct7=False)
    
    sr=id+1
    print(sr)

    print(id)
    if (sr==8):
        xyz = Answerset.objects.filter(student=request.user).values('correct1','correct2','correct3','correct4','correct5','correct6','correct7')
        sum = 0
        notattempt=0
        #total = sum+
        #print(xyz[0]['correct2'])
        if (xyz[0]['correct1']==True):
            sum=sum+1
        elif (xyz[0]['correct1']==None):
            notattempt = notattempt+1
        
        if (xyz[0]['correct2']==True):
            sum=sum+1
        elif (xyz[0]['correct2']==None):
            notattempt = notattempt+1
        
        if (xyz[0]['correct3']==True):
            sum=sum+1
        elif (xyz[0]['correct3']==None):
            notattempt = notattempt+1
        
        if (xyz[0]['correct4']==True):
            sum=sum+1
        elif (xyz[0]['correct4']==None):
            notattempt = notattempt+1
        
        if (xyz[0]['correct5']==True):
            sum=sum+1
        elif (xyz[0]['correct5']==None):
            notattempt = notattempt+1
        
        if (xyz[0]['correct6']==True):
            sum=sum+1
        elif (xyz[0]['correct6']==None):
            notattempt = notattempt+1
        
        if (xyz[0]['correct7']==True):
            sum=sum+1
        elif (xyz[0]['correct7']==None):
            notattempt = notattempt+1
        percentage = round((sum*100)/7,2)
        total = 7
        print(total)

        attempted=7-notattempt
        Answerset.objects.filter(student=request.user).update(marks=percentage)
        send = Answerset.objects.filter(student=request.user).values()
        return render(request,"result.html",{'data':send,'sum':sum,'attempted':attempted,'total':total})
    else:
        x = Questions.objects.filter(Question_No=id).values()
        return render(request,"start.html",{'question':x[0]['Question'],'id':x[0]['id'],'opt1':x[0]['option1'],'opt2':x[0]['option2'],'opt3':x[0]['option3'],'opt4':x[0]['option4']})

    
    

def loginpage(request):
    if (request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        if (user is not None):
            login(request,user)
            Answerset.objects.create(student=request.user)
            return redirect('/start/0')
        else:
            return redirect('/loginpage')
    

    return render(request,"login.html")

def register(request):
    form = createuserform(request.POST)
    if (request.method=='POST'):
        if (form.is_valid()):
            form.save()
    

    return render(request,"register.html",{'forms':form})



