from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0140_album_m2m_unique_constraints"),
    ]

    operations = [
        migrations.AddField(
            model_name="albumuser",
            name="locked",
            field=models.BooleanField(default=False),
        ),
    ]
