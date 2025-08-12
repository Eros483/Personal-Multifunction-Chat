import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

@st.cache_resource
def load_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float16
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

st.title("Image Generator")
prompt = st.text_input("Enter your prompt:")

if st.button("Generate") and prompt:
    pipe = load_model()
    with st.spinner("Generating..."):
        image = pipe(prompt).images[0]
    st.image(image)