from rest_framework import mixins
from rest_framework import generics
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer, AdminRenderer

from pipeline import manager
from avi.models import DemoModel
from avi.serializers import DemoModelSerializer

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARN)

class DemoModelList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = DemoModel.objects.all()
    serializer_class = DemoModelSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, AdminRenderer)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DemoModelDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = DemoModel.objects.all()
    serializer_class = DemoModelSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, AdminRenderer)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)