from django.shortcuts import render
from app.models import Task
from app.forms import NewTaskForm

# Create your views here.
def tasks(request):
    task_lst = Task.objects.order_by('time_stamp')
    # task_dict = {'tasks':task_lst}

    form = NewTaskForm()
    
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print('ERROR FORM INVALID')
    return render(request,'app.html',{'form':form,'tasks':task_lst})