from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, ListView
from django.urls import reverse_lazy
from .models import User
##################################################################################################
class Home(LoginRequiredMixin, ListView):
    model = User
    template_name = "home.html"
    def get_queryset(self, **kwargs):
        post = User.objects.filter(ds_grupo="GES")
        post = post.filter(ds_secretaria=self.request.user.ds_secretaria)
        return post
##################################################################################################
class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'account/lista.html'
    success_url = reverse_lazy('UserList')
##################################################################################################
class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'ds_secretaria', 'ds_grupo']
    template_name = 'account/update.html'
    success_url = reverse_lazy('UserList')
##################################################################################################
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    return render(request, 'account/cadastro.html', {'form': form})
##################################################################################################
@login_required
def altera_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Por favor, corrija o erro abaixo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/altera_senha.html', {
        'form': form
    })
##################################################################################################
class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'ds_secretaria']
    template_name = 'account/update.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.id == self.object.id:
            var = 'igual'
        else:
            var = 'diferente'
        context['var'] = var
        return context
