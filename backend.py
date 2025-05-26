from fastapi import FastAPI, File, UploadFile, Form
import uvicorn
import os
from model import process_pdf, generate_answer  # Import from your model file

app = FastAPI()

@app.post("/query")
async def query_pdf(file: UploadFile = File(...), query: str = Form(...)):
    pdf_path = f"/content/{file.filename}"
    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    context = process_pdf(pdf_path)  # Extract text from PDF
    answer = generate_answer(query, context)  # Generate answer

    return {"answer": answer}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
