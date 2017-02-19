from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView, UpdateView

from listOfComics.models import Comics

from listOfComics.forms.comics import ComicsForm

class ComicsView(FormView):
    template_name = 'comics.html'
    form_class = ComicsForm
    success_url = '/listOfComics/success'
    
    def form_valid(self, form):
        form.save()
        super(ComicsView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)