from django.urls import path

from yeager_ai.users.views import user_detail_view, user_logout_view, \
    user_redirect_view, user_update_view, user_list_view, user_sign_view, user_login_view

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("login/", view=user_login_view, name="login"),
    path("logout/", view=user_logout_view, name="logout"),
    path("register/", view=user_sign_view, name="register"),
    path("~update/", view=user_update_view, name="update"),
    path("detailss/", view=user_list_view, name="userx_detail"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
