from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, PasswordChangeForm
)
# from .forms import UserUpdateForm
from .forms import ProfileForm, UserForm, ChangePhoneForm
from users.models import Profile
from django.contrib.auth import update_session_auth_hash
# from . import helper as help_ 
# Create your views here.
# Rolling Your Own User Views

# These Views Only Render A Template
# class index
class Index(View):

    def get(self,request):
        if "next" in request.GET:
            request.session["next"] = request.GET["next"]
        return render(request, "users/index.html")

    def post(self, request):
        return HttpResponseNotAllowed(['GET'])




class Welcome(LoginRequiredMixin, View):

    def get(self,request):
        return render(request, "users/welcome.html")
    def post(self,request):
        return HttpResponseNotAllowed(['GET'])


# class logout 
class UserLogout(LoginRequiredMixin, View):

    def get(self,request):
        logout(request)
        # request.session['dict_profile'] = None
        return redirect(settings.LOGIN_URL)
        
    def post(self,request):
        return HttpResponseNotAllowed(['GET'])



# The Following Views All Have An Associated Form
class CreateUser(View):
    template_name = "users/registration.html"
    form_class = ProfileForm
    success_url = "users:login"
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        print(self.context)
        return self.render_to_response(request)

    def post(self, request):
        form = self.form_class(data=request.POST)
        data=request.POST
        if form.is_valid(): 
            user = User.objects.create_user(
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                )
            profile = Profile.objects.create(user=user,
                phone_number=data.get('phone_number')
                )
        
            return redirect(self.success_url)
        else:
            self.context = self.get_context(form)
            return self.render_to_response(request)

    def get_context(self, form):
        return {
            "form": form,
            "action": "users:create",
            "method": "POST",
            "submit_text": "Register"
        }

    def render_to_response(self, request):
        return render(request, self.template_name, self.context)

class LoginUser(View):
    template_name = "users/landing_page.html"
    form_class = AuthenticationForm
    success_url = "portfolio:dashboard"
    context = None

    def get(self, request):
        form = self.form_class()
        self.context = self.get_context(form)
        return self.render_to_response(request)

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        data=request.POST
        if True:
        # if form.is_valid():
            
            # user = form.get_user()
            
            user = User.objects.filter(username=data.get('username'))
            
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user and user.is_authenticated() and user.is_active:
                login(request, user)
            else:
                self.context = self.get_context(form)
                return self.render_to_response(request)
           
            profile = Profile.objects.filter(user=user)
            if "next" in request.session:
                self.success_url = request.session["next"]
                del request.session["next"]
            request.session.set_expiry(10000000)
            # dict_profile = {'username': data.get('username'),
            #     'first_name':data.get('first_name'),
            #     'last_name' : data.get('last_name'),
            #     'email' : data.get('email'),
            #     'phone_number' : data.get('phone_number')
            #     }
            # request.session['dict_profile'] = dict_profile
            return redirect(self.success_url)
        else:
            self.context = self.get_context(form)
            return self.render_to_response(request)

    def get_context(self, form):
        return {
            "form": form,
            "action": "users:login",
            "method": "POST",
            "submit_text": "Login" 
        }

    def render_to_response(self, request):
        return render(request, self.template_name, self.context)

class UpdateUser(LoginRequiredMixin, View):
    template_name = "dashboard.html"
    form_class = UserForm
    success_url = "portfolio:dashboard"
    context = None

    def get(self, request):
        form = self.form_class(instance=request.user)
        self.context = self.get_context(form)
        return self.render_to_response(request)

    def post(self, request):
        form = self.form_class(
            data=request.POST, instance=request.user
        )
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            self.context = self.get_context(form)
            return self.render_to_response(request)

    def get_context(self, form):
        return {
            "user_form": form,
            "action": "users:update",
            "method": "POST",
            "submit_text": "Update" 
        }
        
    def render_to_response(self, request):
        return render(request, self.template_name, self.context)

class ChangePassword(LoginRequiredMixin, View):
    template_name = "dashboard.html"
    form_class = PasswordChangeForm
    success_url = "portfolio:dashboard"
    context = None

    def get(self, request):
        print('***************inside the get')
        form = self.form_class(user=request.user)
        self.context = self.get_context(form)
        return self.render_to_response(request)

    def post(self, request):
        print('***************inside the post')
        form = self.form_class(
            user=request.user, data=request.POST
        )
        print(request.user)
        print(request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(self.success_url)
        else:
            print('form is not is_valid')
            self.context = self.get_context(form)
            return self.render_to_response(request)

    def get_context(self, form):
        return {
            "user_form": form,
            "action": "users:passwordChange",
            "method": "POST",
            "submit_text": "Update" 
        }
        
    def render_to_response(self, request):
        return render(request, self.template_name, self.context)

class ChangePhone(LoginRequiredMixin, View):
    template_name = "dashboard.html"
    form_class = ChangePhoneForm
    success_url = "portfolio:dashboard"
    context = None

    def get(self, request):
        print('***************inside the get to change number')
        profile = Profile.objects.get(user=request.user)
        request.profile = profile
        form = self.form_class(instance=profile)
        self.context = self.get_context(form)
        return self.render_to_response(request)

    def post(self, request):
        print('***************inside the post to change number')
        # form = self.form_class(
        #     user=request.user, data=request.POST
        # )
        profile = Profile.objects.get(user=request.user)
        form = self.form_class(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            print('form is not valid')
            self.context = self.get_context(form)
            return self.render_to_response(request)

    def get_context(self, form):
        return {
            "user_form": form,
            "action": "users:ChangePhone",
            "method": "POST",
            "submit_text": "change" 
        }
        
    def render_to_response(self, request):
        return render(request, self.template_name, self.context)


