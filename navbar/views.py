from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.html import escape
import json

def index(request):
    return render(request, 'navbar/index.html')


@csrf_exempt
def showCodigo(request):

	html = ''
	if request.method == 'POST':
		print("Entre a la vista!!!")
		url = request.POST

		listaJson = []

		for i in url:
			lista = json.loads(i)

		print("La lista es:",lista)	
		html = render_to_string('navbar/navbar.html', { 'lista': lista })
		print(html)

	context = {'html':html}
	template = loader.get_template('navbar/navbarCodigo.html')
	return HttpResponse(template.render(context,request))
		

