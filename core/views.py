from django.shortcuts import render

def index(request):
    if request.method == "POST":
        password = request.POST.get("password")
        email = request.POST.get("email")
        print(email)
        print(password)
    return render(request,'index.html')