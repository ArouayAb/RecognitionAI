# Generated by Django 4.0.4 on 2022-06-23 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmotionDetector', '0002_alter_emotionhistoric_emotion_percentage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmotionHistoric',
            new_name='InferenceModel',
        ),
    ]