# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # check checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    extraspaceremove = request.POST.get('extraspaceremove','off')
    charcount = request.POST.get('charcount','off')


    # remove punctuations from input
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    # capitalzed input
    if fullcaps == "on" :
        analyzed = ""
        for char in djtext :
            analyzed += char.upper()

        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    # new line remover --
    if newlineremove == "on" :
        analyzed = ""
        for char in djtext :
            if char != "\n" and char != "\r":
                analyzed += char 

        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    # extra Space remover 
    if extraspaceremove == "on":
        analyzed = " ".join(djtext.split())

        params = {'purpose': 'Remove Extra Space','analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    # character count
    if charcount == "on" :
        analyzed = ""
        count = 0
        for char in djtext :
            analyzed += char
            count += 1

        op = f"text = {analyzed},  count = {count}"
        params = {'purpose': 'Count Character', 'analyzed_text': op}
        
        return render(request, 'analyze.html', params)


    # if not select any functions
    if (removepunc != "on" and fullcaps != "on" and newlineremove != "on" and extraspaceremove != "on") :
        return HttpResponse("Please select any operations")

    else : 
        return render(request, 'analyze.html', params)


     
def index(request):
    return render(request, 'index.html')

def youtube(request):
    return render(request, 'youtube.html')
        
def contact(request):
    return render(request, 'contact.html')   
    

