import traceback
import requests
import logging
from gempyp.config import DefaultSettings
import logging
import sys


def _getHeaders(bridge_token, user_name):

    return {"Content-Type": "application/json", "bridgeToken": bridge_token, "username": user_name}



def sendSuiteData(payload, bridge_token, user_name, mode="POST"):
    try:
        response = _sendData(payload, DefaultSettings.urls["suiteExec"], bridge_token, user_name, mode)
        if response.status_code == 201:
            logging.info("data uploaded successfully")

    except Exception as e:
        logging.error(traceback.format_exc())

def sendTestcaseData(payload, bridge_token, user_name):
    try:
        response = _sendData(payload, DefaultSettings.urls["testcases"], bridge_token, user_name, method="POST")

        if response.status_code == 201:
            logging.info("data uploaded successfully")

    except Exception as e:
        logging.error(traceback.format_exc())


def _sendData(payload, url, bridge_token, user_name, method="POST"):

    if DefaultSettings.count > 3:
        logging.critical("Incorrect bridge_token/username or APIs are down")
        sys.exit()

    response = requests.request(
        method=method,
        url=url,
        data=payload,
        headers=_getHeaders(bridge_token, user_name),
    )
    if response.status_code != 200 and response.status_code != 201:
        DefaultSettings.count += 1
    logging.info(f"status: {response.status_code}")
    response.raise_for_status()

    return response
