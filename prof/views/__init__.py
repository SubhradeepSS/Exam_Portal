from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# separate views import
from .exam import *
from .group import *
from .question import *
from .question_paper import *
from .student import *

def index(request):
    prof = request.user
    return render(request, 'prof/index.html', {'prof': prof })