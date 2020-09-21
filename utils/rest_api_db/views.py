from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class RestApiModelViewSet(ViewSet):
    queryset = None
    serializer_class = None

    def list(self, request, *args, **kwargs):
        conditions = self.queryset.manager.model.translate_query_params_to_conditions(
            request.query_params)
        results = self.queryset.filter(**conditions)
        serializer = self.serializer_class(results, many=True)
        return Response(serializer.data)

