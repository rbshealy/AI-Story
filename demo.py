from PIL import Image
from gradio_client import Client, handle_file

access_token = "Your Access Token Here"

client = Client("deepseek-ai/Janus-Pro-7B", hf_token = access_token)
result1 = client.predict(
		prompt="Gamer revolution takes over the world",
		seed=123456,
		guidance=5,
		api_name="/generate_image"
)

pr = client.predict(
		image=handle_file(result1[0]['image']),
		question="Use a storytelling tone to narrate what is going on in the image, but keep it pretty short. Then, make up something that would happen next in this context",
		seed=42,
		top_p=0.95,
		temperature=0.1,
		api_name="/multimodal_understanding"
)

im = Image.open(result1[0]['image'])
im.show()

print(pr)

result2 = client.predict(
		prompt=pr,
		seed=123456,
		guidance=5,
		api_name="/generate_image"
)

im2 = Image.open(result2[0]['image'])
im2.show()

#for res in result1:
	#test = Image.open(res['image'])
	#test.show()
