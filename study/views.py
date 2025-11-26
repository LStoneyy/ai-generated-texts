from django.shortcuts import render, redirect
from .forms import ParticipantForm, ResponseForm
from .models import TextItem, Participant, Response

# Startseite


def start(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            request.session["participant_id"] = participant.id

            # Randomisierte Textreihenfolge für diesen Teilnehmer speichern
            text_ids = list(TextItem.objects.all().values_list("id", flat=True))
            import random

            random.shuffle(text_ids)
            request.session["text_order"] = text_ids
            request.session["current_index"] = 0

            return redirect("study:classify", index=1)
    else:
        form = ParticipantForm()
    return render(request, "study/start.html", {"form": form})


# Klassifizierungsseite
def classify(request, index):
    participant_id = request.session.get("participant_id")
    text_order = request.session.get("text_order")
    current_index = request.session.get("current_index", 0)

    if participant_id is None or text_order is None:
        return redirect("study:start")

    if current_index >= len(text_order):
        return redirect("study:finish")

    text_id = text_order[current_index]
    text = TextItem.objects.get(id=text_id)
    form = ResponseForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        participant = Participant.objects.get(id=participant_id)
        Response.objects.create(
            participant=participant,
            text=text,
            classification=form.cleaned_data["classification"],
            confidence=int(form.cleaned_data["confidence"]),
            response_time=int(form.cleaned_data["response_time"]),
            index=current_index + 1,
        )
        # Index hochzählen
        request.session["current_index"] = current_index + 1

        if current_index + 1 >= len(text_order):
            return redirect("study:finish")
        else:
            # +2, weil index=1-basiert
            return redirect("study:classify", index=current_index + 2)

    context = {"form": form, "text": text, "index": index, "total": len(text_order)}
    return render(request, "study/classify.html", context)


# Abschlussseite
def finish(request):
    # Session löschen (optional)
    request.session.flush()
    return render(request, "study/finish.html")


def impressum(request):
    return render(request, "study/impressum.html")


def datenschutz(request):
    return render(request, "study/datenschutz.html")
