from django import forms
from symptomchecker.models import Diseases_Symptoms

class SymptomForm(forms.ModelForm):
    age_group=forms.ChoiceField(choices=(
    ("Newborn (0-28 days)","Newborn (0-28 days)"),
    ("Infant (29 days-1 year)","Infant (29 days-1 year)"),
    ("Younger Child (1 year-5 years)","Younger Child (1 year-5 years)"),
    ("Older Child (6-12 years)","Older Child (6-12 years)"),
    ("Adolescent (13-16 years)","Adolescent (13-16 years)"),
    ("Young Adult (17-29 years)","Young Adult (17-29 years)"),
    ("Adult (30-39 years)","Adult (30-39 years)"),
    ("Adult (40-49 years)","Adult (40-49 years)"),
    ("Adult (50-64 years)","Adult (50-64 years)"),
    ("Senior (65 years-over)","Senior (65 years-over)")), widget=forms.Select(),label="age", required=True)

    gender=forms.ChoiceField(choices=(
        ("Male","Male"),
        ("Female","Female")),widget=forms.RadioSelect(),label="gender",required=True,initial='none')
    is_pregnant=forms.BooleanField(label="is pregnant",initial=False)
    symptom1=forms.CharField(max_length=250,required=True)
    symptom2 = forms.CharField(max_length=250,required=True)
    symptom3 = forms.CharField(max_length=250,required=True)
    symptom4 = forms.CharField(max_length=250, required=True)

    class Meta:
        model=Diseases_Symptoms
        fields=['symptom1','symptom2','symptom3','symptom4','age_group','gender','is_pregnant']

class symform(forms.Form):
    symptom1=forms.BooleanField(label="Agitation",initial=False)
    symptom2 = forms.BooleanField(label="Apyrexial", initial=False)
    symptom3 = forms.BooleanField(label="Ascites", initial=False)
    symptom4 = forms.BooleanField(label="Asthenia", initial=False)
    symptom5 = forms.BooleanField(label="Blackout", initial=False)
    symptom6 = forms.BooleanField(label="Bradycardia", initial=False)
    symptom7 = forms.BooleanField(label="Breath sounds decreased", initial=False)
    symptom8 = forms.BooleanField(label="Chest tightness", initial=False)
    symptom9 = forms.BooleanField(label="Chill", initial=False)
    symptom10 = forms.BooleanField(label="Consciousness clear", initial=False)
    symptom11 = forms.BooleanField(label="Cough", initial=False)
    symptom12 = forms.BooleanField(label="Decreased body weight", initial=False)
    symptom13 = forms.BooleanField(label="Diarrhea", initial=False)
    symptom14= forms.BooleanField(label="Difficulty", initial=False)
    symptom15= forms.BooleanField(label="Distress respiratory", initial=False)
    symptom16= forms.BooleanField(label="Drowsiness", initial=False)
    symptom17= forms.BooleanField(label="Dyspnea", initial=False)
    symptom18= forms.BooleanField(label="Facial Paresis", initial=False)
    symptom19= forms.BooleanField(label="Fatigue", initial=False)
    symptom20= forms.BooleanField(label="Feeling Hopeless", initial=False)
    symptom21 = forms.BooleanField(label="Feeling Suicidal", initial=False)
    symptom22= forms.BooleanField(label="Fever", initial=False)
    symptom23= forms.BooleanField(label="Guaiac positive", initial=False)
    symptom24= forms.BooleanField(label="Haemorrhage", initial=False)
    symptom25= forms.BooleanField(label="Hallucinations auditory", initial=False)
    symptom26= forms.BooleanField(label="Hallucinations visual", initial=False)
    symptom27= forms.BooleanField(label="Headache", initial=False)
    symptom28= forms.BooleanField(label="Hematuria", initial=False)
    symptom29 = forms.BooleanField(label="Hemodynamically stable", initial=False)
    symptom30 = forms.BooleanField(label="Homelessness", initial=False)
    symptom31 = forms.BooleanField(label="Hypokinesia", initial=False)
    symptom32 = forms.BooleanField(label="Hypotension", initial=False)
    symptom33 = forms.BooleanField(label="Intoxication", initial=False)
    symptom34 = forms.BooleanField(label="Irritable Mood", initial=False)
    symptom35 = forms.BooleanField(label="Lesion", initial=False)
    symptom36 = forms.BooleanField(label="Mass of body structure", initial=False)
    symptom37 = forms.BooleanField(label="Mental status changes", initial=False)
    symptom38 = forms.BooleanField(label="Mood depressed", initial=False)
    symptom39= forms.BooleanField(label="Nausea", initial=False)
    symptom40 = forms.BooleanField(label="Orthopnea", initial=False)
    symptom41 = forms.BooleanField(label="Pain", initial=False)
    symptom42 = forms.BooleanField(label="Pain abdominal", initial=False)
    symptom43 = forms.BooleanField(label="Pain chest", initial=False)
    symptom44 = forms.BooleanField(label="Patient non compliance", initial=False)
    symptom45 = forms.BooleanField(label="Pleuritic pain", initial=False)
    symptom46 = forms.BooleanField(label="Prostatism", initial=False)
    symptom47 = forms.BooleanField(label="Rale", initial=False)
    symptom48 = forms.BooleanField(label="Shortness of breath", initial=False)
    symptom49 = forms.BooleanField(label="Sleeplessness", initial=False)
    symptom50 = forms.BooleanField(label="Sore to touch", initial=False)

    class Meta:
        fields=['symptom1','symptom2','symptom3','symptom4','symptom5','symptom6','symptom7',
                'symptom8','symptom9','symptom10','symptom11','symptom12','symptom13','symptom14','symptom15',
                'symptom16','symptom17','symptom18','symptom19','symptom20','symptom21','symptom22','symptom23'
            , 'symptom24','symptom25','symptom26','symptom27','symptom28','symptom29','symptom30','symptom31'
            , 'symptom32','symptom33','symptom34','symptom35','symptom36','symptom37','symptom38','symptom39'
            , 'symptom40','symptom41','symptom42','symptom43','symptom44','symptom45','symptom46','symptom47',
                'symptom48','symptom49','symptom50']
