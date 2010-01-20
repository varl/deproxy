from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    from urllib2 import urlopen

    url = request.GET.get('url', '') 
    if (url == ''):
        return HttpResponse("Nyaaah no param")
    else:
        return render_to_response('proxy/index.html', {'url': url})

def render(request):
    from urllib2 import urlopen
    from BeautifulSoup import BeautifulSoup

    url = request.GET.get('url', '') 
    if (url == ''):
        return HttpResponse("Nyaaah no param")
    else:
        soup = BeautifulSoup(urlopen(url))
        anchors = soup.findAll('a')
        images = soup.findAll('img')

        for anchor in anchors:
            anchor['href'] = url + anchor['href']
        for image in images:
            image['src'] = url + image['src']

        return HttpResponse(soup)
