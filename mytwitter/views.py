from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView,
    UpdateView,
)
from .models import Status


def home(request):
    context = {"status: Status.objects.all()"}
    return render(request, "mytwitter/home.html", context)


class StatusListView(ListView):
    model = Status
    template_name = "mytwitter/home.html"
    context_object_name = "statuses"
    paginate_by = 10


class UserStatusListView(ListView):
    model = Status
    template_name = "mytwitter/user_status.html"
    context_object_name = "user_statuses"
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Status.objects.filter(author=user).order_by("-date_posted")


class StatusDetailView(DetailView):
    model = Status


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ["message"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Status
    fields = ["message"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        status = self.get_object()
        if self.request.user == status.author:
            return True
        return False


class StatusDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Status
    success_url = "/"

    def test_func(self):
        status = self.get_object()
        if self.request.user == status.author:
            return True
        return False


def about(request):
    return render(request, "mytwitter/about.html", {"title": "About"})
