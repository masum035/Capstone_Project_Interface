from .models import *


def add_variable_to_context(request):
    projectInfo = "Capstone Project"
    teamMembers = Team_Section.objects.all()
    testimonials = Testimonial.objects.all()
    workplans = WorkPlan.objects.all()
    frequent_faq = FAQ_Section.objects.all()

    # key matters in rendering...
    everyWhere = {
        'projectInfo': projectInfo,
        'team_members': teamMembers,
        'given_testimonials': testimonials,
        'implemented_workplans': workplans,
        'faq_section': frequent_faq,
    }
    return everyWhere
