from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

#This just for test change token by bearer not using at all in this project
class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'
