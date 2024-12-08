from fastapi import FastAPI
from pydantic import BaseModel
from transformers import LlamaForCausalLM, LlamaTokenizer

# Carga el modelo Llama3 y el tokenizador
model_name = "meta-llama/Llama-3.2"  # Nombre del modelo Llama 3 (puede variar dependiendo de la versión)
model = LlamaForCausalLM.from_pretrained(model_name)
tokenizer = LlamaTokenizer.from_pretrained(model_name)

app = FastAPI()

class CV(BaseModel):
    name: str
    skills: list

class JobOffer(BaseModel):
    title: str
    description: str
    skills_required: list

@app.post("/generate_cover_letter")
async def generate_cover_letter(cv: CV, offer: JobOffer):
    # Crea el prompt que se usará como entrada para el modelo Llama3
    prompt = f"Create a cover letter for {cv.name} applying to the position of {offer.title}. The candidate's skills are {cv.skills}."
    
    # Tokeniza el prompt para el modelo Llama3
    inputs = tokenizer(prompt, return_tensors="pt")

    # Genera la respuesta del modelo Llama3
    outputs = model.generate(inputs['input_ids'], max_length=200)

    # Decodifica la respuesta generada en texto
    cover_letter = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {"cover_letter": cover_letter.strip()}
