
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy  # это функция из Django, которая используется для отложенного (ленивого) определения URL-адреса

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, TemplateView
from orders.models import Order, OrderItem

from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import ProfileForm, UserLoginForm, UserRegistrationForm


# Create your views here.

# класс для авторизации
class UserLoginView(LoginView):
    template_name = "users/login.html" # шаблон авторизации
    form_class = UserLoginForm # форма авторизации 
    success_url = reverse_lazy("main:index") # перенаправление после успешной авторизации

    # метод получения контекста для шаблона 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # получаем базовый контекст от родительского класса LoginView 
        context["title"] = "Home - Авторизация" # заголовок страницы
        return context 
    
    # метод валидации формы
    def form_valid(self, form):
        username = self.request.POST["username"] # имя пользователя из формы 
        password = self.request.POST["password"] # пароль из формы 
        user = auth.authenticate(username=username, password=password) # проверяем если такой пользователь существует 

        if user: # если пользователь существует
            login(self.request, user) # выполняем авторизацию
            messages.success(self.request, f"Полльзователь {username}, Вы вошли в аккаунт") # и выводим сообщение об успешном входе

            next_url = self.request.POST.get("next", None) # извлекаем значение next из POST запроса
            if next_url: # если значение next существует
                return HttpResponseRedirect(next_url) # перенаправляем пользователя на указанную страницу

            return HttpResponseRedirect(self.get_success_url()) # перенаправляем пользователя на страницу успешного входа
        else: # если пользователь не существует
            form.add_error(None, "Неверное имя пользователя или пароль") # добавляем ошибку в форму 
            return self.form_invalid(form) # возвращаем невалидную форму 


# класс для регистрации
class UserRegistrationView(CreateView): # CreateView - класс для создания нового объекта
    template_name = "users/registration.html" # шаблон регистрации
    form_class = UserRegistrationForm # форма регистрации 
    success_url = reverse_lazy("user:profile") # перенаправление после успешной регистрации

    # метод валидации формы
    def form_valid(self, form):
        user = form.save() # сохраняем пользователя в базе данных
        self.object = user # записываем пользователя в объект класса 
        login(self.request, user) # выполняем авторизацию 
        messages.success(self.request, f"Пользователь {user.username}, Вы успешно зарегистрировались") # выводим сообщение об успешном регистрации
        return HttpResponseRedirect(self.get_success_url()) # перенаправляем пользователя на страницу успешного регистрации
    
    # метод получения контекста для шаблона
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # получаем базовый контекст от родительского класса CreateView
        context["title"] = "Home - Регистрация" # заголовок страницы
        return context


# класс для обновления профиля
# LoginRequiredMixin - класс для проверки авторизации
# UpdateView - класс для обновления объекта
class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = "users/profile.html" # шаблон профиля 
    form_class = ProfileForm # форма профиля 
    success_url = reverse_lazy("user:profile") # перенаправление после успешного обновления профиля
    
    # метод получения объекта
    def get_object(self, queryset=None):
        return self.request.user # возвращаем текущего пользователя
    
    # метод валидации формы
    def form_valid(self, form):
        messages.success(self.request, "Профайл обновлен")# выводим сообщение об успешном обновлении
        return super().form_valid(form) # возвращаем валидную форму
    
    # метод обработки невалидной формы
    def form_invalid(self, form):
        messages.error(self.request, "Профайл не обновлен") # выводим сообщение об ошибке
        return super().form_invalid(form) # возвращаем невалидную форму
    
    # метод получения контекста для шаблона
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # получаем базовый контекст от родительского класса UpdateView
        context["title"] = "Home - Личный кабинет" # заголовок страницы
        # получаем все заказы пользователя
        context["orders"] = (Order.objects.filter(user=self.request.user) # фильтруем заказы по пользователю
            # подгружаем связанные объекты в одном запросе. (prefetch_related-чтобы избежать проблемы "N+1 запросов")
            .prefetch_related(Prefetch( "orderitem_set",queryset=OrderItem.objects.select_related("product"),)) # подгружаем связанный объект OrderItem с моделью Products )
            .order_by("-id") # сортируем заказы по убыванию
        )
        return context


# класс для просмотра корзины
class UserBasketView(TemplateView):
    template_name = "users/users_basket.html" # шаблон корзины
    
    # метод получения контекста для шаблона
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # получаем базовый контекст от родительского класса TemplateView
        context["title"] = "Home - Корзина" # заголовок страницы
        return context 


# класс для выхода из аккаунта
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("main:index") # перенаправление после выхода из аккаунта на главную страницу
    
    # метод обработки запроса
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET": # если запрос GET 
            messages.success(request, f"Пользователь {request.user.username}, Вы вышли из аккаунта") # выводим сообщение об успешном выходе из аккаунта
            logout(request) # выходим из аккаунта
            return redirect(reverse_lazy("main:index")) # перенаправляем пользователя на главную страницу
        return super().dispatch(request, *args, **kwargs) # 
