# Generated by Django 5.1 on 2024-12-06 11:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("review", "0003_alter_review_user_reviewcontributor_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="contributors",
            field=models.ManyToManyField(
                blank=True,
                related_name="contributions",
                through="review.ReviewContributor",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
