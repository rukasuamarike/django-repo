from django import forms

from .models import Blog
class IpForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = {
            "title",
            "desc",
        }



   # def clean_user(self,*args,**kwargs):
    #    user = self.cleaned_data.get("user")
    #    if "key" in user:
    #        return user
    #   if not "l" in user:
    #    raise forms.ValidationError("not valid user")
    #    else:
    #        raise forms.ValidationError("not valid user")
class RawBlogForm(forms.Form):
    title        = forms.CharField()
    desc        = forms.CharField()#(required = True,
                                  #widget = forms.Textarea(
                                  #    attrs={
                                  #        "class":"new-class-name two",
                                  #        "rows": 69
                                  #    }
                                  #))


