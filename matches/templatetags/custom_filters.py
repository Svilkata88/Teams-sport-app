from django import template
from matches.models import Matches

register = template.Library()


@register.filter
def status(match: Matches):
    """Makes status indicator different color depending of status value."""
    if match.status == "scheduled":
        return "#6b21a8"
    elif match.status == "playing":
        return "green"
    elif match.status == "finished":
        return "red"
    elif match.status == 'postponed':
        return "orange"
