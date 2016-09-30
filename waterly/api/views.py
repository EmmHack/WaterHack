from django.shortcuts import render
from rest_framework.test import APIClient

from api.models  import Consumer


class GetConsumerData(generics.ListCreateAPIView):
    """Get data for particular consumer in the city.
    
    """

    def get(self, *args, **kwargs):
        """Given identifier for the consumer get their current data
        
        Kwargs:
            kwargs['pk'] (str): Meter number for the consumer.

        """

        pk = kwargs['pk']
        queryset = self.get_queryset(pk)
        serializer = ConsumerSerializer(queryset, many=False)

        return Response(serializer.data)


class GetCreateDatasets(generics.ListCreateAPIView):
    """Get or create consumer entry on the api.
    
    Attributes:
        queryset (models): All consumers.
        serializer_class (object): Serializer (json)
            
    """

    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer

