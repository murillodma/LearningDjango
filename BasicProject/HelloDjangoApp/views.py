from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    #html_content = "<html><head><title>Hello, Django</title></head><body>"
    #html_content += "<strong>Hello Django!</strong> on " + now.strftime("%A,%d %B, %Y at %X")
    #html_content += "</body></html>"
    #    return HttpResponse(html_content)

    return render(
        request,
        "HelloDjangoApp/index.html", # Relative path from the 'templates' folder to the template file "index.html",
        {
            'title': "Hello Django",
            'message': "Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
)
