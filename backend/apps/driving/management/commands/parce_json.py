import json

from django.core.management.base import BaseCommand

from apps.driving.models import Ticket, Chapter

with open('fixtures/ticket.json', 'r') as f:
    ticket_obj = json.load(f)
with open('fixtures/chapter.json', 'r') as d:
    chapter_obj = json.load(d)


class Command(BaseCommand):

    def handle(self, *args, **options):

        for chapter in chapter_obj:

            Chapter.objects.create(id=chapter['id'], text=chapter['name'])

        for ticket in ticket_obj:
            Ticket.objects.create(
                id=ticket['ticket_id'],
                chapter_id=ticket['chapter_id'],
                question=ticket['question'],
                answer=ticket['answers'],
                explanation=ticket['explanations'])
