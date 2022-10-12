from django.urls import path
from . import views

urlpatterns = [
  path("all_notes/", views.all_notes, name="all_notes"),
  path("add_note/", views.add_note, name="add_note"),
  path("<uuid:note_id>/edit_note", views.edit_note, name="edit_note"),
  path("<uuid:note_id>/delete_note/", views.delete_note, name="delete_note")
]
