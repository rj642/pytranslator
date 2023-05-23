from pydantic import BaseModel

class UserInput(BaseModel):
    text = ""
    from_lang = "en" 
    to_lang = "" 

class UserOutput(BaseModel):
    output_text = ""