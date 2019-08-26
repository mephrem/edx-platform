# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_modes', '0007_coursemode_bulk_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemode',
            name='currency',
            field=models.CharField(default='usd', max_length=8, choices=[(b'tzs', b'TSh'), (b'kes', b'KSh'), (b'zmk', b'K'), (b'etb', b'Br'), (b'eur', b'\xe2\x82\xac'), (b'usd', b'$'), (b'lsl', b'L'), (b'gbp', b'\xc2\xa3')]),
        ),
    ]
