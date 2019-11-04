from django.shortcuts import render

# Create your views here.
def personal_page(request):
    return render(request, "personal/personal_home_screen.html", {})
