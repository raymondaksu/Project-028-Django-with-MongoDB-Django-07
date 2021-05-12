from rest_framework import serializers, viewsets, filters
from .models import Card
from django_filters import rest_framework as filter


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class CardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    filter_backends = (filter.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('question_type',)
    search_fields = ('question',)
    ordering = ('question_type',)
