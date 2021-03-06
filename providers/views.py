from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render_to_response
from providers.models import Provider
import json

def index(request):
    """
    index view for providers
    """
    providers = Provider.objects.all()
    return render_to_response('providers/index.html', {'providers' : providers})

def getAllProviders(request):
    """
    return json output with all providers
    used by ajax post in map.js
    """
    if request.method == 'POST':
        temp_output = serializers.serialize('python', Provider.objects.all())
        output = json.dumps(temp_output, cls=DjangoJSONEncoder)
        return HttpResponse(output, mimetype="application/json")