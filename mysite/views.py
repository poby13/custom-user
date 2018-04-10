from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {'username': UsernameField}


# class HomeView(TemplateView):
#     template_name = 'home.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_manager:
            return redirect('bookshop:manager_welcome')
        elif request.user.is_member:
            return redirect('bookshop:member_welcome')
        else:
            return render(request, 'about.html')
    return render(request, 'home.html')


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = MyUserCreationForm
    # 타이밍 로딩 문제로 reverse를 사용시 에러가 발생
    success_url = reverse_lazy('register_done')


class UserRegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'
