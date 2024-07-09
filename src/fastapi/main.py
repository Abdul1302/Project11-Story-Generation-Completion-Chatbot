from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from src.fastapi.generation import generate, complete
from fastapi.middleware.cors import CORSMiddleware

#Define api
app = FastAPI()   


@app.get('/')
async def check():
    return 'hello'

origins = [
    "http://localhost:3000",  #This allows requests from a ui
    "http://127.0.0.1:3000",  # This allows requests from the loopback address 
]

#add the CORSMiddleware to the FastAPI application.
#(CORSMiddleware is a piece of software that acts as an intermediary between ui and the FastAPI backend. )
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  #specifies the list of allowed origins for CORS requests.
    allow_credentials=True, #CORS requests to include cookies, which is necessary for authenticated requests
    allow_methods=["*"],    #allows all HTTP methods (GET, POST, PUT, DELETE, etc.) for CORS requests.
    allow_headers=["*"],    # allows all headers in CORS requests 
)

#Carry all the parameters from the ui and generate request
class GenerateRequest(BaseModel):
    topic: str
    length: str
    temperature: float = 0.7
    genre: Optional[str] = None
    narrative_perspective: Optional[str] = None
    character_name: Optional[str] = None
    character_description: Optional[str] = None
    setting_description: Optional[str] = None

#Carry all the parameters from the ui and generate request
class CompleteRequest(BaseModel):
    partial_story: str
    length: str
    temperature: float = 0.7
    genre: Optional[str] = None
    narrative_perspective: Optional[str] = None
    character_name: Optional[str] = None
    character_description: Optional[str] = None
    setting_description: Optional[str] = None

#Pass the params from ui to Generate function in generation.py and return their response
@app.post("/generate")
def generate_story(request: GenerateRequest):
    response = generate(
        topic=request.topic,
        length=request.length,
        temperature=request.temperature,
        genre=request.genre,
        narrative_perspective=request.narrative_perspective,
        character_name=request.character_name,
        character_description=request.character_description,
        setting_description=request.setting_description
    )
    return {"story": response}

#Pass the params from ui to complete function in generation.py and return their response
@app.post("/complete")
def complete_story(request: CompleteRequest):
    response = complete(
        partial_story=request.topic,
        length=request.length,
        temperature=request.temperature,
        genre=request.genre,
        narrative_perspective=request.narrative_perspective,
        character_name=request.character_name,
        character_description=request.character_description,
        setting_description=request.setting_description
    )
    return {"completed_story": response}
