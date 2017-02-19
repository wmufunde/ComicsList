from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from listOfComics.models import Comics


class ComicsForm(ModelForm):
    class Meta:
        model = Comics
        fields = ['title', 'publisher', 'issue', 'writer_artist', 'releaseDate']
        
 #       ComicsFormSet = inlineformset_factory(Comics, form=ComicsForm, extra=1)
