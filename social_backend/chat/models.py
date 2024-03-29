from django.db import models
import uuid
from django.utils.timesince import timesince
from account.models import User


class Conversation(models.Model):
    id = models.UUIDField(primary_key =True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created_at',)

    def modified_at_formatted(self):
        return timesince(self.created_at)

class ConversationMessage(models.Model):
    id = models.UUIDField(primary_key =True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    body = models.TextField()
    sent_to = models.ForeignKey(User, related_name='recived_messages', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    class Meta:
        ordering = ('created_at',)

    def created_at_formatted(self):
        return timesince(self.created_at)