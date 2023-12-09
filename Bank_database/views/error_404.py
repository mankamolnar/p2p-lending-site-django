from django.shortcuts import render

#404 Error handling:
def error_404(request,exception):
    return render(request,"error404.html",{})