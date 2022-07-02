def add_variable_to_context(request):
    projectInfo = "Capstone Project"
    teamMembers = ["Masum", "Shad", "Samir", "Wasif"]

    # key matters in rendering...
    everyWhere = {
        'projectInfo': projectInfo,
        'team_members': teamMembers,
    }
    return everyWhere
