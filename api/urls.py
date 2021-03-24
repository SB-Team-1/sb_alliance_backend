from django.urls import path
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword, BusinessCreate, BusinessEdit, Business, BusinessId, AllianceCreate, AllianceEdit, Alliance, AllianceId, PerksCreate, PerksEdit, Perks, PerksId

urlpatterns = [
  # Restful routing
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),

    path('business-create/', BusinessCreate.as_view(), name='business-create'),
    path('business-edit/:id', BusinessEdit.as_view(), name='business-edit'),
    path('business/', Business.as_view(), name='business'),
    path('business/:id', BusinessId.as_view(), name='business-id'),

    path('alliance-create/', AllianceCreate.as_view(), name='alliance-create'),
    path('alliance-edit/:id', AllianceEdit.as_view(), name='alliance-edit'),
    path('alliance/', Alliance.as_view(), name='alliance'),
    path('alliance/:id', AllianceId.as_view(), name='alliance-id'),

    path('perks-create/', PerksCreate.as_view(), name='perks-create'),
    path('perks-edit/:id', PerksEdit.as_view(), name='perks-edit'),
    path('perks/', Perks.as_view(), name='perks'),
    path('perks/:id', PerksId.as_view(), name='perks-id'),

    
]
