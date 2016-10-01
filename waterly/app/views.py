import csv, json

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from api.models import Consumer, Address, Consumption
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

class Home(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class UploadFixture(View):

    def get(self, request, *args, **kwargs):

        with open('datafiles/consumers.csv', 'rb') as consumers:
            reader = csv.reader(consumers, delimiter=',', quotechar='|')
            next(reader, None) 
            for row in reader:
                name = row[0]
                meter_no = row[1]
                Consumer.objects.create(name=name, meter_no=meter_no)

        with open('datafiles/addresses.csv', 'rb') as addresses:
            reader = csv.reader(addresses, delimiter=',', quotechar='|')
            next(reader, None) 
            for row in reader:
                meter_no = row[0]
                building_name = row[1]
                street_no = row[2]
                street_name = row[3]
                suburb_name = row[4]
                municipality_name = row[5]
                province_name = row[6]

                consumer = Consumer.objects.filter(meter_no=meter_no)[0]
                Address.objects.create(consumer=consumer, 
                                       building_name=building_name,
                                       street_no=street_no,
                                       street_name=street_name,
                                       suburb_name=suburb_name,
                                       municipality_name=municipality_name,
                                       province_name=province_name)

        with open('datafiles/consumption.csv', 'rb') as consumption:
            reader = csv.reader(consumption, delimiter=',', quotechar='|')
            next(reader, None) 
            for row in reader:
                meter_no = row[0]
                reading = row[1]
                date = row[2].replace('/', '-')

                consumer = Consumer.objects.filter(meter_no=meter_no)[0]
                Consumption.objects.create(consumer=consumer, reading=reading,
                                           date=date)

        response =  {'result': 'data uploaded successfully'}
        return JsonResponse(response)


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
