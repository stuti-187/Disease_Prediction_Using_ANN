from django.shortcuts import render
from django.template import loader,RequestContext,Context
from profile_user.models import user_details
from django.http import HttpResponse
from django.db.models import Q
from .forms import UserForm,Userauth,Userdata,Medicaldata,passwordchange
from recommended_doctors.models import hospital,DoctorData

# Create your views here.
def usercreate(request):
    if request.method == 'POST':
        q1 = request.POST.get("first_name")
        q2 = request.POST.get("last_name")
        q3 = request.POST.get("email_id")
        q4 = request.POST.get("DateofBirth")
        q5=request.POST.get("password")


        user_details.objects.create(first_name=q1, last_name=q2, email_id=q3, DateofBirth=q4, password=q5)

        return HttpResponse("You are now Registered!")

    else:
        form_class = UserForm()
        template = loader.get_template('profile_user/register.html')
        context = RequestContext(request, {'form': form_class})
        return HttpResponse(template.render(context))


def userlogin(request):
    if request.method=='POST':
        form=Userauth(request.POST)
        medform=Medicaldata()
        pform=passwordchange()
        if form.is_valid():
            email_id=form.cleaned_data['email_id']
            password=form.cleaned_data['password']
            value = user_details.objects.get(email_id=email_id)
            if value.password==password:
                request.session['first_name']=value.first_name
                template = loader.get_template('profile_user/Profile.html')
                context = RequestContext(request, { 'name': request.session['first_name'],'lname': value.last_name,
                                                    'dob':value.DateofBirth, 'gender':value.gender,'email':value.email_id,
                                                    'address':value.address,'city':value.city,'state':value.state,
                                                    'zip':value.zip,'phone':value.phonen,'blood_group': value.blood_group, 'drug_allergy': value.drug_allergy,
                                           'addhist': value.addict_hist,
                                           'psych_ill': value.psych_ill, 'hypertension': value.hypertension,
                                           'bronchites': value.bronchites,
                                           'fits': value.fits, 'any_congential': value.any_congential,
                                           'surgery_accident': value.surgery_accident,
                                           'drug_intake': value.drug_intake, 'other': value.other,'medform':medform,'pform':pform})
                return HttpResponse(template.render(context))
            else:
                return HttpResponse("Wrong Password!")

    else:
        form = Userauth()
        template = loader.get_template('profile_user/login.html')
        context = RequestContext(request, {'form': form})
        return HttpResponse(template.render(context))

def useredit(request):
    firstname=request.session['first_name']
    medform = Medicaldata()
    pform = passwordchange()
    if request.method=='POST':
        #form = Userdata()
        value = user_details.objects.get(first_name=firstname)
        value.gender = request.POST.get("gender")
        value.address = request.POST.get("address")
        value.city = request.POST.get("city")
        value.state = request.POST.get("state")
        value.zip = request.POST.get("zip")
        value.phonen = request.POST.get("phonen")
        value.save()
        template = loader.get_template('profile_user/Profile.html')
        context = RequestContext(request, {'name': value.first_name,'lname':value.last_name,'blood_group': value.blood_group, 'drug_allergy': value.drug_allergy,
                                           'addhist': value.addict_hist,
                                           'psych_ill': value.psych_ill, 'hypertension': value.hypertension,
                                           'bronchites': value.bronchites,
                                           'fits': value.fits, 'any_congential': value.any_congential,
                                           'surgery_accident': value.surgery_accident,
                                           'drug_intake': value.drug_intake, 'medform':medform,'pform':pform,'other': value.other,'dob':value.DateofBirth, 'gender':value.gender,'email':value.email_id,'address':value.address,'city':value.city,'state':value.state,'zip':value.zip,'phone':value.phonen})
        return HttpResponse(template.render(context))
    else:
       # form=Userdata()
        value = user_details.objects.get(first_name=firstname)
        template = loader.get_template('profile_user/Profile.html')
        context = RequestContext(request, {'name': firstname,'lname':value.last_name, 'dob':value.DateofBirth, 'blood_group': value.blood_group, 'drug_allergy': value.drug_allergy,
                                           'addhist': value.addict_hist,
                                           'psych_ill': value.psych_ill, 'hypertension': value.hypertension,
                                           'bronchites': value.bronchites,
                                           'fits': value.fits, 'any_congential': value.any_congential,
                                           'surgery_accident': value.surgery_accident,
                                           'drug_intake': value.drug_intake, 'other': value.other,'medform':medform,'pform':pform,'gender':value.gender,'email':value.email_id,'address':value.address,'city':value.city,'state':value.state,'zip':value.zip,'phone':value.phonen})
        return HttpResponse(template.render(context))

