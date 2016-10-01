from django.shortcuts import render
from django.views import View


# Create your views here.
class Home(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Login(View):
    template_name = 'app/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SignUp(View):
    template_name = 'app/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
