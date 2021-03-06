# Generated by Django 4.0.4 on 2022-07-15 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortcode', models.CharField(help_text='lowercase short url. Automatically allocated shortcodes are exactly 6-length. User subitted shortcodes are at leat 4-length.', max_length=20, unique=True, verbose_name='Short URL')),
                ('original_url', models.CharField(help_text='Original long URL', max_length=255, verbose_name='Original URL')),
                ('accessed_count', models.PositiveIntegerField(default=0, editable=False, help_text='How many times this short code is accessed', verbose_name='Accessed Count')),
                ('last_accessed_at', models.DateTimeField(blank=True, editable=False, help_text='Timestamp when the shortcode was last accessed', null=True, verbose_name='Last Accessed')),
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Timestamp when the record was created. The date and time are displayed in the Timezone from where request is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Registered')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the record was modified. The date and time are displayed in the Timezone from where request is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'ShortCode',
                'verbose_name_plural': 'ShortCodes',
            },
        ),
    ]
