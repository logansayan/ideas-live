from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

class CustomUserCrationFrom(UserCreationForm):
  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]

  def __init__(self, *args, **kwargs):
    super(CustomUserCrationFrom, self).__init__(*args, **kwargs)

    self.fields["username"].widget.attrs["placeholder"] = "Username"
    self.fields["email"].widget.attrs["placeholder"] = "Email"
    self.fields["password1"].widget.attrs["placeholder"] = "Password"
    self.fields["password2"].widget.attrs["placeholder"] = "Confirm password"

    for name, field in self.fields.items():
      field.widget.attrs.update({"class": "auth__input"})

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    exclude = ["user", ]


