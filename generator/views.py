from django.shortcuts import render, HttpResponse, redirect
from .models import Faculty, add
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from .forms import UpdateForm

# Create your views here.
def home(request):
    return render(request, 'generator/index.html')

def about(request):
    return render(request,'generator/about.html')


def delete(request):
    return render(request,'generator/deleteQ.html')

def update(request, pk):
    adds = add.objects.get(questionId=pk)
    form = UpdateForm(instance=adds)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=adds)
        if form.is_valid():
            return redirect('/')
            form.save()

    context = {'form': form}
    return render(request, 'generator/updateQ.html', context)

def generate(request):
    return render(request,'generator/generateQ.html')

def login(request):
    if request.method == "POST":
        print(request)
    return render(request, 'generator/login.html')

def handleSignup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        course = request.POST['course']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #check for errorneous inputs

        # create the user

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        # return redirect('generator/addQ')
        return HttpResponse('generator/signup')

    else :
        return HttpResponse('404 - not found')




def addQ(request):
    # adds = add.objects.all(id=pk_test)

    if request.method == 'POST':
        questionId=request.POST.get('questionId', '')
        EnterTheQuestion = request.POST.get('EnterTheQuestion', '')
        Subject = request.POST.get('Subject', '')
        DifficultLevel = request.POST.get('DifficultLevel', '')
        unitNo = request.POST.get('unitNo', '')
        year = request.POST.get('year', '')
        Marks_alloted = request.POST.get('Marks_alloted', '')
        Module = request.POST.get('Module', '')
        Semester = request.POST.get('Semester', '')
        Subject_code = request.POST.get('Subject_code', '')

        addition=add(questionId=questionId, EnterTheQuestion=EnterTheQuestion, DifficultLevel=DifficultLevel, unitNo=unitNo, Subject=Subject, year=year, Marks_alloted=Marks_alloted,
                 Module=Module, Semester=Semester, Subject_code=Subject_code)
        addition.save()
    return render(request, 'generator/addQ.html')

def create(request):
    adds = add.objects.all()
    context = {'adds': adds}
    return render(request, 'generator/create.html', context)

