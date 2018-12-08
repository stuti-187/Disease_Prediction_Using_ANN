from profile_user.models import user_details
from django import forms

class UserForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput)
    DateofBirth=forms.DateField(widget=forms.DateInput)
    email_id=forms.EmailField()

    class Meta:
        model=user_details
        fields=['first_name','last_name','email_id','DateofBirth','password']


class Userdata(forms.ModelForm):
    #password=forms.CharField(widget=forms.PasswordInput)

    gender=forms.CharField(widget=forms.TextInput)
    address=forms.CharField(widget=forms.TextInput)
    city=forms.CharField(widget=forms.TextInput)
    state=forms.CharField(widget=forms.TextInput)
    zip=forms.CharField(widget=forms.TextInput)
    phonen=forms.CharField(widget=forms.TextInput)
    class Meta:
        model=user_details
        fields=['gender','address','city','state','zip','phonen']


class Userauth(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=user_details
        fields=['email_id', 'password']

class Medicaldata(forms.ModelForm):
    blood_group = forms.CharField(label="Blood Group")
    drug_allergy = forms.BooleanField(label="Any History", initial=False)
    addict_hist = forms.BooleanField(label="Addiction history", initial=False)
    psych_ill = forms.BooleanField(label="Any illness", initial=False)
    hypertension = forms.BooleanField(label="Hypertension", initial=False)
    diabetes = forms.BooleanField(label="Diabetes", initial=False)
    asthma = forms.BooleanField(label="Asthma", initial=False)
    bronchites = forms.BooleanField(label="Bronchites", initial=False)
    fits = forms.BooleanField(label="Fits", initial=False)
    any_congential = forms.BooleanField(label="Congential Diseases", initial=False)
    surgery_accident = forms.CharField(label="Any previous surgeries/accidents")
    drug_intake = forms.BooleanField(label="Any Drug Intake", initial=False)
    other = forms.CharField(label="Addiction history")

    class Meta:
        model=user_details
        fields=['blood_group','drug_allergy','addict_hist','psych_ill','hypertension',
                'diabetes','asthma','bronchites','fits','any_congential','surgery_accident','drug_intake','other']


class passwordchange(forms.ModelForm):
    opassword = forms.CharField(widget=forms.PasswordInput, label="Old Password")
    npassword = forms.CharField(widget=forms.PasswordInput, label="New Password")

    class Meta:
        model = user_details
        fields = ['opassword', 'npassword']
