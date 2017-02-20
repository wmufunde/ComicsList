from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from listOfComics.models import Comic


class ComicsForm(ModelForm):
    class Meta:
        model = Comic
        fields = ['title', 'cover', 'publisher', 'issue', 'writer_artist', 'releaseDate']

