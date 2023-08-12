# Generated by Django 4.2.2 on 2023-06-29 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp_test', '0004_goods_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='goods_set', to='erp_test.goodscategory', verbose_name='产品分类'),
        ),
    ]