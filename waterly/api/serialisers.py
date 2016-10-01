from rest_framework import serializers

class ConsumerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = ['meter_no', 'name', 'address', 'created_at', 'modified_at']

    def create(self, validated_data):
        meter_no = validated_data.get('meter_no')
        name = validated_data.get('name')
        address = validated_data('address')
        created_at = validated_data.get('created_at')
        modified_at = validated_data.get('modified_at')

        consumer = Consumer.objects.create(meter_no=meter_no, name=name,
                                           address=address,
                                           num_features=num_features,
                                           created_at=created_at,
                                           modified_at=modified_at)

        return consumer


class ConsumptionSerialiser(serializer.ModelSerializer):
    class Meta:
        model = Consumption
        fields = ['meter_no', 'value', 'consumer', 'data']


class AddressSerialiser(serializer.ModelSerializer):
    class Meta:
        model = Address
        fields = ['building_name', 'street_no', 'suburb_name', 
                  'municipality_name', 'province_name']
