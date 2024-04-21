from django.db.models import Model, CharField, TextField, DateTimeField


class News(Model):
    title = CharField(max_length=500)
    body = TextField()
    # date
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
