from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import News, Comment
from .newform import NewForm
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactForm
from django.views.generic import TemplateView


class NewsListView(ListView):
    model = News
    template_name = 'news-list.html'
    context_object_name = 'news'
    ordering = ['title']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset


class NewsCreateView(CreateView):
    model = News
    fields = ['title', 'description', 'year', 'image']
    template_name = 'news-create.html'
    class_form = NewForm
    success_url = reverse_lazy('news:list')


class NewsUpdateView(UpdateView):
    model = News
    fields = ['title', 'description', 'year', 'image']
    template_name = 'news-update.html'
    class_form = NewForm
    success_url = reverse_lazy('news:list')


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news-delete.html'
    success_url = reverse_lazy('news:list')


class NewsDetailView(DetailView):
    model = News
    template_name = 'news-detail.html'

    def post(self, request, *args, **kwargs):
        news = self.get_object()
        comment_text = request.POST.get('comment')
        if comment_text:
            Comment.objects.create(user=request.user, post=news, text=comment_text)
            return redirect('news:new-detail', pk=news.pk)
        return render(request, self.template_name, {'news': news})


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('news:thank_you')

    def form_valid(self, form):
        from django.core.mail import send_mail
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        send_mail(
            'Sizga taklifim bor !',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            'sotvoldiyevazamat193@gmail.com.com',
            ['sotvoldiyevazamat193@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'thank_you.html'