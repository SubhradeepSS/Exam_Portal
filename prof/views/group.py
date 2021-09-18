from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def create_student_group(request):
    prof = request.user

    if request.method == "POST":
        form = Group_Form(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.professor = prof
            group.save()
            form.save_m2m()
            
            return redirect('prof:view_groups')

    return render(request, 'prof/group/addview_groups.html', {
        'special_students_db': Special_Students.objects.filter(professor=prof), 'prof': prof, 'groupForm': Group_Form()
    })
    

def view_specific_group(request, group_id):
    prof = request.user
    group = Special_Students.objects.get(professor=prof, pk=group_id)

    return render(request, 'prof/group/view_specific_group.html', {
        'group': group, 'prof': prof, 'group_students': group.students.all()
    })
    

def view_student_in_group(request, group_id):
    prof = request.user
    group = Special_Students.objects.get(professor=prof, pk=group_id)

    if request.method == 'POST':
        student_username = request.POST['username']
        student = User.objects.get(username=student_username)
        group.students.add(student)

    return render(request, 'prof/group/view_special_stud.html', {
        'students': group.students.all(), 'group': group, 'prof': prof
    })
    

def edit_group(request, group_id):
    prof = request.user 
    group = Special_Students.objects.get(professor=prof, pk=group_id)
    group_form = Group_Form(instance=group)
    
    if request.method == "POST":
        form = Group_Form(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('prof:view_groups')

    return render(request, 'prof/group/edit_group.html', {
        'prof':prof, 'group':group, 'group_form': group_form
    })
    

def delete_group(request, group_id):
    prof = request.user
    Special_Students.objects.filter(professor=prof, pk=group_id).delete()
    return redirect('prof:view_groups')
    