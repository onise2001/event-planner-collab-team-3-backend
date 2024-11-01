from rest_framework.filters import BaseFilterBackend


class EventFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        my_events = request.query_params.get('my-events')

        if my_events:
            queryset = queryset.filter(organizer=request.user)

        print(queryset)
        return queryset
    

class EventFilesFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        event_id = request.query_params.get('event_id')

        if event_id:
            queryset = queryset.filter(event__id=event_id)

        return queryset
    



class RSVPFilesFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        event_id = request.query_params.get('event_id')

        if event_id:
            queryset = queryset.filter(event__id=event_id)

        return queryset
    