from django.urls import path
from Gr33kLibrary import views

urlpatterns = [
    path('about_me/',views.about_me,name='about_me'),
    path('main/',views.page_main,name='page_main'),
    path('login/',views.login,name='login'),
    path('user_manage/<page_num>/',views.user_manage,name='user_manage'),
    path('add_user/',views.add_user,name='add_user'),
    path('edite_user/<user_id>/',views.edite_user,name='edite_user'),
    path('delete_user/',views.delete_user,name='delete_user'),
    path('classify_manage/',views.classify_manage,name='classify_manage'),
    path('add_classify/',views.add_classify,name='add_classify'),
    path('delete_classify/',views.delete_classify,name='delete_classify'),
    path('add_tag/',views.add_tag,name='add_tag'),
    path('delete_tag/',views.delete_tag,name='delete_tag'),
    path('update_log/<page_num>/',views.update_log,name='update_log'),
    path('update_log/',views.update_log_index,name='update_log_index'),
    path('add_update_log/',views.add_update_log,name='add_update_log'),
    path('delete_update_log/<update_log_id>/',views.delete_update_log,name='delete_update_log'),
    path('myarticle/<page_num>/',views.myarticle,name='myarticle'),
    path('create_article/',views.create_article,name='create_article'),
    path('edite_article/<article_id>/',views.edite_article,name='edite_article'),
    path('delete_article/',views.delete_article,name='delete_article'),
    path('tools_manage/<page_num>/',views.tools_manage,name='tools_manage'),
    path('tools_manage/',views.tools_manage_index,name='tools_manage_index'),
    path('search_tools/',views.search_tools,name='search_tools'),
    path('upload_tool/',views.upload_tool,name='upload_tool'),
    path('delete_tool/',views.delete_tool,name='delete_tool'),
    path('article_detail/<article_id>/',views.article_detail,name='article_detail'),
    path('search_result/',views.search_result,name='search_result'),
    path('logout/',views.logout,name='logout'),
    path('my_setting/',views.my_setting,name='my_setting'),
    path('change_user_state/',views.change_user_state,name='change_user_state'),
    path('reset_password/<user_id>/',views.reset_password,name='reset_password'),
    path('download_tool/<tool_id>/',views.download_tool,name='download_tool'),
    path('invitation_code_manage/',views.invitation_code_manage,name='invitation_code_manage'),
    path('register/',views.register,name='register'),
    path('preview/<article_id>/',views.preview,name='preview'),
    path('change_password/',views.change_password,name='change_password'),
    path('verify/',views.verify,name='verify'),
    path('back_article/',views.back_article,name='back_article'),
    path('verify_article/<article_id>/',views.verify_article,name='verify_article'),
    path('show_back_info/',views.show_back_info,name='show_back_info'),
    path('library/',views.library,name='library'),
    path('files/upload/', views.fileupload,name='图片分片上传'),
    path('upload/complete/', views.fileMerge,name='上传成功合并'),
    path('search_author/',views.search_author,name='search_author'),
    path('search_tag/',views.search_tag,name='search_tag'),
    path('search_article/',views.search_article,name='search_article'),
    path('collect/',views.collect,name='collect'),
    path('delete_collect/',views.delete_collect,name='delete_collect'),
    path('mycollect/<page_num>/',views.mycollect,name='mycollect'),
    path('search_collect_article/',views.search_collect_article,name='search_collect_article'),
    path('go_set_classify/',views.go_set_classify,name='go_set_classify'),
    path('set_classify/',views.set_classify,name='set_classify'),
    path('go_set_tags/',views.go_set_tags,name='go_set_tags'),
    path('set_tags/',views.set_tags,name='set_tags'),
    path('delete_articles/',views.delete_articles,name='delete_articles'),
]