import json

from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response


# Create your views here.
def uepay(request):
    if request.method == 'GET':
        result = {}
        username = request.GET.get('username')
        mobile = request.GET.get('mibile')
        data = request.GET.get('data')
        result['username'] = username
        result['mibileName'] = mobile
        result['data'] = data
        result = json.dumps(result)
        return HttpResponse(result)
    elif request.method == 'POST':
        username = request.POST.get('username')
        return HttpResponse(username, content_type='application/json;charset=utf-8')
    else:
        return render_to_response('uepay.html')
