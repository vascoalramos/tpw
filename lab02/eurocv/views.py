from django.shortcuts import render, HttpResponse

from .models import *


# Create your views here.
def render_cv(request, name):
    data = {}
    try:
        person = Person.objects.get(first_name=name)
        data["person"] = person
        phones = list(Phone.objects.filter(person=person))
        data["phones"] = phones
        faxes = list(Fax.objects.filter(person=person))
        data["faxes"] = faxes
        emails = list(Email.objects.filter(person=person))
        data["emails"] = emails
        # there are still missing fields, I didn't added them because it was just the same logic
        return render(request, "eurocv.html", data)


    except Person.DoesNotExist:
        return HttpResponse("<h1>The specified person does not exist!</h1>")
