from django import forms
from salaire.models import Cost, Pricing, Contract, Month, Day, Summary, ContractEnd

class CostForm(forms.ModelForm):
   class Meta:
     model = Cost
     fields = '__all__'

class PricingForm(forms.ModelForm):
  class Meta:
     model = Pricing
     fields = '__all__'

class ContractForm(forms.ModelForm):
  pricing = forms.ModelChoiceField(queryset=Pricing.objects.all())
  class Meta:
     model = Contract
     fields = '__all__'

class MonthForm(forms.ModelForm):
  name = forms.ModelChoiceField(queryset=Contract.objects.all())
  cost = forms.ModelChoiceField(queryset=Cost.objects.all())
  class Meta:
     model = Month
     fields = '__all__'

class DayForm(forms.ModelForm):
   class Meta:
      model = Day
      exclude = ['name']
   def __init__(self, *args, **kwargs):
      super(DayForm, self).__init__(*args, **kwargs)  
      self.fields['day'].widget.attrs['readonly'] = True
      self.fields['day_name'].widget.attrs['readonly'] = True
      self.fields['day'].widget.attrs['readonly'] = True
      self.fields['day'].widget.attrs['class'] = 'no-border'
      self.fields['day_name'].widget.attrs['class'] = 'no-border'
      self.fields['supp_hours_number'].widget.attrs['class'] = 'small'

class SummaryForm(forms.ModelForm):
   cost = forms.ModelChoiceField(queryset=Cost.objects.all())
   class Meta:
     model = Summary
     fields = '__all__'

class ContractEndForm(forms.ModelForm):
   name = forms.ModelChoiceField(queryset=Contract.objects.all())
   class Meta:
     model = ContractEnd
     fields = '__all__'
