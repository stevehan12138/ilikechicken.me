import os
import hmac
import hashlib
import json
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from ilikechicken import constants
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def postreceive(request):
    if 'X_GITHUB_EVENT' not in request.headers or 'X_Hub_Signature_256' not in request.headers:
        return HttpResponse(status=400)
    event = request.headers['X_GITHUB_EVENT']
    if event == 'ping':
        return HttpResponse('pong')
    elif event == 'push':
        json_data = json.loads(request.body)
        if json_data['ref'] == 'refs/heads/main':
            signature = hmac.new(constants.POST_RECEIVE_SECRET , request.body, hashlib.sha256).hexdigest()
            expected = request.headers['X_Hub_Signature_256']
            if not hmac.compare_digest(signature, expected):
                return HttpResponse(status=403)
            os.system('bash ./deploy.sh')
            return HttpResponse('success')
    return HttpResponse(status=204)