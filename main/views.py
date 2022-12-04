from django.shortcuts import render

from .models import Division, DivisionLevel


def index(request):
    query = Division.objects.filter(level=DivisionLevel.LEVEL_1)
    return render(request, "base.html", {"divisions": query})
