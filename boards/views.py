from django.http import JsonResponse
from boards.models import Board

# Create your views here.
def home(request):
    boards = Board.objects.all().values("name","description")
    board_names = list(boards)
    return JsonResponse(board_names,safe=False)
