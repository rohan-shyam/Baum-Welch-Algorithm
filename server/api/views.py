from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
def run_baum_welch(req):
    data = req.data 
    iterations = data.get('iterations')
    states = data.get('states')
    sequence = data.get('sequence')
    
    

    final_probability = 0.5
    
    return Response({
        "status": "success",
        "message": "Algorithm completed",
        "final_probability": final_probability,
        "received_sequence_length": len(sequence)
    })
