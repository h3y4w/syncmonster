from pydrive.auth import GoogleAuth
from dropbox import DropboxOAuth2FlowNoRedirect

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse


class ConnectDropbox (Resource):
    APP_KEY = 'bn8ub3zq0ytazro'
    APP_SECRET = 'xbepfvaz1rzudcg'
    def get(self):
        auth_flow = DropboxOAuth2FlowNoRedirect(self.APP_KEY, self.APP_SECRET)
        return(auth_flow.start())
    
    @staticmethod
    def auth(auth_code):
        APP_KEY = 'bn8ub3zq0ytazro'
        APP_SECRET = 'xbepfvaz1rzudcg'
        auth_flow = DropboxOAuth2FlowNoRedirect(self.APP_KEY, self.APP_SECRET)
        token, user_id = auth_flow.finish(auth_code)
        return token


class ConnectGoogleDrive (Resource):
    def get(self):
        gauth = GoogleAuth()
        return  gauth.GetAuthUrl()

    @staticmethod
    def auth(token):
        gauth = GoogleAuth()
        return (gauth.Auth(token))

