import os
import hmac
import hashlib
import json
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from ilikechicken import constants
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import force_bytes
from django.shortcuts import render
from blog.models import BlogPost

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
            signature = hmac.new(force_bytes(constants.POST_RECEIVE_SECRET), msg=force_bytes(request.body), digestmod=hashlib.sha256)
            expected = request.headers['X_Hub_Signature_256'].split('=')[1]
            if not hmac.compare_digest(force_bytes(signature.hexdigest()), force_bytes(expected)):
                return HttpResponse(status=403)
        os.system('bash ./deploy.sh')
        return HttpResponse('success')
    return HttpResponse(status=204)


def handler404(request, exception):
    return render(request, "page/404.html", status=404)

def home_page(request):
    blogs = BlogPost.objects.all()
    blog_count = len(blogs)
    return render(request, "page/index.html", {'blogs': blogs, 'blog_count': blog_count})