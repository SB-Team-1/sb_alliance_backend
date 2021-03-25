from django.urls import path
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.alliance_views import AllAlliance, Alliance, AllianceDetail
from .views.business_views import AllBusiness, Business, BusinessDetail
from .views.perks_views import AllPerks, Perks, PerksDetail

urlpatterns = [
  # Restful routing
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),

    path('business-create/', Business.as_view(), name='business-create'),
    path('business-edit/:id', BusinessDetail.as_view(), name='business-edit'),
    path('business/', AllBusiness.as_view(), name='business'),
    path('business/:id', BusinessDetail.as_view(), name='business-id'),

    path('alliance-create/', Alliance.as_view(), name='alliance-create'),
    path('alliance-edit/:id', AllianceDetail.as_view(), name='alliance-edit'),
    path('alliance/', AllAlliance.as_view(), name='alliance'),
    path('alliance/:id', AllianceDetail.as_view(), name='alliance-id'),

    path('perks-create/', Perks.as_view(), name='perks-create'),
    path('perks-edit/:id', PerksDetail.as_view(), name='perks-edit'),
    path('perks/', AllPerks.as_view(), name='perks'),
    path('perks/:id', PerksDetail.as_view(), name='perks-id'),
    
]
