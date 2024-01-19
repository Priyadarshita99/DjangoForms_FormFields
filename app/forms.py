from django import forms

g=[['MALE','MalE'],['FEMALE','FemalE']]  #key = saved in Database as value #value = show in html page
c=[['PYTHON','PYTHON'],('Django','Django'),['SQL','SQL']]

class NameForm(forms.Form):
    Sname=forms.CharField()
    Sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':5}))
    #gender=forms.ChoiceField(choices=g)                                                 #dropdown
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c)
    #course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)     #dropdown