from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import Formulario
from django.urls import reverse_lazy

# Create your views here.


class index(FormView):
  template_name = "index.html"
  form_class = Formulario
  success_url = reverse_lazy('success')
  initial = {'message': 'Mensagem Inicial'}

  def post(self, request, *args, **kwargs):
        initial = None
        form = Formulario(initial=initial, data=request.POST)
        if form.is_valid():
          return render(request, 'success.html', {'form': form})

class success(TemplateView):
  template_name = "success.html"

