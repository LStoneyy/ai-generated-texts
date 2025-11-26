from django.shortcuts import render, redirect


# Startseite
def start(request):
    if request.method == "POST":
        # für jetzt nur direkt zur Klassifizierung weiterleiten
        return redirect("study:classify", index=1)
    return render(request, "study/start.html")


# Klassifizierungsseite
def classify(request, index):
    return render(request, "study/classify.html")


# Abschlussseite
def finish(request):
    return render(request, "study/finish.html")
