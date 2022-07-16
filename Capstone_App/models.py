from django.db import models
import django_filters
from django.utils.safestring import mark_safe

MAX_LENGTH = 250


class sign_up(models.Model):
    name = models.CharField(verbose_name='Username', max_length=100)
    password = models.CharField(verbose_name='Password', max_length=60)
    email = models.EmailField(verbose_name='Email', max_length=60)

    class Meta:
        verbose_name = 'Sign Up'
        verbose_name_plural = 'Sign Up'
        db_table = 'sign_up'

    def __str__(self):
        return "%s" % (self.email)


# for filtering out in admin section
class SignUpFilter(django_filters.FilterSet):
    class Meta:
        model = sign_up
        fields = ['email', 'name']


class Testimonial(models.Model):
    person = models.CharField(max_length=MAX_LENGTH, verbose_name="Person", blank=True, null=True)
    designation = models.CharField(max_length=MAX_LENGTH, verbose_name="Designation", blank=True, null=True)
    testimonial = models.CharField(max_length=MAX_LENGTH, verbose_name="Testimonial", blank=True, null=True)
    person_link = models.URLField(max_length=MAX_LENGTH, verbose_name="Person's Link", blank=True, null=True)
    person_pic = models.ImageField(upload_to='testimonials/%Y/%m/%d/', blank=True, null=True,
                                   verbose_name="Person's Picture")

    def image_tag(self):
        return mark_safe("<img src='./media/%s' />" % (self.person_pic))

    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Testimonials'
        verbose_name_plural = 'Testimonials'
        db_table = 'testimonial'

    def __str__(self):
        return "%s" % (self.person)


class Video(models.Model):
    video_holder = models.ForeignKey(sign_up, on_delete=models.DO_NOTHING, related_name='Videos')
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return self.caption


class WorkPlan(models.Model):
    workplan_title = models.CharField(max_length=MAX_LENGTH, verbose_name="Workplan Title", blank=True, null=True)
    workplan_sheduled = models.DateField(verbose_name='Scheduled At', blank=True, null=True)
    workplan_summary = models.TextField(max_length=MAX_LENGTH, verbose_name="Workplan Summary", blank=True, null=True)
    workplan_link = models.URLField(max_length=MAX_LENGTH, verbose_name="WorkPlan Link", blank=True, null=True)

    class Meta:
        verbose_name = 'Work-Plans'
        verbose_name_plural = 'Work-Plans'
        db_table = 'workplan'

    def __str__(self):
        return self.workplan_title


class FAQ_Section(models.Model):
    faq_question = models.CharField(max_length=MAX_LENGTH, verbose_name="FAQ Question", blank=True, null=True)
    faq_answer = models.TextField(max_length=500, verbose_name="FAQ Answer", blank=True, null=True)

    class Meta:
        verbose_name = 'FAQ Section'
        verbose_name_plural = 'FAQ Section'
        db_table = 'faq_section'

    def __str__(self):
        return self.faq_question


class Team_Section(models.Model):
    member_name = models.CharField(max_length=MAX_LENGTH, verbose_name="Member's Name", blank=True, null=True)
    member_designation = models.CharField(max_length=MAX_LENGTH, verbose_name="Member's Designation", blank=True,
                                          null=True)
    member_about = models.TextField(max_length=MAX_LENGTH, verbose_name="About Summary of Member", blank=True,
                                    null=True)
    member_github = models.URLField(max_length=MAX_LENGTH, verbose_name="Member's Github Link", blank=True, null=True)
    member_facebook = models.URLField(max_length=MAX_LENGTH, verbose_name="Member's FaceBook Link", blank=True,
                                      null=True)
    member_linkedin = models.URLField(max_length=MAX_LENGTH, verbose_name="Member's LinkedIn Link", blank=True,
                                      null=True)
    member_pic = models.ImageField(upload_to='team/', blank=True, null=True,
                                   verbose_name="Person's Picture")

    def image_tag(self):
        return mark_safe("<img src='./media/%s' />" % (self.member_pic))

    image_tag.allow_tags = True

    class Meta:
        verbose_name = 'Team Section'
        verbose_name_plural = 'Team Section'
        db_table = 'team_section'

    def __str__(self):
        return self.member_name
