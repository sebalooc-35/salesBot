from fastapi import FastAPI, File, UploadFile
import openai
import os

app = FastAPI()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Use environment variables for security

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint to receive the uploaded file and process it with ChatGPT.
    """
    # Read the uploaded file
    file_content = await file.read()

    # Call the OpenAI API with the file content
    try:
        # Example of a call to ChatGPT for parsing logic
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a data extraction assistant."},
                {"role": "user", "content": f"Parse the following file content and generate SQL queries:\n{file_content.decode('utf-8')}"}
            ]
        )
        sql_queries = response['choices'][0]['message']['content']
        return {"sql_queries": sql_queries}

    except Exception as e:
        return {"error": str(e)}
