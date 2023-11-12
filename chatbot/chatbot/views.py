# myapp/views.py

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from nltk.chat.util import Chat, reflections

patterns = [
    # Your chat patterns here
]

chatbot = Chat(patterns, reflections)

@csrf_exempt
@require_POST
def chat(request):
    user_input = request.POST.get('user_input', '')
    response = chatbot.respond(user_input)
    return JsonResponse({'response': response})

def index(request):
    return render(request, 'index.html')
