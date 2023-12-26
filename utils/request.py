import random
import string
import os

from requests_toolbelt.multipart.encoder import MultipartEncoder

def get_request():
    user_agent = os.getenv("USER_AGENT")
    file_path = "./resources/seed.html"
    boundary = '----WebKitFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

    encoder = MultipartEncoder(
        fields={'image': ('seed.html', open(file_path, 'rb'), 'text/plain'), "submit": "submit"},
        boundary=boundary,
    )
    headers = {'Content-Type': encoder.content_type, 'User-Agent': user_agent, "Connection": "keep-alive"}

    return headers, encoder