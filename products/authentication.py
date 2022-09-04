from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

#This just for test change token by bearer not using at all in this project
class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'


# in shell 
# from rest_framework.authtoken.models import *  ===> we can import this in this authentication.py and manipulate it as we wont
# Token.objects.all()     ==> this bring all tokens
# token = Token.objects.all().first()
# token.created           ==> show created time
