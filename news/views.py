from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from news.forms import *
from django.template.loader import render_to_string


# Create your views here.

class HomeNewsView(ListView):
    model = news
    template_name = 'news/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_list = news.objects.order_by('?')[:4]
        context['news_0'] = news_list[0] if len(news_list) > 0 else None
        context['news_1'] = news_list[1] if len(news_list) > 1 else None
        context['news_2'] = news_list[2] if len(news_list) > 2 else None
        context['news_3'] = news_list[3] if len(news_list) > 3 else None
        return context


class DashboardView(LoginRequiredMixin,ListView):
    model = news
    template_name = 'news/dashboard.html'
    login_url = 'news-login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mynews = news.objects.filter(author=self.request.user)
        context['news'] = mynews
        return context


class UserLoginView(LoginView):
    template_name = 'news/login.html'
    authentication_form = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('news-dashboard')

class UserRegisterView(CreateView):
    form_class = UserRegisterform
    template_name = 'news/register.html'
    success_url = reverse_lazy('news-login')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home-page')

class NewsAddView(LoginRequiredMixin, CreateView):
    model = news
    form_class = NewsForm
    template_name = 'news/addnews.html'
    success_url = reverse_lazy('news-dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TagsAddView(LoginRequiredMixin, CreateView):
    model = tags
    form_class = TagForm
    template_name = 'news/tags_form.html'
    success_url = reverse_lazy('news-add')

    def form_valid(self, form):
        response = super().form_valid(form)
        tags = self.object
        if 'HX-request' in self.request.headers:
            render_question = render_to_string('news/addtags_success.html', {'tags': tags})
            return HttpResponse(render_question)

        return response

class NewsDeleteView(DeleteView):
    model = news
    template_name = 'news/news_confirm_delete.html'
    success_url = reverse_lazy('news-dashboard')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if 'HX-request' in self.request.headers:
            return JsonResponse({'success': True})
        return response

class NewsByIDView(DetailView):
    model = news
    template_name = 'news/content.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_list = news.objects.order_by('?')[:3]
        context['news1'] = news_list[0] if len(news_list) > 0 else None
        context['news2'] = news_list[1] if len(news_list) > 0 else None
        context['news3'] = news_list[2] if len(news_list) > 0 else None

        comment = comments.objects.filter(news=self.object)
        context['comment_list'] = comment
        return context

class CommentAddViews(LoginRequiredMixin, CreateView):
    model = comments
    form_class = CommentForm
    template_name = 'news/add_comment.html'
    success_url = reverse_lazy('news-dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        newz = news.objects.get(id=self.kwargs['pk'])
        form.instance.news = newz
        response = super().form_valid(form)
        comment = self.object
        if 'HX-request' in self.request.headers:
            render_question = render_to_string('news/addcomment_success.html', {'comment': comment})
            return HttpResponse(render_question)

        return response

class NewsEditView(UpdateView):
    model = news
    form_class = NewsForm
    template_name = 'news/edit_news.html'

    def get_success_url(self):
        return reverse_lazy('news-dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
