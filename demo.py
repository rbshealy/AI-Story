from gradio_client import Client

client = Client("deepseek-ai/Janus-1.3B")
result = client.predict(
		prompt="Hello!!",
		seed=12345,
		guidance=5,
		api_name="/generate_image"
)
print(result)