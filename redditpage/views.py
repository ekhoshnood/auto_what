from django.shortcuts import render


def reddit(request):
    return render(request, "reddit/home.html")