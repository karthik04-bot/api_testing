import requests
import logging
import json


class Log:
    def log_module(self, file):
        # Create and configure logger
        logging.basicConfig(filename=file + ".log",
                            format='%(asctime)s %(message)s',
                            filemode='w')

        # Creating an object
        self.logger = logging.getLogger()

        # Setting the threshold of logger to DEBUG
        self.logger.setLevel(logging.DEBUG)
        return self.logger

class API:

    def __init__(self):
        self.logger = Log().log_module(__name__)
        self.session = requests.Session()
        self.session.verify = False

    def get_method(self, api):
        self.logger.info("Get Method for API is {}".format(api))
        response = self.session.get(api)
        self.logger.info("Response: \n {}".format(response))
        return response.json()

    def post_method(self,api,payload):
        self.logger.info("Post Method API is {}.\nThe payload for the same API : {}".format(API, payload))
        response = self.session.post(api, data=json.dumps(payload))
        self.logger.info("Response: \n {}".format(response))
        return response.json()

    # def http_api(self, path, input_data=None, method, timeout=3600):
    #     kwargs = {'data':input_data}
    #     if not isinstance(input_data, dict):
    #         kwargs['headers'] = {'Content-Type': 'application/json'}
    #     self.logger.info(self.session.headers)
    #     self.logger.info("Full URL is {} and data is {}".format(path, input_data))
    #     response = self.session.request(method, path, **kwargs)
    #     self.logger.info("Response code - {}".format(response.status_code))

if __name__ == '__main__':
    pass



