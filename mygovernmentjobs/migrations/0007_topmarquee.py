# Generated by Django 3.2.5 on 2021-09-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygovernmentjobs', '0006_auto_20210905_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopMarquee',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('post_name1', models.CharField(default='', max_length=600)),
                ('category1', models.CharField(choices=[('jobs', 'Latest Jobs'), ('admitcard', 'Admit Card'), ('govtplan', 'Sarkari Yojnaye'), ('result', 'Result'), ('answerkey', 'Answer Key'), ('syllabus', 'Syllabus'), ('schooluni', 'School/University'), ('certification', 'Certification'), ('other', 'Other')], default='', max_length=20)),
                ('slug1', models.CharField(default='', max_length=600)),
                ('post_name2', models.CharField(default='', max_length=600)),
                ('category2', models.CharField(choices=[('jobs', 'Latest Jobs'), ('admitcard', 'Admit Card'), ('govtplan', 'Sarkari Yojnaye'), ('result', 'Result'), ('answerkey', 'Answer Key'), ('syllabus', 'Syllabus'), ('schooluni', 'School/University'), ('certification', 'Certification'), ('other', 'Other')], default='', max_length=20)),
                ('slug2', models.CharField(default='', max_length=600)),
                ('post_name3', models.CharField(default='', max_length=600)),
                ('category3', models.CharField(choices=[('jobs', 'Latest Jobs'), ('admitcard', 'Admit Card'), ('govtplan', 'Sarkari Yojnaye'), ('result', 'Result'), ('answerkey', 'Answer Key'), ('syllabus', 'Syllabus'), ('schooluni', 'School/University'), ('certification', 'Certification'), ('other', 'Other')], default='', max_length=20)),
                ('slug3', models.CharField(default='', max_length=600)),
                ('post_name4', models.CharField(default='', max_length=600)),
                ('category4', models.CharField(choices=[('jobs', 'Latest Jobs'), ('admitcard', 'Admit Card'), ('govtplan', 'Sarkari Yojnaye'), ('result', 'Result'), ('answerkey', 'Answer Key'), ('syllabus', 'Syllabus'), ('schooluni', 'School/University'), ('certification', 'Certification'), ('other', 'Other')], default='', max_length=20)),
                ('slug4', models.CharField(default='', max_length=600)),
            ],
        ),
    ]
