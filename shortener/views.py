from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import secrets
from .models import ShortURL

# Create your views here.

def _generate_random_string(length=6):
    RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(secrets.choice(RANDOM_STRING_CHARS) for _ in range(length))

@login_required(login_url = "/login")
def dashboard_view(request):
    user_ = request.user
    urls = ShortURL.objects.filter(user = user_)
    return render(request, "dashboard.html", { "urls" : urls})

@login_required(login_url = "/login")
def generate_view(request):
    if request.method == "POST":
        # generate
        original_long_url = request.POST["original"]
        custom_short_text = request.POST["short"]
        user_ = request.user

        if original_long_url and custom_short_text:
            # generate based on user input
            check = ShortURL.objects.filter(short_query = custom_short_text)
            if not check:
                new_url = ShortURL(
                    user = user_,
                    original_url = original_long_url,
                    short_query = custom_short_text,
                )
                new_url.save()
            else:
                messages.error(request, "Custom URL already exists!")
            return redirect(dashboard_view)
        elif original_long_url:
            # generate randomly
            generated = False
            while not generated:
                random_short_text = _generate_random_string()
                check = ShortURL.objects.filter(short_query = random_short_text)
                if not check:
                    new_url = ShortURL(
                        user = user_,
                        original_url = original_long_url,
                        short_query = random_short_text,
                    )
                    new_url.save()
                    generated = True
            return redirect(dashboard_view)
        else:
            messages.error(request, "Empty Fields!")
            return redirect(dashboard_view)

    else:
        return redirect(dashboard_view)

def home_view(request, query=None):
    if not query or query is None:
        return render(request, 'home.html')
    else:
        try:
            shorturl_object = ShortURL.objects.get(short_query=query)
            shorturl_object.visits_count = shorturl_object.visits_count + 1
            shorturl_object.save()
            return redirect(shorturl_object.original_url)
        except ShortURL.DoesNotExist:
            return render(request, 'home.html', {'error': "Error!"})

@login_required(login_url='/login/')
def delete_view(request):
    if request.method == "POST":
        short = request.POST['delete']
        try:
            check = ShortURL.objects.filter(short_query=short)
            check.delete()
            return redirect(dashboard_view)
        except ShortURL.DoesNotExist:
            return redirect(home_view)
    else:
        return redirect(home_view)
