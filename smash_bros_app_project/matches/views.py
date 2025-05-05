# matches/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Match
from .forms import MatchForm
from django.core.paginator import Paginator
from django.shortcuts import render

def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matches:match_list')
    else:
        form = MatchForm()
    return render(request, 'matches/match_form.html', {'form': form})

def match_list(request):
    matches = Match.objects.all().order_by('-match_time')
    return render(request, 'matches/match_list.html', {'matches': matches})

def delete_match(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == 'POST':
        match.delete()
        return redirect(reverse('matches:match_list'))
    return render(request, 'matches/confirm_delete.html', {'match': match})

def edit_match(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('matches:match_list')
    else:
        form = MatchForm(instance=match)
    return render(request, 'matches/edit_match.html', {'form': form})

def match_list(request):
    match_list = Match.objects.order_by('-match_time')
    paginator = Paginator(match_list, 10)  # 🔸 1ページに15件

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'matches/match_list.html', {'page_obj': page_obj})