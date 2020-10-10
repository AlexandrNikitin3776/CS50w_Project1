from encyclopedia import util
from django import forms
from django.forms import ValidationError


def validate_page_title(page_title):
    if page_title.lower() in list(map(lambda x: x.lower(), util.list_entries())):
        raise ValidationError("Article already exists.")


class NewPageForm(forms.Form):
    page_title = forms.CharField(
        validators=[validate_page_title],
        max_length=20,
        label="",
        help_text="Enter a page title",
    )
    content = forms.CharField(
        widget=forms.Textarea(),
        label="",
        help_text="Enter a Markdown page content",
    )

class EditPageForm(forms.Form):
    page_title = forms.CharField(
        max_length=20,
        label="",
        help_text="Enter a page title",
    )
    content = forms.CharField(
        widget=forms.Textarea(),
        label="",
        help_text="Enter a Markdown page content",
    )
