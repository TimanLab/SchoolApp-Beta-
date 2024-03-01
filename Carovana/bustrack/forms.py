# forms.py

from django import forms
from .models import Child, BusStop, Login
from .models import Parent, Bus
from .models import BusMileage, Feedback
from .models import PopRegister, Exclusion, Operator

class OperatorForm(forms.Form):
    model = Operator
    fields = ['name','bus']
    
class PopRegisterForm(forms.ModelForm):
    class Meta:
        model = PopRegister
        fields = ['child', 'operator', 'status']

class ExclusionForm(forms.ModelForm):
    class Meta:
        model = Exclusion
        fields = ['child', 'reason']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username','password']

class BusMileageForm(forms.ModelForm):
    class Meta:
        model = BusMileage
        fields = ['bus', 'initial_mileage']


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name','bus']

class ChildForm(forms.Form):
    class Meta:
        model = Child
        fields = ['name','ucs_number','grade']
       
class BusStopForm(forms.Form):
    class Meta:
        model = BusStop
        fields = ['bus_stage_name','pick_drop_time']
       
class BusForm(forms.Form):
    model = Bus
    fields = ['number']
  
    
class FeedbackForm(forms.Form):
    model = Feedback
    fields = ['message']
   
