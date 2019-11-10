from django.shortcuts import render


def iframe(request):
    return render(request, "iframe/iframe_test.html")
