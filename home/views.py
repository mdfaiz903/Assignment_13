from django.shortcuts import render,HttpResponseRedirect
from . forms import contact_form
from . models import contact_model
# Create your views here.
def homeview(request):
    if request.method=='GET':
        frm = contact_form(request.GET)
        if frm.is_valid():
            f_name = frm.cleaned_data['F_name']
            L_name = frm.cleaned_data['L_name']
            Phone = frm.cleaned_data['Phone']
            Email = frm.cleaned_data['Email']
            Text = frm.cleaned_data['Text']
            form = contact_model(first_name=f_name,last_name=L_name,phone=Phone,email=Email,content=Text)
            form.save()
            # return HttpResponseRedirect('/success/')
    else:
        frm = contact_form()

    return render(request,'home/homeview.html',{'form':frm})

