import json
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, View, ListView, RedirectView, UpdateView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class UserListView(ListView):
    dummy_data = [
        {
            "fullname": "Emma Smith",
            "role": "administrator",
            "email": "emma@gmail.com",
            "login": "yesterday",
            "date": "25 Oct 2023, 5:20 pm",
            "two_step": "Enabled",
        },
        {
            "fullname": "Max Smith",
            "role": "developer",
            "email": "maxsmith@gmail.com",
            "login": "yesterday",
            "date": "25 Oct 2023, 5:20 pm",
            "two_step": "Enabled",
        },
        {
            "fullname": "Melody Macy",
            "role": "Analyst",
            "email": "melody@gmail.com",
            "login": "yesterday",
            "date": "25 Oct 2023, 5:20 pm",
            "two_step": "Enabled",
        },
    ]
    context_object_name = 'user_list'
    template_name = "pages/User/users.html"
    queryset = dummy_data


user_list_view = UserListView.as_view()


class UserSignUpView(View):
    success_url = reverse_lazy("login")

    def post(self, request,  *args, **kwargs):
        pass1 = request.POST["password"]
        pass2 = request.POST["confirm_password"]
        if pass1 != pass2:
            messages.error(request, "password dont match")
            return redirect("/accounts/login")

        email = request.POST["email"]
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        try:
            user = User.objects.get(username=username)
            messages.info(request, "user exits")
        except User.DoesNotExit:
            # Create user and save to the database
            user = User.objects.create_user(username=username, email=email, password=pass1)
            # Update fields and then save again
            user.first_name = first_name
            user.last_name = last_name
            user.name = f"{first_name}  {last_name}" 
            user.save()
            return redirect("users:login")


user_sign_view = UserSignUpView.as_view()


class UserLoginView(View):

    def post(self, request,  *args, **kwargs):
        pass1 = request.POST["password"]
        email = request.POST["email"]
        user = auth.authenticate(email=email, password=pass1) | auth.authenicate(username=email, password=pass1)
        if user is not None:
            # auth.login(request.user)
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "wrong login credentials")
            return redirect("/accounts/login")


user_login_view = UserLoginView.as_view()


class UserLogoutView(View):
    def post(self, request,  *args, **kwargs):
        auth.logout(request)
        redirect("users:login")


user_logout_view = UserLogoutView.as_view()
