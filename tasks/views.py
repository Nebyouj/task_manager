from rest_framework import viewsets
from .models import Task
from.serializer import TaskSerializer
from.tasks import send_task_email

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()
        send_task_email.delay(task.id)