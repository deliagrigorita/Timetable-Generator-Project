from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    # def on_start(self):
    #     self.client.post("/auth", {
    #         "username": "deliagrigorita@yahoo.com",
    #         "password": "1234"
    #     })
    
    @task
    def auth (self):
        self.client.get("/auth")
        
    @task
    def index (self):
        self.client.get("/") #index

    @task
    def  add_student (self):
        self.client.get("/add_student")
    
    @task
    def add_resource (self):
        self.client.get("/add_resource")