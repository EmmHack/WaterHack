from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
class Home(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Login(View):
    template_name = 'app/login.html'

    def get(self, request, *args, **kwargs):

        errors = ""
        next = ""
        if self.request.method == 'GET':
            return render(self.request, self.template_name)

        elif request.method == 'POST':

            try:
                username = self.request.POST.get('username')
                password = self.request.POST.get('password')
                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    auth.login(self.request, user)
                    request.session['username'] = self.request.POST.get('username')
                    return HttpResponseRedirect('/app/')
                else:
                    errors = "Invalid username or password"

            except User.DoesNotExist:
                errors = "Invalid username or password"
                print "none"
            return render(self.request, self.template_name, {'errors': errors})


class SignUp(View):
    template_name = 'app/signup.html'

    def get(self, request, *args, **kwargs):

        if self.request.method == 'GET':
            return render(self.request, self.template_name)
        elif self.request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                errors = "Username already Taken"
                return render(self.request, self.template_name, {"errors": errors})

            elif User.objects.filter(username=username).exists():
                errors = "Email already Registered"
                return render(self.request, self.template_name, {"errors": errors})
            else:
                client = User.objects.create_user(username=username, password=password)
                client.save()
                return render(self.request, self.template_name)
