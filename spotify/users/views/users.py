"""Uses views."""

# Django
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin

# Forms
from spotify.users.forms import SignupForm

# Models
from spotify.users.models import User


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""
    slug_field = 'username'
    slug_url_kwarg = 'username'

    template_name = 'users/update.html'
    model = User
    fields = ['first_name', 'last_name']

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object
        return reverse('users:update', kwargs={'username': username})
