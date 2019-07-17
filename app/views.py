from rest_framework.response import Response
from rest_framework.views import APIView


class SomeView(APIView):
    def get(self, request):
        data = {"a": "b", "c": "d"}
        return Response(data)
