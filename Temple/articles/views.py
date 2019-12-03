from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # new
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from articles.form import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup.html', args)

    else:
        form = RegistrationForm()

        args = {'form' : form}

class WelcomeListView(View):
    model = models.Article
    template_name = 'welcome.html'

    def get(self, request):
       return render(request,'welcome.html')

    def post(self,request):
      return render(request, 'welcome.html')


class ArticleListView(LoginRequiredMixin,ListView):
    model = models.Article
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Article
    fields = ['name', 'god', 'amount',  ]
    template_name = 'article_edit.html'
    login_url = 'login'

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = models.Article
    template_name = 'article_new.html'
    fields = ['name', 'amount', 'god',]
    login_url = 'login' #new

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PoojaListView(View):
    model = models.Article
    template_name = 'pooja.html'

    def get(self, request):
       return render(request,'pooja.html')

    def post(self,request):
      return render(request, 'pooja.html')

class PoojaTimingListView(View):
    model = models.Article
    template_name = 'poojaTiming.html'

    def get(self, request):
       return render(request,'poojaTiming.html')

    def post(self,request):
      return render(request, 'poojaTiming.html')

class PoojaDetailListView(View):
    model = models.Article
    template_name = 'poojaDetail.html'

    def get(self, request):
       return render(request,'poojaDetail.html')

    def post(self,request):
      return render(request, 'poojaDetail.html')

class ContactListView(View):
    model = models.Article
    template_name = 'contact.html'

    def get(self,request):
        return render(request, 'contact.html')

    def post(self,request):
        return render(request, 'contact.html')

class AdministrationListView(View):
    model = models.Article
    template_name = 'administration.html'

    def get(self,request):
        return render(request, 'administration.html')

    def post(self,request):
        return render(request, 'administration.html')

class AddPoojaListView(View):
    model = models.Article
    template_name = 'addPooja.html'

    def get (self,request):
        return render(request, 'addPooja.html')

    def post(self,request):
        return render(request, 'addPooja.html')

class PrintListView(View):
    model = models.Print
    template_name = 'poojaPrint.html'

    def get (self,request):
        return render(request, 'poojaPrint.html')

    def post(self,request):
        return render(request, 'poojaPrint.html')



