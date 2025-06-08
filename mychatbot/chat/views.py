from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .langchain_bot import ask_bot
# chat/views.py

from django.shortcuts import render

def index(request):
    return render(request, "chat/index.html")


@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")
        if user_message:
            bot_response = ask_bot(user_message)
            return JsonResponse({"response": bot_response})
    return JsonResponse({"response": "Error: No message received"}, status=400)
