from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from models import register_form

def login(request, in_or_out):
    out = True if "out" in in_or_out else False
    ignore = (request.POST.get('todo') == 'redirect')
    if ignore:
        out = False
    reg = request.GET.get('reg', False)
    next = request.GET.get(u'next', '/app/home/')
    valid = True
    if request.POST and not out and not ignore:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(next)
        else:
            valid = False
    if "out" in in_or_out and not ignore:
            auth.logout(request)
            request.session['username'] = request.POST.get('username')
    return render(request,'app/login.html', {'in_or_out': out, 'reg': reg, 'valid': valid, 'next': next})
    #return render(request,'app/login.html')

# Create your views here.
class Home(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def register(request):
    """

    :param request:
    :return:
    """
    duplicate = False
    if request.POST:
        username = request.POST.get('username')
        if User.objects.filter(username=username):
            duplicate = True
        else:
            user = User.objects.create_user(username=username, password=request.POST.get('password'))
            user.username = request.POST.get('username')
            user.password = request.POST.get('password'),
            user.save()
            return HttpResponseRedirect("/app/login/?reg=1")
    form = register_form()
    return render(request,'app/signup.html', {'form': form, 'duplicate': duplicate})
