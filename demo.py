from PIL import Image
from gradio_client import Client

access_token = "your access token here"

client = Client("deepseek-ai/Janus-Pro-7B", hf_token = access_token)
result = client.predict(
		prompt="Hello!!",
		seed=12345,
		guidance=5,
		api_name="/generate_image"
)

for res in result:
	test = Image.open(res['image'])
	test.show()
