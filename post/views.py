import logging
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .forms import InquiryForm

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class DetailView(generic.DetailView):
    template_name = "detail.html"

class InquiryView(generic.FormView):
    template_name = 'inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('post:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info(f'お問い合わせをした方のお名前：{form.cleaned_data["name"]}')
        return super().form_valid(form)