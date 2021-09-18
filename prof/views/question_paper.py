from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def make_paper(request):
    prof = request.user

    if request.method == 'POST' and not request.POST.get('presence', False):
        add_question_in_paper(request)

    elif request.method == 'POST' and request.POST.get('presence', False):
        title = request.POST['title']
        Question_Paper.objects.filter(professor=prof, qPaperTitle=title).first().delete()

    return render(request, 'prof/question_paper/qpaper.html', {
        'qpaper_db': Question_Paper.objects.filter(professor=prof), 'prof': prof
    })



def add_question_in_paper(request):
    prof = request.user

    if request.method == 'POST' and request.POST.get('qpaper', False):
        paper_title = request.POST['qpaper']
        question_paper = Question_Paper(professor=prof, qPaperTitle=paper_title)
        question_paper.save()

        left_ques = []
        curr_paper_questions = question_paper.questions.all()
        for ques in Question_DB.objects.filter(professor=prof):
            if ques not in curr_paper_questions:
                left_ques.append(ques)

        return render(request, 'prof/question_paper/addquestopaper.html', {
            'qpaper': question_paper,
            'question_list': left_ques, 'prof': prof
        })

    elif request.method == 'POST' and request.POST.get('title', False):
        addques = request.POST['title']
        ques_ = Question_DB.objects.filter(professor=prof, qno=addques).first()
        title = request.POST['papertitle']
        ques_paper = Question_Paper.objects.filter(professor=prof, qPaperTitle=title).first()
        ques_paper.questions.add(ques_)
        ques_paper.save()

        left_ques = []
        curr_paper_questions = ques_paper.questions.all()
        for ques in Question_DB.objects.filter(professor=prof):
            if ques not in curr_paper_questions:
                left_ques.append(ques)

        return render(request, 'prof/question_paper/addquestopaper.html', {
            'qpaper': ques_paper, 'question_list': left_ques, 'prof': prof
        })

    return render(request, 'prof/question_paper/addquestopaper.html')



def view_paper(request):
    prof = request.user

    if request.method == 'POST':
        papertitle = request.POST['title']
        ques_paper = Question_Paper.objects.get(professor=prof, qPaperTitle=papertitle)

        return render(request, 'prof/question_paper/viewpaper.html', {
            'qpaper': ques_paper, 'question_list': ques_paper.questions.all(), 'prof': prof
        })



def edit_paper(request):
    prof = request.user

    if request.method == 'POST' and request.POST.get('title', False):
        papertitle = request.POST['title']
        ques_paper = Question_Paper.objects.filter(professor=prof, qPaperTitle=papertitle).first()

        left_ques = []
        curr_paper_questions = ques_paper.questions.all()
        for ques in Question_DB.objects.filter(professor=prof):
            if ques not in curr_paper_questions:
                left_ques.append(ques)

        return render(request, 'prof/question_paper/editpaper.html', {
            'ques_left': left_ques, 'qpaper': ques_paper, 'question_list': ques_paper.questions.all(), 'prof': prof
        })

    elif request.method == 'POST' and request.POST.get('remove', False):
        papertitle = request.POST['paper']
        no = request.POST['question']
        ques_paper = Question_Paper.objects.filter(professor=prof, qPaperTitle=papertitle).first()
        ques = Question_DB.objects.filter(professor=prof, qno=no).first()
        ques_paper.questions.remove(ques)
        ques_paper.save()

        left_ques = []
        curr_paper_questions = ques_paper.questions.all()
        for ques in Question_DB.objects.filter(professor=prof):
            if ques not in curr_paper_questions:
                left_ques.append(ques)

        return render(request, 'prof/question_paper/editpaper.html', {
            'ques_left': left_ques, 'qpaper': ques_paper, 'question_list': ques_paper.questions.all(), 'prof': prof
        })

    elif request.method == 'POST' and request.POST.get('qnumber', False) != False:
        qno = request.POST['qnumber']
        ptitle = request.POST['titlepaper']
        ques_paper = Question_Paper.objects.filter(
            professor=prof, qPaperTitle=ptitle).first()
        a = Question_DB.objects.filter(professor=prof, qno=qno).first()
        ques_paper.questions.add(a)
        ques_paper.save()

        left_ques = []
        curr_paper_questions = ques_paper.questions.all()
        for ques in Question_DB.objects.filter(professor=prof):
            if ques not in curr_paper_questions:
                left_ques.append(ques)

        return render(request, 'prof/question_paper/editpaper.html', {
            'ques_left': left_ques, 'qpaper': ques_paper, 'question_list': ques_paper.questions.all(), 'prof': prof
        })
            


def view_specific_paper(request, paper_id):
    prof = request.user

    paper = Question_Paper.objects.get(professor=prof, pk=paper_id)
    return render(request, 'prof/question_paper/viewpaper.html', {
        'qpaper': paper, 'question_list': paper.questions.all(), 'prof': prof
    })
