from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Favorite
from .serializers import favoriteSerializer


def index(request):
    return HttpResponse("Olá mundo! Este é o app de Tecnologias Web do Insper.")

@api_view(['POST'])
def api_favorite(request):

    if request.method == 'POST':
        
        favorite=Favorite()
        new_favorite_data = request.data
        favorite.title = new_favorite_data['title']
        favorite.save()

    serialized_favorite = favoriteSerializer(favorite)
    return Response(serialized_favorite.data)
    
@api_view(['GET'])
def api_favoriteList(request):
    favorite = Favorite.objects.all()
    serialized_note = favoriteSerializer(favorite, many=True)
    return Response(serialized_note.data)