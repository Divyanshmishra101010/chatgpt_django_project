import openai
import os
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from chatgpt_project.settings import OPENAI_API_KEY

# Initialize OpenAI Client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

@csrf_exempt
def chat_with_gpt(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()

            if not user_message:
                return JsonResponse({'error': 'No message provided'}, status=400)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}]
            )

            chat_response = response.choices[0].message.content
            return JsonResponse({'response': chat_response})

        except openai.OpenAIError as e:
            return JsonResponse({'error': f'OpenAI API Error: {str(e)}'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON input'}, status=400)

        except Exception as e:
            return JsonResponse({'error': f'Server Error: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def chat_page(request):
    return render(request, 'chat.html')
