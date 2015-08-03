from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index, "root"),
    url(r'^survey_load/$', views.load_survey, "load-survey"),
    url(r'^survey/(?P<survey_id>\d+)/$', views.survey_view, "survey-detail"),
    url(r'^admin_login/$', views.admin_login, name="admin-login"),
    url(r'^admin_panel/$', views.admin_panel, name="admin-panel"),
    url(r'^admin_panel/survey_delete/$', views.survey_delete, name="admin-survey-delete"),
    url(r'^admin_panel/survey/(?P<survey_id>\d+)/$', views.admin_answers, name="answer-detail"),
    url(r'^admin_panel/survey_create_view/$', views.survey_create_view, name="admin-survey-create-view"),
    url(r'^admin_panel/survey_create/$', views.survey_create, name="admin-survey-create"),
    url(r'^admin_panel/question_add_view/$', views.question_add_view, name="admin-question-add-view"),
    url(r'^admin_panel/question_add/$', views.question_add, name="admin-question-add"),
    url(r'^admin_panel/choice_add_view/$', views.choice_add_view, name="admin-choice-add-view"),
    url(r'^admin_panel/choice_add/$', views.choice_add, name="admin-choice-add"),
    url(r'^admin_panel/survey_delete/$', views.survey_delete, name="admin-survey-delete"),

]