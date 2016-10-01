from django.shortcuts import render
from rest_framework.test import APIClient
from rest_framework import generics

from api.models  import Consumer, Address


class GetConsumptionData(generics.ListCreateAPIView):
    """Get consumption data for particular consumer in the city.
    
    """

    def get(self, *args, **kwargs):
        """Given identifier for the consumer get their consumption data
        
        Kwargs:
            kwargs['meter_no'] (str): Meter number for the consumer.

        """

        meter_no = int(kwargs['meter_no'])
        queryset = self.get_queryset(meter_no)
        serializer = ConsumerSerializer(queryset, many=True)

        return Response(serializer.data)

    def get_queryset(self, meter_no):
        """Construct queryset based on the given consumer.
        
        Args:
            meter_no (str): Meter number.

        Returns:
           QuerySet: All the consumption records for the consumer.

        """

        # TODO: Specify the start date to read from

        queryset = Consumption.objects.filter(meter_no=meter_no)
        return queryset


class GetConsumers(generics.ListAPIView):
    """Get consumer entries from the api.
    
    Attributes:
        queryset (models): All consumers.
        serializer_class (object): Serializer (json)
            
    """

    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class AddListConsumers(generics.ListCreateAPIView):
    """Add consumer consumption for the day. 
    
    Attributes:
        queryset (models): All Consumers.
        serializer_class (object): Serializer (json)
            
    """

    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerialiser


class ListCreateConsumerAddress(generics.ListCreateAPIView):
    """Create or List consumer addres given meter_no.
    
    Attributes:
        queryset (models): All Addresses.
        serializer_class (object): Serializer (json)
            
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerialiser


class GetConsumerAddress(generics.ListCreateAPIView):
    """Get consumer address given the meter number.
    
    """

    def get(self, *args, **kwargs):
        """Given meter number get consumer address as model
        
        Kwargs:
            kwargs['meter_no'] (str): Meter number for the consumer.

        """

        meter_no = int(kwargs['meter_no'])
        queryset = self.get_queryset(meter_no)
        serializer = AddressSerialiser(queryset, many=False)

        return Response(serializer.data)

    def get_queryset(self, meter_no):
        """Construct queryset based on the given consumer.
        
        Args:
            meter_no (str): Meter number.

        Returns:
           model: The address of a give consumer.

        """

        queryset = Address.objects.filter(meter_no=meter_no)[0]
        return queryset
