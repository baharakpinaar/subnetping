from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PingResult
from .serializers import PingResultSerializer
from .utils import calculate_subnet_ips, ping_ip

class SubnetPingView(APIView):

    def post(self, request):
        ip = request.data.get('ip')
        subnet_mask = request.data.get('subnet_mask')

        # IP ve subnet kontrolü yapılıyor
        try:
            ips = calculate_subnet_ips(ip, subnet_mask)
        except ValueError:
            return Response({"error": "Invalid IP address or subnet mask"}, status=status.HTTP_400_BAD_REQUEST)

        results = []
        for ip in ips:
            status = "active" if ping_ip(str(ip)) else "inactive"
            result = PingResult.objects.create(ip_address=str(ip), status=status)
            results.append(result)

        serializer = PingResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        results = PingResult.objects.all()
        serializer = PingResultSerializer(results, many=True)
        return Response(serializer.data)
