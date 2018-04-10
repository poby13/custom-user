from django.views.generic.base import TemplateView


class ManagerHomeTV(TemplateView):
    template_name = "manager/welcome.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class MemberHomeTV(TemplateView):
    template_name = "member/welcome.html"
