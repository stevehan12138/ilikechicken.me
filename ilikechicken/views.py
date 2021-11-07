import os
import hashlib
import json
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from ilikechicken import constants
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def postreceive(request):
    if 'X_GITHUB_EVENT' not in request.headers:
        return HttpResponse(status=400)
    event = request.headers['X_GITHUB_EVENT']
    if event == 'ping':
        return HttpResponse('pong')
    elif event == 'push':
        json_data = json.loads(request.body)
        if hashlib.sha256().update(json_data['hook']['config']['secret']).hexdigest() == constants.POST_RECEIVE_SECRET:
            os.system('bash ./deploy.sh')
        else:
            return HttpResponse('Invalid secret key')
    return HttpResponse(status=204)