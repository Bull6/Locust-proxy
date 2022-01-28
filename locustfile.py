from webbrowser import get
from locust import HttpUser, task
import time
from proxy import main as get_proxy


class HelloWorldUser(HttpUser):

    @task(7)
    def get_landing(self):

        respone = self.client.get(url="/", proxies=get_proxy())
        respone.status_code

    @task(3)
    def get_redirect(self):
        self.client.get(url="/test", proxies=get_proxy())
