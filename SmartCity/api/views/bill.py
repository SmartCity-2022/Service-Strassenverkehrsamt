from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Bill
from ..serializers import BillSerializer


@api_view(["GET"])
def get_all_bills(request):
    bills = Bill.objects.all()
    serializer = BillSerializer(bills, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_bill(request):
    serializer = BillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["GET"])
def get_bill_by_id(request, id):
    try:
        bill = Bill.objects.get(pk=id)
    except Bill.DoesNotExist:
        return Response(status=404)    
    serializer = BillSerializer(bill, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_bill_by_user(request):
    
    # TODO: Verify user by token from request first
    
    try:
        bills = Bill.objects.filter(owner=request.owner)    
    except Bill.DoesNotExist:
        return Response(status=404)        
    serializer = BillSerializer(bills, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_bill_by_id(request, id):
    
    # TODO: Verify user by token from request first
    
    try:
        bill = Bill.objects.get(pk=id)    
    except Bill.DoesNotExist:
        return Response(status=404)   
    bill.delete()
    return Response(status=200)