from email.mime import application
from googletrans import Translator
from fastapi import FastAPI, Request
from src.models.LanguageInput import UserInput, UserOutput
import uvicorn

translator = Translator()

app = FastAPI()

@app.get("/test", response_model=UserOutput)
def translate_now(body: UserInput):
    json_dict = dict(body)
    text = json_dict['text']
    from_lang = json_dict['from_lang']
    to_lang = json_dict['to_lang']
    data = translator.translate(text, to_lang, from_lang)
    user_output = UserOutput(output_text = data.text)
    return user_output


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

app = application