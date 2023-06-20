from django.shortcuts import render


# renders the landing page of the website
def home_page_view(request):
    return render(request, 'pages/home_page.html')