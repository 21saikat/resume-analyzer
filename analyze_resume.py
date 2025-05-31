import openai
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="your-api-key",
    api_version="2024-05-01-preview",
    azure_endpoint="your-endpoint"
)

deployment_name = "resume-analyzer"

def analyze_resume(resume_text):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a professional career advisor analyzing resumes."},
            {"role": "user", "content": f"Analyze this resume:\n\n{resume_text}"}
        ]
    )
    return response.choices[0].message.content
