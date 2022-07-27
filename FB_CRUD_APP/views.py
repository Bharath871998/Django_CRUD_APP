from django.shortcuts import  render, redirect
from .models import Student
# from django.views import View
from .forms import StudentForm
# Create your views here.

def home(request):
    data = Student.objects.all()
    return render(request ,"crud/home.html", {"studata": data})

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()   
    return render(request, 'crud/add.html', {'form': form})
    
    
def edit(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form = StudentForm()
        else:
            stu = Student.objects.get(id = id)
            sform = StudentForm(instance=stu)
        return render(request, 'crud/edit.html', {'form': sform})
    else:
        if id == 0:
            sform = StudentForm(request.POST)
        else:
            student = Student.objects.get(id=id)
            sf = StudentForm(request.POST, instance = student)
            if sf.is_valid():
                sf.save()
                return redirect('/')
            else:
                return render(request, 'crud/edit.html', {'form': sform})
    
    
def delete(request,id):
    dform = Student.objects.get(id=id)
    dform.delete()
    return redirect('/')
        
    
    
    