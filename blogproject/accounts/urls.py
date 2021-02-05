from django.urls import path
from django.contrib.auth import views as auth_views


from .views import CustomUserCreationView, CustomUserLoginView, CustomUserUpdateView, ManageView, MarkAsSpamThreadView, MarkAsSpamCommentView

app_name = 'accounts'

urlpatterns = [
    path('registrar/', CustomUserCreationView, name='register'),
    path('entrar/', CustomUserLoginView.as_view(), name='login'),
    path('sair/', auth_views.LogoutView.as_view(template_name='user/sair/sair.html'), name='logout'),
    path('esqueci-a-senha/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('atualizar/', CustomUserUpdateView.as_view(), name='update'),
    path('gerenciar/', ManageView.as_view(), name='manage'),
    path('gerenciar/thread/<slug>', MarkAsSpamThreadView.as_view(), name='spamThread'),
    path('gerenciar/comentario/<pk>', MarkAsSpamCommentView.as_view(), name='spamComment'),

]
