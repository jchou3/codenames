from django.shortcuts import render
from django.template import loader


# Create your views here.
def board(request):
    
    return render(request, "board/board.html")