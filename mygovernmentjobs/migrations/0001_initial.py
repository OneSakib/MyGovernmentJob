# Generated by Django 3.2.5 on 2021-09-04 15:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdmitCardData',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(default='', max_length=600)),
                ('post_category', models.CharField(choices=[('bank', 'Bank'), ('railway', 'Railway'), ('ssc', 'SSC'), ('defence', 'Defence'), ('army', 'Indian Army'), ('police', 'Police'), ('other', 'Other'), ('state', 'State')], default='', max_length=50)),
                ('admit_card_name', models.CharField(default='', max_length=600)),
                ('post_date_update', models.DateTimeField()),
                ('admit_card_date', models.DateField(blank=True, null=True)),
                ('admit_card_link', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerKeyData',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(default='', max_length=600)),
                ('post_category', models.CharField(choices=[('bank', 'Bank'), ('railway', 'Railway'), ('ssc', 'SSC'), ('defence', 'Defence'), ('army', 'Indian Army'), ('police', 'Police'), ('other', 'Other'), ('state', 'State')], default='', max_length=50)),
                ('answerkey_name', models.CharField(default='', max_length=600)),
                ('post_date_update', models.DateField(blank=True, null=True)),
                ('answerkey_link', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=800)),
                ('desc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='CertificationData',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(default='', max_length=600)),
                ('post_name', models.CharField(default='', max_length=200)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_date_update', models.DateTimeField()),
                ('post_information', models.CharField(default='', max_length=4000)),
                ('app_begin_date', models.DateField(blank=True, null=True)),
                ('last_date', models.DateField(blank=True, null=True)),
                ('complete_last_date', models.DateField(blank=True, null=True)),
                ('pay_examination_fees', models.DateField(blank=True, null=True)),
                ('exam_date', models.DateField(blank=True, null=True)),
                ('admit_card_date', models.DateField(blank=True, null=True)),
                ('age_on_date', models.DateField(blank=True, null=True)),
                ('min_age', models.IntegerField(default='')),
                ('max_age', models.IntegerField(default='')),
                ('gen_fees', models.IntegerField(default='')),
                ('obc_fees', models.IntegerField(default='')),
                ('scst_fees', models.IntegerField(default='')),
                ('eligiblity', models.TextField(default='')),
                ('post_detail', models.TextField(default='')),
                ('e_certificate_coice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('e_certificate_link', models.CharField(default='', max_length=600)),
                ('result_coice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('result_link', models.CharField(default='', max_length=600)),
                ('answerkey_choice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('answerkey_link', models.CharField(default='', max_length=600)),
                ('admit_card_choice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('admit_card_link', models.CharField(default='', max_length=600)),
                ('correction_choice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('correction_link', models.CharField(default='', max_length=600)),
                ('registration_choice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('registration_link', models.CharField(default='', max_length=600)),
                ('login_choice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('login_link', models.CharField(default='', max_length=600)),
                ('download_notification', models.CharField(default='', max_length=600)),
                ('official_website', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Defence',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=800)),
                ('desc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='GovernmentPlan',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(default='', max_length=600)),
                ('plan_name', models.CharField(default='', max_length=600)),
                ('plan_date', models.DateTimeField(blank=True, null=True)),
                ('plan_date_update', models.DateTimeField(blank=True, null=True)),
                ('plan_info', models.CharField(default='', max_length=1000)),
                ('plan_date_begin', models.DateField(blank=True, null=True)),
                ('plan_last_date', models.DateField(blank=True, null=True)),
                ('plan_complate', models.DateField(blank=True, null=True)),
                ('gen_fees', models.IntegerField(default=0)),
                ('obc_fees', models.IntegerField(default=0)),
                ('scst_fees', models.IntegerField(default=0)),
                ('plan_detail', models.TextField(default='')),
                ('registration_coice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('registration_link', models.CharField(default='', max_length=600)),
                ('login_choice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('login_link', models.CharField(default='', max_length=600)),
                ('download_notification', models.CharField(default='', max_length=600)),
                ('official_website', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='IndianArmy',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=800)),
                ('desc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='JobsData',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(default='', max_length=600)),
                ('post_name', models.CharField(default='', max_length=200)),
                ('post_category', models.CharField(choices=[('bank', 'Bank'), ('railway', 'Railway'), ('ssc', 'SSC'), ('defence', 'Defence'), ('army', 'Indian Army'), ('police', 'Police'), ('other', 'Other'), ('state', 'State')], default='', max_length=50)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_date_update', models.DateTimeField()),
                ('post_information', models.CharField(default='', max_length=4000)),
                ('app_begin_date', models.DateField(blank=True, null=True)),
                ('last_date', models.DateField(blank=True, null=True)),
                ('complete_last_date', models.DateField(blank=True, null=True)),
                ('pay_examination_fees', models.DateField(blank=True, null=True)),
                ('exam_date', models.DateField(blank=True, null=True)),
                ('admit_card_date', models.DateField(blank=True, null=True)),
                ('age_on_date', models.DateField(blank=True, null=True)),
                ('min_age', models.IntegerField(default='')),
                ('max_age', models.IntegerField(default='')),
                ('gen_fees', models.IntegerField(default='')),
                ('obc_fees', models.IntegerField(default='')),
                ('scst_fees', models.IntegerField(default='')),
                ('eligiblity', models.TextField(default='')),
                ('post_detail', models.TextField(default='')),
                ('registration_coice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('registration_link', models.CharField(default='', max_length=600)),
                ('login_choice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('login_link', models.CharField(default='', max_length=600)),
                ('download_notification', models.CharField(default='', max_length=600)),
                ('official_website', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='OtherData',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(default='', max_length=600)),
                ('post_name', models.CharField(default='', max_length=200)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_date_update', models.DateTimeField()),
                ('post_information', models.CharField(default='', max_length=4000)),
                ('app_begin_date', models.DateField(blank=True, null=True)),
                ('last_date', models.DateField(blank=True, null=True)),
                ('complete_last_date', models.DateField(blank=True, null=True)),
                ('pay_examination_fees', models.DateField(blank=True, null=True)),
                ('exam_date', models.DateField(blank=True, null=True)),
                ('admit_card_date', models.DateField(blank=True, null=True)),
                ('age_on_date', models.DateField(blank=True, null=True)),
                ('min_age', models.IntegerField(default='')),
                ('max_age', models.IntegerField(default='')),
                ('gen_fees', models.IntegerField(default='')),
                ('obc_fees', models.IntegerField(default='')),
                ('scst_fees', models.IntegerField(default='')),
                ('eligiblity', models.TextField(default='')),
                ('post_detail', models.TextField(default='')),
                ('registration_coice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('registration_link', models.CharField(default='', max_length=600)),
                ('login_choice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('login_link', models.CharField(default='', max_length=600)),
                ('download_notification', models.CharField(default='', max_length=600)),
                ('official_website', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=800)),
                ('desc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Railway',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=800)),
                ('desc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='ResultData',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(default='', max_length=600)),
                ('post_category', models.CharField(choices=[('bank', 'Bank'), ('railway', 'Railway'), ('ssc', 'SSC'), ('defence', 'Defence'), ('army', 'Indian Army'), ('police', 'Police'), ('other', 'Other'), ('state', 'State')], default='', max_length=50)),
                ('result_name', models.CharField(default='', max_length=600)),
                ('post_date_update', models.DateField(blank=True, null=True)),
                ('result_link', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolUniData',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(default='', max_length=600)),
                ('post_name', models.CharField(default='', max_length=200)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('post_date_update', models.DateTimeField()),
                ('post_information', models.CharField(default='', max_length=4000)),
                ('app_begin_date', models.DateField(blank=True, null=True)),
                ('last_date', models.DateField(blank=True, null=True)),
                ('complete_last_date', models.DateField(blank=True, null=True)),
                ('pay_examination_fees', models.DateField(blank=True, null=True)),
                ('exam_date', models.DateField(blank=True, null=True)),
                ('admit_card_date', models.DateField(blank=True, null=True)),
                ('age_on_date', models.DateField(blank=True, null=True)),
                ('min_age', models.IntegerField(default='')),
                ('max_age', models.IntegerField(default='')),
                ('gen_fees', models.IntegerField(default='')),
                ('obc_fees', models.IntegerField(default='')),
                ('scst_fees', models.IntegerField(default='')),
                ('eligiblity', models.TextField(default='')),
                ('post_detail', models.TextField(default='')),
                ('registration_coice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('registration_link', models.CharField(default='', max_length=600)),
                ('login_choice', models.CharField(choices=[('enabled', 'enable'), ('disabled', 'disable')], default='', max_length=10)),
                ('login_link', models.CharField(default='', max_length=600)),
                ('download_notification', models.CharField(default='', max_length=600)),
                ('official_website', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='SSC',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=800)),
                ('desc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=800)),
                ('desc', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='SyllabusData',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.CharField(default='', max_length=600)),
                ('post_category', models.CharField(choices=[('bank', 'Bank'), ('railway', 'Railway'), ('ssc', 'SSC'), ('defence', 'Defence'), ('army', 'Indian Army'), ('police', 'Police'), ('other', 'Other'), ('state', 'State')], default='', max_length=50)),
                ('syllabus_name', models.CharField(default='', max_length=600)),
                ('post_date_update', models.DateField(blank=True, null=True)),
                ('syllabus_link', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='TopPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(default='', max_length=600)),
                ('color', models.CharField(choices=[('bg-secondary', 'Secondary'), ('bg-info', 'Info'), ('bg-danger', 'Danger'), ('bg-warning', 'Warning'), ('bg-primary', 'Primary'), ('bg-success', 'Success'), ('bg-dark', 'Dark')], default='', max_length=20)),
                ('category', models.CharField(choices=[('jobs', 'Latest Jobs'), ('admitcard', 'Admit Card'), ('govtplan', 'Sarkari Yojnaye'), ('result', 'Result'), ('answerkey', 'Answer Key'), ('syllabus', 'Syllabus'), ('schooluni', 'School/University'), ('certification', 'Certification'), ('other', 'Other')], default='', max_length=20)),
                ('slug', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='SyllabusComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.syllabuscomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.syllabusdata')),
            ],
        ),
        migrations.CreateModel(
            name='StatesComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.statescomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.state')),
            ],
        ),
        migrations.CreateModel(
            name='SSCComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.ssccomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.ssc')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolUniComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.schoolunicomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.schoolunidata')),
            ],
        ),
        migrations.CreateModel(
            name='ResultComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.resultcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.resultdata')),
            ],
        ),
        migrations.CreateModel(
            name='RailwayComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.railwaycomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.railway')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.postcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.jobsdata')),
            ],
        ),
        migrations.CreateModel(
            name='PoliceComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.policecomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.police')),
            ],
        ),
        migrations.CreateModel(
            name='OtherComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.othercomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.otherdata')),
            ],
        ),
        migrations.CreateModel(
            name='IndianArmyComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.indianarmycomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.indianarmy')),
            ],
        ),
        migrations.CreateModel(
            name='GovtPlanComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.govtplancomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.governmentplan')),
            ],
        ),
        migrations.CreateModel(
            name='DefenceComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.defencecomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.defence')),
            ],
        ),
        migrations.CreateModel(
            name='CerttificationComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.certtificationcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.certificationdata')),
            ],
        ),
        migrations.CreateModel(
            name='BankComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.bankcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.bank')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerKeyComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.answerkeycomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.answerkeydata')),
            ],
        ),
        migrations.CreateModel(
            name='AdmitCardComment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.admitcardcomment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygovernmentjobs.admitcarddata')),
            ],
        ),
    ]
