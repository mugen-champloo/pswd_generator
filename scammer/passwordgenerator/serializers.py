from rest_framework import serializers


class PasswordGenerateSerializer(serializers.Serializer):
    lenght = serializers.IntegerField(default=8)
    use_digit = serializers.BooleanField(default=True)
    use_rus = serializers.BooleanField(default=True)
    use_upper_rus = serializers.BooleanField(default=True)
    use_eng = serializers.BooleanField(default=True)
    use_upper_eng = serializers.BooleanField(default=True)
    use_spec_simbols = serializers.BooleanField(default=True)