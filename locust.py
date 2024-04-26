from locust  import HttpUser, task


class HelloWorldUser(HttpUser):

    @task
    def hello_world(self):
        url = 'http://127.0.0.1/api/v1/news/counter/'
        response = self.client.get(url)
        print(response.json())
"""
locust command
locust -f main.py --host http://0.0.0.0:8090
"""