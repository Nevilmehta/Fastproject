import os.path
import markdown
from pydantic import FilePath

def openfile(filename):
    filePath= os.path.join("app/pages/",filename)
    with open(filePath, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    data={
        "text": html
    }
    return data