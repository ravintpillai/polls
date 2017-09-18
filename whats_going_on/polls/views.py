from django.http import HttpResponse

from .models import Question, Choice, Activity


def index(request):
    return HttpResponse(str(Question.objects.all()[0]))