from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from .models import timeSheet, pileLogs
from .serializers import timeSheetSerializer, pileLogSerializer


# Create your views here.

class timeSheetViewSet(ModelViewSet):
    queryset = timeSheet.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = timeSheetSerializer


class pileLogViewSet(ModelViewSet):
    queryset = pileLogs.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = pileLogSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        try:
            pile = pileLogs(jobNumber=request.data['jobNumber'], weatherField=request.data['weatherField'],
                            Date=request.data['Date'], wallNumber=request.data['wallNumber'],
                            pileNumber=request.data['pileNumber'], augarDia=request.data['augarDia'],
                            wallType=request.data['wallType'], casing=request.data['casing'],
                            extras=request.data['extras'], signoff=request.data['signoff'])
            pile.save()

        except Exception as e:
            print(e)

        return JsonResponse({"success": "Data created successfully"})
