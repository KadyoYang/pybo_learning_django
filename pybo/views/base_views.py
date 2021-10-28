from django.core import paginator
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question, Answer, Comment
from django.utils import timezone
from ..forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.http import HttpResponse
# Create your views here.



def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') #페이지 넘버

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개
    page_obj = paginator.get_page(page)


    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
