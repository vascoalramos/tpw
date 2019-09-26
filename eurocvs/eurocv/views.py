import json
import os

from django.shortcuts import render

from eurocvs.settings import STATIC_URL, STATICFILES_DIRS


# Create your views here.
def render_cv(request, name):
    cv_url = f"{STATICFILES_DIRS[0]}/json/eurocv_{name}.json"
    cv = json.loads(open(cv_url).read())["eurocv"]
    return render(request, "eurocv.html", cv)
