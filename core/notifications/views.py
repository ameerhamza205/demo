from django.shortcuts import render

# Create your views here.
def notification_page_view(request):
    return render(request, 'notifications/notifications_page.html',)