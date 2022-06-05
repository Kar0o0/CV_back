from django.shortcuts import render,redirect
from .models import About, Abilities, Projects, Contact
from .forms import ContactModelForm
from django.views.generic.edit import CreateView

# Create your views here.


def personal_info(request):
    personal_information = About.objects.get(pk=1)
    abilities = Abilities.objects.all()
    projects = Projects.objects.all()
    contact_form = ContactModelForm(request.POST)
    if contact_form.is_valid():
        contact = Contact(
            name=contact_form.cleaned_data.get('name'),
            email=contact_form.cleaned_data.get('email'),
            subject=contact_form.cleaned_data.get('subject'),
            message=contact_form.cleaned_data.get('message')
        )

        contact.save()
        return redirect('/')
    else:
        contact_form = ContactModelForm
    context = {
        'info' : personal_information,
        'abilities' : abilities,
        'projects' : projects,
        'contact_form' : contact_form
    }
    return render(request,'the_main/theBody.html',context)