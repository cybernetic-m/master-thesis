from transformers import AutoModelForVision2Seq, AutoProcessor
from PIL import Image
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu" # Check if GPU is available

processor = AutoProcessor.from_pretrained("openvla/openvla-7b", trust_remote_code=True)
vla = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b", 
    #attn_implementation="flash_attention_2",  # [Optional] Requires `flash_attn`
    torch_dtype=torch.bfloat16, 
    low_cpu_mem_usage=True, 
    trust_remote_code=True
).to(device)
print("OpenVLA loaded successfully in", device)

image = Image.open("image.jpg").convert("RGB")  # Load your image here
prompt = "In: What action should the robot take to take the orange robot?\nOut:."

inputs = processor(prompt, image).to("cuda:0", dtype=torch.bfloat16)
action = vla.predict_action(**inputs, unnorm_key="bridge_orig", do_sample=False)

print("Predicted action:", action)