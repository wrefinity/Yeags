from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("project/", TemplateView.as_view(template_name="pages/project.html"), name="project"),
    path("billing/", TemplateView.as_view(template_name="pages/billing.html"), name="billing"),
    path("components/", TemplateView.as_view(template_name="pages/components/compo.html"), name="components"),
    path("modals/", TemplateView.as_view(template_name="pages/components/modals.html"), name="modals"),
    path("chats/", TemplateView.as_view(template_name="pages/components/chats.html"), name="chats"),
    path("subscriptions/", TemplateView.as_view(template_name="pages/components/subscriptions.html"), name="subscriptions"),
    path("keys/", TemplateView.as_view(template_name="pages/api_key.html"), name="api_keys"),
    path("activity/", TemplateView.as_view(template_name="pages/User/activity.html"), name="activity"),




    path("signin/", TemplateView.as_view(template_name="pages/auth/sign-in.html"), name="signing"),
    path("signup/", TemplateView.as_view(template_name="pages/auth/sign-up.html"), name="signup"),
    path("reset-password/", TemplateView.as_view(template_name="pages/auth/reset_password.html"), name="reset_password"),
    path("new-password/", TemplateView.as_view(template_name="pages/auth/new_password.html"), name="new_password"),
    path("two-factor/", TemplateView.as_view(template_name="pages/auth/two_factor.html"), name="two_factor"),

    # projects routes
    path("project/", TemplateView.as_view(template_name="pages/dashboards/project.html"), name="project"),
    path("project/detail", TemplateView.as_view(template_name="pages/Project/project.html"), name="project_details"),
    path("project/my_project", TemplateView.as_view(template_name="pages/Project/my_project.html"), name="my_project"),
    path("project/project_targets", TemplateView.as_view(template_name="pages/Project/project_target.html"), name="project_targets"),
    path("project/budget/add", TemplateView.as_view(template_name="pages/Project/project_budget.html"), name="project_budget_add"),
    path("project/users", TemplateView.as_view(template_name="pages/User/user_list.html"), name="project_users"),
    # billing
    path("billing/", TemplateView.as_view(template_name="pages/Billing/billing.html"), name="billing"),
    path("keys/", TemplateView.as_view(template_name="pages/api_keys.html"), name="keys"),
    path("dashboard/", TemplateView.as_view(template_name="pages/dashboards/index.html"), name="dashboard"),
    # Courses
    path("courses/", TemplateView.as_view(template_name="pages/dashboards/courses.html"), name="courses_dashboard"),
    # Marketting
    path("marketing/", TemplateView.as_view(template_name="pages/dashboards/marketing.html"), name="marketing_dashboard"),
    # Calls
    path("calls/", TemplateView.as_view(template_name="pages/dashboards/call_center.html"), name="call_center_dashboard"),
    # POS
    path("pos/", TemplateView.as_view(template_name="pages/dashboards/pos.html"), name="pos_dashboard"),
    # ecommerce
    path("ecommerce/", TemplateView.as_view(template_name="pages/dashboards/ecommerce.html"), name="ecommerce_dashboard"),
    path("ecommerce/products", TemplateView.as_view(template_name="pages/ecommerce/product_list.html"), name="products"),
    path("ecommerce/products/add", TemplateView.as_view(template_name="pages/ecommerce/add_product.html"), name="products_add"),
    path("ecommerce/products/edit", TemplateView.as_view(template_name="pages/ecommerce/edit_product.html"), name="products_edit"),
    path("ecommerce/products/views", TemplateView.as_view(template_name="pages/ecommerce/product_viewed.html"), name="products_views"),
    path("ecommerce/categories", TemplateView.as_view(template_name="pages/ecommerce/category_list.html"), name="categories"),
    path("ecommerce/categories/add", TemplateView.as_view(template_name="pages/ecommerce/add_category.html"), name="categories_add"),
    path("ecommerce/categories/edit", TemplateView.as_view(template_name="pages/ecommerce/edit_category.html"), name="categories_edit"),
    path("ecommerce/orders", TemplateView.as_view(template_name="pages/ecommerce/order_list.html"), name="orders"),
    path("ecommerce/orders/add", TemplateView.as_view(template_name="pages/ecommerce/add_order.html"), name="orders_add"),
    path("ecommerce/orders/edit", TemplateView.as_view(template_name="pages/ecommerce/add_order.html"), name="orders_edit"),
    path("ecommerce/orders/details", TemplateView.as_view(template_name="pages/ecommerce/order_details.html"), name="orders_details"),

    path("userx/", TemplateView.as_view(template_name="pages/User/user_list.html"), name="userx"),
    path("userx/all", TemplateView.as_view(template_name="pages/User/users.html"), name="users_all"),
    path("userx/profile", TemplateView.as_view(template_name="pages/User/user_detail.html"), name="users_profile"),

    path("about/", TemplateView.as_view(template_name="pages/User/about.html"), name="about"),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("yeager_ai.users.urls", namespace="users")),
    # account authentications
    path("accounts/", include("allauth.urls")),
    # world path
    # path("accounts/", include("yeager_ai.world.urls")),
    # stripe path
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    path('', include("referrals.urls", namespace="referrals")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
