from django.shortcuts import render

def display_persona(request):
    return render(request, 'persona.html')