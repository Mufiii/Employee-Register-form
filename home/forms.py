from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm) :
  
  class Meta:
    model = Employee              
    fields = ('fullName','mobile','emp_code','position')
    labels = {
        'fullName' : 'Full Name',
        'emp_code' : 'Emp Code',
        'position' : 'Position'
    }
    
  def __init__(self,*args,**kwargs) :
    super(EmployeeForm,self).__init__(*args,**kwargs)
    self.fields['position'].empty_label = 'Select'
    self.fields["position"].widget.attrs["class"] = "form-control"
    self.fields['emp_code'].required = False
    