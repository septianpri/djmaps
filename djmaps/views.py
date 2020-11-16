from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import FileUploadParser
from datetime import tzinfo, timedelta, datetime
import pytz
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from . import serializers
from . import models
import os
from django.conf import settings
import pprint
from rest_framework.parsers import MultiPartParser
from . import query as querynya
from django.db import connection
# Create your views here.

from rest_framework import filters

class Poi(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""
    serializer_class = serializers.Poi
    queryset = models.djmaps.objects.all()
    #filter_backends = (filters.gid,)
    #queryset = models.portpoi.objects.all().order_by('gid')
    # filter_backends = (filters.SearchFilter,)
    # search_fields = {'dateNotif',}


class PoiAP(APIView):

    serializer_class = serializers.Poi

    def get(self, request, format=None):
        req = request.GET.copy()
        oQuery = querynya.poidepok.getZoneVolume(req)
        cursor = connection.cursor()
        cursor.execute(oQuery)

        curData = cursor.fetchall()
        connection.close()

        listData = []

        try:
            for i in curData:
                listData.append({'gid': i[1], 'nama': i[2], 'alamat': i[3], 'kecamatan': i[4], 'keterangan': i[5], 'kategori': i[6], 'kelurahan': i[7], 'imgpath': i[8], 'id_kec': i[10], 'id_kel': i[11], 'geomjson': i[12]})
        except IndexError:
            pprint('error')

        return Response(listData)
