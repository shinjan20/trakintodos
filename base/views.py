from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Todo,User
from .forms import todoform,registrationform
from django.core.paginator import Paginator
from django.core.mail import send_mail
import environ
env = environ.Env()
environ.Env.read_env()

# Create your views here.

def index(request):
    context={}
    if request.user.is_authenticated==True :
        param=request.GET.get('q') if (request.GET.get('q')!=None) else ''
        todos = Todo.objects.filter(Q(user=request.user) & (Q(title__icontains=param) | Q(description__icontains=param))).order_by('-created_at')
        paginator = Paginator(todos,4)
        page_num = request.GET.get('page')
        if page_num == None:
            page_num = 1
        else :
            page_num = str(page_num)
        selected_todos = paginator.get_page(page_num)
        pending = Todo.objects.filter(Q(user=request.user) & Q(is_completed=False)).count()
        context={'todos':selected_todos,'pending':pending}
    return render(request,'base/home.html',context)

def registerpage(request):
    process="register"
    if request.user.is_authenticated : 
        return HttpResponseRedirect('/')
    form = registrationform()
    if request.method == 'POST' : 
            form = registrationform(request.POST)
            if form.is_valid():
                new_user=form.save(commit=False)
                new_user.save()
                login(request,new_user)
                send_mail('Registration complete',f'Welcome {new_user.username} to our website.Thank you for choosing our services.',env('SENDING_EMAIL'),[new_user.email])
                return HttpResponseRedirect('/')
            else : 
                messages.error(request,'Please fill up the form properly !!!') 
    return render(request,'base/login-register.html',{
        'process' : process,
        'form' : form
    })

def loginpage(request):
    if request.user.is_authenticated : 
        return HttpResponseRedirect('/')
    process = 'Login'
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
        except :
                messages.error(request,'User does not exist !!!')
                return HttpResponseRedirect('/accounts/login/')

        user = authenticate(request,email=email,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else :
            messages.error(request,'User or password do not exist !!!')
            return HttpResponseRedirect('/accounts/login/')
       
    return render(request,'base/login-register.html',{
        'process' : process
    })

def logoutpage(request):
    if request.user.is_authenticated == False : 
        return HttpResponseRedirect('/')
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/accounts/login/')
def createtodo(request):
    form=todoform()
    if request.method == 'POST':
        form = todoform(request.POST)
        if form.is_valid():
            new_todo=form.save(commit=False)
            new_todo.user=request.user
            new_todo.save()
            return HttpResponseRedirect('/')
    return render(request,'base/create-todo.html',{
        'form':form,
    })

@login_required(login_url='/accounts/login/')
def updatetodo(request,pk):
    todo = Todo.objects.get(id=pk)
    form = todoform(instance=todo)
    if request.method == 'POST':
        form = todoform(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'base/update-todo.html',{
        'form' : form,
    })

@login_required(login_url='/accounts/login/')
def deletetodo(request,pk):
    todo = Todo.objects.get(id=pk)
    if(request.user !=  todo.user):
        return HttpResponse('you are not allowed to do that')
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect('/')
    return render(request,'base/delete-todo.html',{
        'obj': todo,
    })
    

@login_required(login_url='/accounts/login/')
def detailstodo(request,pk):
    todo = Todo.objects.get(id=pk)
    return render(request,'base/details-todo.html',{
        'todo' : todo,
    })