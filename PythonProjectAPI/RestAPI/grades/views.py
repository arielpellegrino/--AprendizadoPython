
def grades(request):
    if request.method =='GET':
        return HttpResponse("ok!")