from django.shortcuts import render
from users.models import waitlist
from django.http import HttpResponse
from users.models import waitlist

def home(request):
    return render(request, "home.html")


def waitlist_v(request):
    try:
        if request.user.waitlist:
            return HttpResponse("You have already submitted the waitlist")
    except:
        return render(request, "waitlist.html")

def waitlist_submit(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll_number = request.POST.get('roll_number')
        image = request.FILES.get('id_card')
        university = request.POST.get('university')
        waitlist_obj = waitlist.objects.create(user=user, name=name, email=email, enrollment_number=roll_number, id_card=image, university=university)
        waitlist_obj.save()
        return HttpResponse("Waitlist submitted successfully")