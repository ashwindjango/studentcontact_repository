from django.shortcuts import render
from .models import StudentData
from .forms import StudentForm
from django.http.response import HttpResponse

def student_view(request):
    if request.method == "POST":
        sform = StudentForm(request.POST)
        if sform.is_valid():
            sname1=request.POST.get('sname')
            fname1=request.POST.get('fname')
            sloc1=request.POST.get('sloc')
            scontact1=request.POST.get('scontact')
            sgender1=request.POST.get('sgender')
            a= StudentData(
                sname=sname1,
                fname=fname1,
                sloc=sloc1,
                scontact=scontact1,
                sgender=sgender1,
            )
            a.save()
            sform=StudentForm()
            return render(request, 'studentdata.html', {'abcd':sform})
        else:
            return HttpResponse("User Invalid Data")
    else:
        sform=StudentForm()
        return render( request, 'studentdata.html', {'abcd': sform})



# Create your views here.
