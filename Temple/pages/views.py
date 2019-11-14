from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView

from .models import Choice, Questions

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Questions
    #template_name = 'pages/detail.html'
    context_object_name = 'question'


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'pages/results.html'



class HomePageView(TemplateView):
    template_name = 'home.html'


def detail(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'pages/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'pages/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'pages/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pages:results', args=(question.id,)))


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'pages/index.html', context)