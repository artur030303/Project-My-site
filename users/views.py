from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, TemplateView
from orders.models import Order, OrderItem

from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import ProfileForm, UserLoginForm, UserRegistrationForm


# Create your views here.


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("main:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Авторизация"
        return context

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user:
            login(self.request, user)
            messages.success(
                self.request, f"Полльзователь {username}, Вы вошли в аккаунт"
            )

            next_url = self.request.POST.get("next", None)
            if next_url:
                return HttpResponseRedirect(next_url)

            return HttpResponseRedirect(self.get_success_url())
        else:
            form.add_error(None, "Неверное имя пользователя или пароль")
            return self.form_invalid(form)


class UserRegistrationView(CreateView):
    template_name = "users/registration.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("user:profile")

    def form_valid(self, form):
        user = form.save()
        self.object = user
        login(self.request, user)
        messages.success(
            self.request, f"Пользователь {user.username}, Вы успешно зарегистрировались"
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Регистрация"
        return context


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("user:profile")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Профайл обновлен")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Профайл не обновлен")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Личный кабинет"
        context["orders"] = (
            Order.objects.filter(user=self.request.user)
            .prefetch_related(
                Prefetch(
                    "orderitem_set",
                    queryset=OrderItem.objects.select_related("product"),
                )
            )
            .order_by("-id")
        )

        return context


class UserBasketView(TemplateView):
    template_name = "users/users_basket.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home - Корзина"
        return context


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("main:index")

    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            messages.success(
                request, f"Пользователь {request.user.username}, Вы вышли из аккаунта"
            )
            logout(request)
            return redirect(reverse_lazy("main:index"))
        return super().dispatch(request, *args, **kwargs)
