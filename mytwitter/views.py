from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView


def home(request):
    context = {"status: Status.objects.all()"}
    return render(request, "mytwitter/home.html", context)


def about(request):
    return render(request, "mytwitter/about.html", {"title": "About"})


class StatusListView(ListView):
    pass


class StatusDeleteView(DeleteView):
    pass


class StatusDetailView(DetailView):
    pass


class UserStatusListView(ListView):
    pass
