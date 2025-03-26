import json
import os

import django
from django.db import transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "the_gatherer.settings")
django.setup()

if True:
    from core.models import Card


def main() -> None:
    with open("data/AllIdentifiers.json", "r") as f:
        content = json.loads(f.read())
        with transaction.atomic():
            cards: dict[str, Card] = {}
            for uuid in content["data"]:
                card = content["data"][uuid]

                if card["name"] in cards:
                    continue

                if not card.get("originalText"):
                    continue

                rulings: list[str] = []
                for rule in card.get("rulings", []):
                    rulings.append(rule["text"])
                rulings_text = "\n\n".join(rulings)

                card_obj = Card(
                    uuid=uuid,
                    name=card["name"],
                    text=card.get("text"),
                    rulings=rulings_text or None,
                )

                cards[card["name"]] = card_obj

            added = 0
            for card in cards.values():
                card.save()
                added += 1

            print(f"Added {added} cards")


if __name__ == "__main__":
    delete = input("Delete?: ")
    if delete:
        Card.objects.all().delete()
        print("Deleted all cards")

    main()
