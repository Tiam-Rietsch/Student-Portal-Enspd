from django.shortcuts import render


# renders the landing page of the website
def index(request):
    return render(request, 'pages/index.html')


# renders the home page of ENSPD
def enspd_home_page_view(request):
    return render(request, 'pages/ENSPD/enspd_home_page.html')