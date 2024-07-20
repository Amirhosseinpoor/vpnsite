from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from useraccount.models import CustomUser
from extract import Extractor

@login_required
def link_to_fragment(request):
    if request.method == 'POST':
        link = request.POST['link']
        info = Extractor(link)
        user = request.user
        user.vpn_link = link
        user.fragment = info.final_output()[1]
        user.save()

        return render(request, 'input_month_user.html')

    return render(request, 'input_link.html')

def month_user(request):
    if request.method == 'POST':
        month = request.POST['month']
        user_number = request.POST['user']
        user = request.user
        user.month = month
        user.user = user_number
        user.save()
        return render(request, 'output.html')
    return render(request, 'input_month_user.html')

