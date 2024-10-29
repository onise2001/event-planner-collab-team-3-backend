from rest_framework.filters import BaseFilterBackend


class EventFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        my_events = request.query_params.get('my-events')

        if my_events:
            queryset = queryset.filter(organizer=request.user)

        
        return queryset