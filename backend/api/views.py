from django.http import JsonResponse
from django.forms.models import model_to_dict

from product.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    '''
    DRF API views
    '''
    
    if request.method != "GET":
        return Response({"detail":"GET not allowed"}, status=405)

    model_data= Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data=model_to_dict(model_data, fields=['title','price'])
    return Response(data)
        # data['title']= model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
    # return JsonResponse({"message": "Hi there this is your django API response!!"})