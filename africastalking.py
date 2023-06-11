import africastalking

class AfricasTalking:
    def __init__(self):
        # Initialize SDK
        username = "awssms" 
        api_key = "394957400d15920d7c16a7256387bec89219e3d78e7a40379378916367c7df1f"
        self.africastalking = africastalking.initialize(username, api_key)
