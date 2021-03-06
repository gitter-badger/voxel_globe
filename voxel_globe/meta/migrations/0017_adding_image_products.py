# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0016_remove_event_trigger_origin'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemImage',
            fields=[
                ('image_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='meta.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('meta.image',),
        ),
        migrations.CreateModel(
            name='DerivativeImage',
            fields=[
                ('image_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='meta.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('meta.image',),
        ),
        migrations.CreateModel(
            name='DisplayImage',
            fields=[
                ('image_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='meta.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('meta.image',),
        ),
        migrations.RenameField(
            model_name='image',
            old_name='coverage_poly',
            new_name='coverage',
        ),
        migrations.AddField(
            model_name='displayimage',
            name='images',
            field=models.ManyToManyField(related_name='display_image', to='meta.Image'),
        ),
        migrations.AddField(
            model_name='derivativeimage',
            name='images',
            field=models.ManyToManyField(related_name='derivative_image', to='meta.Image'),
        ),
    ]
