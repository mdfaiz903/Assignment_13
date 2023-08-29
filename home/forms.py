from  django import forms 
class contact_form(forms.Form):
    F_name = forms.CharField(max_length=50,label='First Name')
    L_name = forms.CharField(max_length=50,label='Last Name')
    Phone = forms.CharField(
        max_length=15,
        initial='+880',
    )
    Email = forms.EmailField()
    Text = forms.CharField(
        widget=forms.Textarea(attrs={'rows':5,'colms':30})
    )

