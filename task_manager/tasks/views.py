from rest_framework import viewsets, filters, status
from rest_framework.response import Response

from tasks.models import Task
from tasks.producer import send_task
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["status"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()

        send_task({
            'id': task.id,
            'title': task.title,
            'description': task.description,
        })

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)