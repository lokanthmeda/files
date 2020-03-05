from django.shortcuts import render
from .models import Collegedata
def register(request):

    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        father=request.POST.get('father')
        mobile=request.POST.get('mobile')
        mother=request.POST.get('mother')
        address=request.POST.get('address')
        pwd=request.POST.get('password')
        data=Collegedata(
           First_name=fname,
           Last_name=lname,
           dob=dob,
           email=email,
           Father_name=father,
           mobile=mobile,
           Mother_name=mother,
           address=address,
           password=pwd
        )
        data.save()
        return render(request, 'student/rform.html')
    else:
        return render(request,'student/rform.html')