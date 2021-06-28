from rest_framework import generics
from django.db.models import OuterRef, F, Subquery

from estate.models import StatusHistory
from estate import serializers
from rest_framework.exceptions import ValidationError

CONST_ALLOWED_STATUS_USER = ['pre_venta', 'en_venta', 'vendido']


class StatusPropertyViewSet(generics.ListAPIView):
    """Manage petitions for users over properties query"""
    serializer_class = serializers.StatusHistorySerializer
    queryset = StatusHistory.objects.all()

    def get_queryset(self):
        """Retrieves the properties for user"""
        city = self.request.query_params.get('city')
        status = self.request.query_params.get('status')
        year = self.request.query_params.get('year')
        queryset = self.queryset
        newest = StatusHistory.objects. \
            filter(property=OuterRef('property')). \
            order_by('-id')
        queryset = queryset. \
            annotate(newest_status_id=Subquery(newest.values('id')[:1])). \
            filter(id=F('newest_status_id'))
        try:
            if city:
                queryset = queryset.filter(property__city__contains=city)
            if status:
                queryset = queryset.filter(status__id=int(status))
            if year:
                queryset = queryset.filter(property__year=int(year))
        except ValueError:
            raise ValidationError(
                detail="some filters arent in correct format"
            )

        return queryset.filter(status__name__in=CONST_ALLOWED_STATUS_USER)
