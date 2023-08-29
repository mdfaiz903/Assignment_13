from django.shortcuts import render
from home . forms import contact_form
# Create your views here.
def contact(request):
   if request.method=='POST':
      frm = contact_form(request.POST)
      if frm.is_valid():
         frm.save
   else:
      frm = contact_form()
   return render(request,'contact/cont.html',{'form':frm})