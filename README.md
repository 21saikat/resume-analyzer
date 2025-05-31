# 🧠 AI Resume Analyzer

An intelligent Resume Analyzer app built using **Azure OpenAI**, **Python**, and **Streamlit**. It gives expert feedback on resumes using GPT-35-Turbo and is deployed on a secure **Azure Linux VM**.

---

## 🚀 Live on Azure VM

🔗 Access: `http://<Your_VM_Public_IP>:8501`

> Replace `<Your_VM_Public_IP>` with your VM's actual public IP address.

---

## 📌 Project Features

- Analyze resumes using Azure OpenAI’s GPT-3.5-Turbo
- Simple and responsive web interface built with Streamlit
- Hosted on a secure Ubuntu VM (UFW-configured)
- Terminal-first deployment using Azure CLI and SSH
- Lightweight and fast — ideal for quick evaluations

---

## 🔧 Tech Stack

- **Azure**: Linux VM, OpenAI Service
- **Azure OpenAI**: GPT-35-Turbo deployment
- **Python**: Resume parsing and analysis logic
- **Streamlit**: Interactive browser UI
- **UFW**: Secure access on port 8501
- **Git & GitHub**: Version control and collaboration

---

## 📂 Project Structure

resume-analyzer/
├── app.py # Streamlit web UI
├── analyze_resume.py # GPT-based resume analysis logic
├── requirements.txt # Python package dependencies
├── .gitignore # Files to ignore in Git
└── README.md # Project documentation





---

## 🧠 How It Works

1. User pastes their resume content into the web app.
2. The app sends the content to GPT-3.5 Turbo via Azure OpenAI.
3. GPT returns detailed feedback and suggestions.
4. Feedback is displayed instantly in the browser.

---

## 💻 Local Setup

```bash
# Clone the repository
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer

# Create and activate a virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run the application
streamlit run app.py




 Azure OpenAI Setup
In analyze_resume.py, replace the placeholders below with your actual Azure OpenAI credentials:

client = AzureOpenAI(
    api_key="your-api-key",
    api_version="2024-05-01-preview",
    azure_endpoint="your-endpoint"
)





👨‍💻 Author
Ibne Sabid Saikat
💼 Azure Cloud Engineer | Python Developer | Microsoft Learn Student Ambassador
🔗 LinkedIn
