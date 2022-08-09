from django.http import Http404 , JsonResponse

# Create your views here.
def index(request):
    header_name = request.META.get('HTTP_NAME', 'unknown')
    if header_name == "Prithvi" or header_name == "Sagar":
        print("==> in if " , header_name)
        return JsonResponse({"response" : "hola world"})
    raise Http404
