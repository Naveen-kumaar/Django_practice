from django.shortcuts import render

# Create your views here.
# def cookies_view(request):
#     count= request.COOKIES.get('count',0)
#     totalCount = int(count) + 1
#     response = render(request,'sessionapp/index.html',{'count':totalCount})
#     response.set_cookie('count',totalCount)
#     return response
def cookies_view(request):
    count = request.session.get('count',0)
    totalcount = int(count) + 1
    request.session['count'] = totalcount
    print(request.session.get_expiry_date())
    return render(request,'sessionapp/index.html',{'count':totalcount})