import os
from dotenv import *
from LinkedInClient import *

load_dotenv("environment.env")

client = LinkedInClient(clientId=os.getenv("LinkedIn_clientId"),clientSecret=os.getenv("LinkedIn_clientSecret"))