from django import forms


# class forname(forms.Form):
#     n1=forms.CharField()
#     n2=forms.CharField()
#     n3=forms.CharField()
#     #n3=forms.FileField().


class S_signup(forms.Form):
    name=forms.CharField(max_length=25,label="Your name", widget=forms.TextInput(attrs={"class":"ask-name","placeholder": "Name"}))
    section=forms.CharField(max_length=25,label="Your name", widget=forms.TextInput(attrs={"class":"ask-name","placeholder": "Section"}))
    admno=forms.CharField(max_length=7, min_length=7,label="Your Admission number", widget=forms.TextInput(attrs={"class":"ask-name" , "placeholder": "Admission No."}))
    password=forms.CharField(min_length=8,label="password", widget=forms.TextInput(attrs={"class":"ask-password", "placeholder": "Password (minimum 8 characters)", "type": "password"}))
    repassword=forms.CharField(min_length=8,label="repassword", widget=forms.TextInput(attrs={"class":"ask-password", "placeholder": "Re-enter Password", "type": "password"}))

class S_login(forms.Form):
    admno=forms.CharField(max_length=7, min_length=7,label="Your Admission number sravan", widget=forms.TextInput(attrs={"class":"ask" , "placeholder": "Admission No."}))
    password=forms.CharField(min_length=8,label="password", widget=forms.TextInput(attrs={"class":"ask", "placeholder": "Password", "type": "password"}))  