import os
import hmac
import hashlib
import json
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from ilikechicken import constants
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import force_bytes

@csrf_exempt
@require_POST
def postreceive(request):
    if 'X_GITHUB_EVENT' not in request.headers or 'X_Hub_Signature_256' not in request.headers:
        return HttpResponse(status=400)
    json_data = json.loads(request.body)
    if json_data['ref'] == 'refs/heads/main':
        signature = hmac.new(force_bytes(constants.POST_RECEIVE_SECRET), msg=force_bytes(request.body), digestmod=hashlib.sha256)
        expected = request.headers['X_Hub_Signature_256'].split('=')[1]
        if not hmac.compare_digest(force_bytes(signature.hexdigest()), force_bytes(expected)):
            return HttpResponse(status=403)
    event = request.headers['X_GITHUB_EVENT']
    if event == 'ping':
        return HttpResponse('pong')
    elif event == 'push':
        os.system('bash ./deploy.sh')
        return HttpResponse('success')
    return HttpResponse(status=204)