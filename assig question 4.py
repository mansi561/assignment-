from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from keycloak import KeycloakOpenID
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from keycloak.decorators import keycloak_protect
class KeycloakGraphQLView(GraphQLView):
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    @method_decorator(keycloak_protect(realm_name=settings.KEYCLOAK_REALM,
                                       resource_name=settings.KEYCLOAK_CLIENT_ID,
                                       scopes=['openid'],
                                       roles=['admin']))
    def dispatch(self, request, *args, **kwargs):
        token = request.session.get('oidc_access_token')
        keycloak_openid = KeycloakOpenID(server_url=settings.KEYCLOAK_SERVER_URL,
                                         client_id=settings.KEYCLOAK_CLIENT_ID,
                                         client_secret_key=settings.KEYCLOAK_CLIENT_SECRET,
                                         realm_name=settings.KEYCLOAK_REALM)
        userinfo = keycloak_openid.userinfo(token)
        return super().dispatch(request, user=userinfo, *args, **kwargs)