def medhistedit(request):
    firstname = request.session['first_name']
    medform = Medicaldata()
    pform=passwordchange()
    if request.method == 'POST':
        value = user_details.objects.get(first_name=firstname)
        value.blood_group = request.POST.get("blood_group")
        value.drug_allergy = request.POST.get("drug_allergy")
        value.addict_hist = request.POST.get("addict_hist")
        value.diabetes=request.POST.get("diabetes")
        value.asthma = request.POST.get("asthma")
        value.psych_ill = request.POST.get("psych_ill")
        value.hypertension = request.POST.get("hypertension")
        value.bronchites = request.POST.get("bronchites")
        value.fits = request.POST.get("fits")
        value.any_congential = request.POST.get("any_congential")
        value.surgery_accident = request.POST.get("surgery_accident")
        value.drug_intake = request.POST.get("drug_intake")
        value.other = request.POST.get("other")
        value.save()
        template = loader.get_template('profile_user/Profile.html')
        context = RequestContext(request, {'name': firstname, 'lname': value.last_name, 'dob': value.DateofBirth,
                                           'blood_group': value.blood_group, 'drug_allergy': value.drug_allergy, 'addhist': value.addict_hist,
                                           'psych_ill': value.psych_ill, 'hypertension': value.hypertension, 'bronchites': value.bronchites,
                                           'fits': value.fits,'any_congential': value.any_congential,'surgery_accident':value.surgery_accident,
                                           'drug_intake':value.drug_intake,'other':value.other,'medform':medform,'pform':pform ,'gender':value.gender,'email':value.email_id,'address':value.address,'city':value.city,'state':value.state,'zip':value.zip,'phone':value.phonen})
        return HttpResponse(template.render(context))
    else:
        # form=Userdata()

        value = user_details.objects.get(first_name=firstname)
        template = loader.get_template('profile_user/Profile.html')
        context = RequestContext(request, {'name': firstname, 'lname': value.last_name, 'dob': value.DateofBirth,
                                           'blood_group': value.blood_group, 'drug_allergy': value.drug_allergy, 'addhist': value.addict_hist,
                                           'psych_ill': value.psych_ill, 'hypertension': value.hypertension, 'bronchites': value.bronchites,
                                           'fits': value.fits,'any_congential': value.any_congential,'surgery_accident':value.surgery_accident,
                                           'drug_intake':value.drug_intake,'other':value.other,'medform':medform,'pform':pform ,'gender':value.gender,'email':value.email_id,'address':value.address,'city':value.city,'state':value.state,'zip':value.zip,'phone':value.phonen})
        return HttpResponse(template.render(context))

def loggedinhome(request):
    firstname = request.session['first_name']
    template = loader.get_template('profile_user/medeasemain.html')
    context = RequestContext(request,{'name': firstname})
    return HttpResponse(template.render(context))


def changepassword(request):
    firstname = request.session['first_name']
    pform = passwordchange()
    medform=Medicaldata()
    if request.method == 'POST':
        value = user_details.objects.get(first_name=firstname)
        opass=request.POST['opassword']
        npass=request.POST['npassword']

        value.password=npass
        value.save()
        template=loader.get_template('profile_user/Profile.html')
        context = RequestContext(request, {'name': firstname, 'lname': value.last_name, 'dob': value.DateofBirth,
                                               'blood_group': value.blood_group, 'drug_allergy': value.drug_allergy,
                                               'addhist': value.addict_hist,
                                               'psych_ill': value.psych_ill, 'hypertension': value.hypertension,
                                               'bronchites': value.bronchites,'medform':medform,'pform':pform,
                                               'fits': value.fits, 'any_congential': value.any_congential,
                                               'surgery_accident': value.surgery_accident,
                                               'drug_intake': value.drug_intake, 'other': value.other, 'gender':value.gender,'email':value.email_id,'address':value.address,'city':value.city,'state':value.state,'zip':value.zip,'phone':value.phonen})
        return HttpResponse(template.render(context))

    else:
        value = user_details.objects.get(first_name=firstname)
        template = loader.get_template('profile_user/Profile.html')
        context = RequestContext(request, {'name': firstname, 'lname': value.last_name, 'dob': value.DateofBirth,
                                           'blood_group': value.blood_group, 'drug_allergy': value.drug_allergy,
                                           'addhist': value.addict_hist,
                                           'psych_ill': value.psych_ill, 'hypertension': value.hypertension,
                                           'bronchites': value.bronchites,
                                           'fits': value.fits, 'any_congential': value.any_congential,
                                           'surgery_accident': value.surgery_accident,
                                           'drug_intake': value.drug_intake, 'other': value.other, 'medform':medform,'pform': pform, 'gender':value.gender,'email':value.email_id,'address':value.address,'city':value.city,'state':value.state,'zip':value.zip,'phone':value.phonen})
        return HttpResponse(template.render(context))


def locatehospital(request):
    firstname = request.session['first_name']
    value = user_details.objects.get(first_name=firstname)
    user_add=value.address
    user_city=value.city
    user_state=value.state
    if user_city=="Noida" or user_city=="Ghaziabad" or user_city=="Faridabad" or user_city=="Gurgaon" or user_city=="New Delhi":
        names = hospital.objects.filter(
            Q(address__contains=user_add) |
            Q(city__exact="Noida") |
            Q(city__exact="Ghaziabad") |
            Q(city__exact="Faridabad") |
            Q(city__exact="Gurgaon") |
            Q(city__exact="New Delhi") |
            Q(state__exact=user_state)
        )
    else:
        names = hospital.objects.filter(
            Q(address__contains=user_add) |
            Q(city__exact=user_city) |
            Q(state__exact=user_state)
        )

    template = loader.get_template('profile_user/hospital_list.html')
    context = RequestContext(request,{'index':names, 'name':firstname})
    return HttpResponse(template.render(context))

def logout(request):
    del request.session['first_name']
    template = loader.get_template('home/home.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
