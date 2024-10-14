from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
# def login(request):
#     try:
#         kakao_account = KakaoUser.objects.get(user=request.user, provider='kakao')
#         extra_data = kakao_account.extra_data
#         context = {
#             'nickname': extra_data.get('properties', {}).get('nickname', ''),
#             'profile_image': extra_data.get('properties', {}).get('profile_image', ''),
#         }
#     except KakaoUser.DoesNotExist:
#         context = {}
#     return render(request, 'accounts/login.html', context)

def login_view(request):
    return render(request, 'accounts/login.html')
