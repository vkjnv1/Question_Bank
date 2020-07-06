from django.shortcuts import render, HttpResponse, redirect
from .models import Faculty, add
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from .forms import UpdateForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'generator/index.html')

def about(request):
    return render(request,'generator/about.html')


def delete(request, myid):
    adds = add.objects.get(questionId=myid)
    form = UpdateForm(instance=adds)

    if request.method == 'POST':
        adds.delete()
        return('/')
    context = {'form': form}
    return render(request, 'generator/deleteQ.html', context)

def update(request, myid):

    adds = add.objects.get(questionId=myid)
    form = UpdateForm(instance=adds)
    #context= {'form': form}
    #print(adds)
    #form = UpdateForm(instance=adds)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=adds)
        if form.is_valid():
            form.save()
            request.META('/generator/create/')
            return redirect('/')
    context = {'form': form}
    return render(request, 'generator/updateQ.html', context)

def generate(request):
    return render(request, 'generator/generateQ.html')

def login(request):
    context = {}
    return render(request, 'generator/login.html', context)

def handleSignup(request):
    form = CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}

    #if request.method == 'POST':
        #username = request.POST['username']
        #fname = request.POST['fname']
        #lname = request.POST['lname']
        #email = request.POST['email']
        #subject = request.POST['subject']
        #course = request.POST['course']
        #pass1 = request.POST['pass1']
        #pass2 = request.POST['pass2']

        #check for errorneous inputs

        # create the user

        #myuser = User.objects.create_user(username,email,pass1)
        #myuser.first_name = fname
        #myuser.last_name = lname
        #myuser.save()
        #messages.success(request,"Your account has been successfully created")
        # return redirect('generator/addQ')
        #return HttpResponse('generator/signup')

    #else :
        #return HttpResponse('404 - not found')
    return render(request, 'generator/signup.html', context)

def addQ(request):
    # adds = add.objects.all(id=pk_test)

    if request.method == 'POST':
        # questionId=request.POST.get('questionId', '')
        EnterTheQuestion = request.POST.get('EnterTheQuestion', '')
        Subject = request.POST.get('Subject', '')
        DifficultLevel = request.POST.get('DifficultLevel', '')
        unitNo = request.POST.get('unitNo', '')
        year = request.POST.get('year', '')
        Marks_alloted = request.POST.get('Marks_alloted', '')
        Module = request.POST.get('Module', '')
        Semester = request.POST.get('Semester', '')
        Subject_code = request.POST.get('Subject_code', '')

        addition = add(EnterTheQuestion = EnterTheQuestion, DifficultLevel = DifficultLevel, unitNo = unitNo, Subject = Subject, year = year, Marks_alloted = Marks_alloted,
                 Module = Module, Semester = Semester, Subject_code = Subject_code)
        addition.save()
    return render(request, 'generator/addQ.html')

def create(request):
    adds = add.objects.all()
    context = {'adds': adds}
    return render(request, 'generator/create.html', context)


