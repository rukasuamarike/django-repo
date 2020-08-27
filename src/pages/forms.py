from django import forms

from .models import Log
class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = {
            'user',
            'time',
            'ip',
        }



   # def clean_user(self,*args,**kwargs):
    #    user = self.cleaned_data.get("user")
    #    if "key" in user:
    #        return user
    #   if not "l" in user:
    #    raise forms.ValidationError("not valid user")
    #    else:
    #        raise forms.ValidationError("not valid user")
class RawLogForm(forms.Form):
    user        = forms.CharField()
    time        = forms.CharField()#(required = True,
                                  #widget = forms.Textarea(
                                  #    attrs={
                                  #        "class":"new-class-name two",
                                  #        "rows": 69
                                  #    }
                                  #))
    ip          = forms.CharField()