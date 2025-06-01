from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from collections import OrderedDict
from django.utils import timezone
import statbotics
sb = statbotics.Statbotics()

# Create your views here.
def event(request, event_key):
    event_data = sb.get_event(event_key)
    matches = sb.get_matches(event=event_key)
    if matches:
        print(matches[0])
    return render(request, "events/event.html", {
        "event": event_data,
        "matches": matches,
    })

@login_required
def events(request, year=timezone.now().year):
    event_data = sb.get_events(year)
    events = {}
    for event in event_data:
        week = event.get("week", "Unscheduled")
        if week not in events:
            events[week] = []
        events[week].append(event)
    # Filter events dictionary directly and sort weeks
    events = OrderedDict(
        (key, events[key])
        for key in sorted(events.keys(), key=lambda w: w if isinstance(w, int) else 99)
    )
    return render(request, "events/events.html", {
        "events": events,
    })