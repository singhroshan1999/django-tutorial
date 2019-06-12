from django import forms
from django.core import validators
from first_app.models import User,UserPortfolio
from django.contrib.auth.models import User as User2


def is_z(val):
    if val[0].lower() != 'z':
        raise forms.ValidationError("no z")
    
class FormName(forms.Form):
    name = forms.CharField(validators = [is_z])
    email = forms.EmailField()
    vemail = forms.EmailField(label = "Re-enter email")
    text = forms.CharField(widget = forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])
    # def clean_botcatcher(self):  ### using django.core --> validators instead
    #     botcat = self.cleaned_data['botcatcher']
    #     if len(botcat) > 0:
    #         raise forms.ValidationError("bot bot bot!")
    #     return botcat
    
    def clean(self):  # clean all data at once
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['vemail']
        if email != vemail:
            raise forms.ValidationError("email mismatch")

class NewUsers(forms.ModelForm):
    class Meta():
        model = User2
        fields = '__all__'
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User2
        fields = ('username','email','password')
class UserPortfolioForm(forms.ModelForm):
    class Meta():
        model = UserPortfolio
        fields = ('portfolio','profile_pic')