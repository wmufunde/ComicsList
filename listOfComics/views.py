from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView, UpdateView, DeleteView

from listOfComics.models import Comic

from listOfComics.forms.comics import ComicsForm

from django.contrib.auth.decorators import login_required 

from django.views.generic.detail import DetailView

class ComicsView(FormView):
    template_name = 'comics.html'
    form_class = ComicsForm
    success_url = '/listOfComics/success'
    
    def form_valid(self, form):
        form.save()
        super(ComicsView, self).form_valid(form)
        
        return HttpResponseRedirect(self.success_url)
    
#@login_required
def my_list(request, template='my_list.html'):
    comics = Comic.objects.all()
    context = {
        'comics': comics,
    }
    return render_to_response(template, context)

    
class IssueView(DetailView):
    template_name = 'comic_issue.html'
    model = Comic
    
class ComicUpdateView(UpdateView):
    template_name = 'comics.html'
    success_url = '/listOfComics/my_list'
    model = Comic
    form_class = ComicsForm
    
class ComicDeleteView(DeleteView):
    template_name = 'comic_confirm_delete.html'
    model = Comic
    success_url = '/listOfComics/my_list'