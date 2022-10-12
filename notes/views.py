from django.shortcuts import render, redirect
from .models import Note
from .forms import AddNoteForm
from users.models import Profile
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def all_notes(request):
  user = request.user.profile.id
  notes = Note.objects.filter(owner=user)
  context = {
    "notes": notes,
    "user": user
  }
  return render(request, "notes/all_notes.html", context)

@login_required(login_url="login")
def add_note(request):
  profile = request.user.profile
  form = AddNoteForm()
  if request.method == "POST":
    form = AddNoteForm(request.POST)
    if form.is_valid():
      note = form.save(commit=False)
      note.owner = profile
      note.save()
      return redirect("all_notes")

  context = {
    "form": form
  }
  return render(request, "notes/note_form.html", context)

@login_required(login_url="login")
def edit_note(request, note_id):
  page = "edit"
  profile = request.user.profile
  note = profile.note_set.get(id=note_id)
  created = note.created
  form = AddNoteForm(instance=note)
  if request.method == "POST":
    form = AddNoteForm(request.POST, instance=note)
    if form.is_valid():
      form.save()
      return redirect("all_notes")
  
  context = {
    "form": form,
    "page": page,
    "created": created
  }
  return render(request, "notes/note_form.html", context)

@login_required(login_url="login")
def delete_note(request, note_id):
  note = Note.objects.get(id=note_id)
  if request.method == "POST":
    note.delete()
    messages.success(request, f"Deleted \"{note}\" successfully")
    return redirect("all_notes")
  context = {
    "object": note
  }
  return render(request, "notes/delete_note.html", context)