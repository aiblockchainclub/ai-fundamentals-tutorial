from diffusers import StableDiffusionPipeline

# Load Stable Diffusion pipeline
pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipeline.to("cpu")

# Generate an image
image = pipeline(prompt="A smart man cooking biryani").images[0]
image.save("output.png")
