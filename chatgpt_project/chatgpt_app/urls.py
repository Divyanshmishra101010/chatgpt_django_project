from django.urls import path
from .views import chat_with_gpt, chat_page

urlpatterns = [
    path('chat/', chat_page, name='chat_page'),
    path('api/chat/', chat_with_gpt, name='chat_with_gpt'),
]
