from typing import Any

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Card


class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs: dict[str, Any]):
        context = super().get_context_data(**kwargs)
        context["card_names"] = [(c.name, c.uuid) for c in Card.objects.all()]
        return context


class GetCardView(APIView):
    def get(self, request: Request) -> Response:
        uuid = request.GET.get("uuid")
        if not uuid:
            return Response(
                {"error": "UUID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            card = get_object_or_404(Card, uuid=uuid)
            print("my get card worked", card.name)
            text = card.text.split("\n") if card.text else []
            rulings = card.rulings.split("\n\n") if card.rulings else []
            return Response(
                {
                    "uuid": card.uuid,
                    "name": card.name,
                    "text": text,
                    "rulings": rulings,
                }
            )
        except Exception as e:
            print("my get card error")
            print("my error", e)
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
