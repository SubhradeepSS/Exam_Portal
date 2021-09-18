from django.shortcuts import render
from main.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def view_students(request):
    prof = request.user
    return render(request, 'prof/student/view_students.html', {
        'students': User.objects.filter(groups__name='Student'), 'prof': prof
    })
    