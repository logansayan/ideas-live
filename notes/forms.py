from django.forms import ModelForm
from .models import Note

class AddNoteForm(ModelForm):
  class Meta:
    model = Note
    fields = ["title", "body"]

  def __init__(self, *args, **kwargs):
    super(AddNoteForm, self).__init__(*args, **kwargs)

    self.fields["title"].widget.attrs["placeholder"] = "Heading"
    self.fields["title"].widget.attrs["class"] = "form__heading"

    self.fields["body"].widget.attrs["placeholder"] = "Write your note here..."
    self.fields["body"].widget.attrs["class"] = "form__body"