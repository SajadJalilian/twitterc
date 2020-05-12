from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from .models import Status


def home(request):
    context = {"status: Status.objects.all()"}
    return render(request, "mytwitter/home.html", context)


def about(request):
    return render(request, "mytwitter/about.html", {"title": "About"})


class StatusListView(ListView):
    model = Status
    template_name = "mytwitter/home.html"
    context_object_name = "statuses"
    paginate_by = 5


class StatusDeleteView(DeleteView):
    model = Status
    success_url = "/"

    def test_func(self):
        status = self.get_object()
        if self.request.user == status.author:
            return True
        return False


class StatusDetailView(DetailView):
    model = Status


class UserStatusListView(ListView):
    model = Status
    template_name = "mytwitter/user_status.html"
    context_object_name = "statuses"
    paginate_by = 5
