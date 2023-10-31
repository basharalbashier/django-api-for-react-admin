from django.http import JsonResponse
from .models import Contact
from .serializer import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def contacts_list(request):
    if request.method=='GET':
        contact = Contact.objects.all()
        serlializer = ContactSerializer(contact,many=True)
        return JsonResponse(serlializer.data,safe=False)
    
    
    if request.method == 'POST':
        serlializer= ContactSerializer(data=request.data)
        if serlializer.is_valid():
            serlializer.save()
            return Response(serlializer.data,status=status.HTTP_201_CREATED)
        
        
@api_view(['GET','PUT','DELETE'])       
def contact_details(request,id):
    try:
        contact= Contact.objects.get(pk=id)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method=='GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid ():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)