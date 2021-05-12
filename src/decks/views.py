from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from cards.models import Card
from .models import Deck
from cards.views import CardSerializer

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'

class DecksViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()

class DeckCardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all().prefetch_related('deck')

    def list(self, request, deck_pk):
        cards = Card.objects.filter(deck=deck_pk)
        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
