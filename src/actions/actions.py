# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import logging
from typing import Any, Text, Dict, List
import requests

import json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

HOST = "http://rocketchat:3000"
PATH = "/api/v1/login"
ADMIN_NAME = "jeffi1"
PASS = "tst123"
BOT_USER = "rocket.agent"

logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


class ActionOverflow(Action):
    def name(self) -> Text:
        return "actions_overflow"

    @classmethod
    def get_authentication_token(cls, user, pw):
        login_data = {"username": user, "password": pw}
        response = requests.post(HOST + PATH, data=login_data)

        if response.json()["status"] == "success":
            logger.info(f"Login succeed | Header = {user}")

            authtoken = response.json()["data"]["authToken"]
            userid = response.json()["data"]["userId"]
            user_header = {
                "X-Auth-Token": authtoken,
                "X-User-Id": userid,
                "Content-Type": "application/json"
            }

            return user_header
        else:
            logger.error(f"Login failed | {response}") 


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_admin_header = self.get_authentication_token(ADMIN_NAME, PASS)

        tst = requests.post(HOST+'/api/v1/livechat/room.forward', json={
            "roomId": tracker.sender_id,
            "userId": "SATL3qmygdTiuFbLJ"
        }, headers=user_admin_header)

        logger.info(tst.content)

        
        return []