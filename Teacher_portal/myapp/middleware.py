from django.shortcuts import redirect
from .models import SessionToken

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed = ["/login/"]
        if request.path not in allowed:
            token = request.COOKIES.get("session_token")
            if not token or not SessionToken.objects.filter(token=token).exists():
                return redirect("/login/")
        return self.get_response(request)





