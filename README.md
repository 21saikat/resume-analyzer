# 🧠 AI Resume Analyzer

An intelligent Resume Analyzer app built using **Azure OpenAI**, **Python**, and **Streamlit**. It gives expert feedback on resumes using GPT-35-Turbo and is deployed on a secure **Azure Linux VM**.

## 🚀 Live on Azure VM

🔗 Access: `http://<Your_VM_Public_IP>:8501`

> Replace `<Your_VM_Public_IP>` with your VM's actual IP.

---

## 📌 Project Features

- Analyze resumes with GPT-3.5-Turbo from Azure OpenAI
- Beautiful web interface built with Streamlit
- Deployed on Ubuntu VM with secure access (UFW)
- Uses CLI tools (Azure CLI, SSH, pip, git)

---

## 🔧 Tech Stack

- **Azure**: Linux VM, OpenAI Service
- **Azure OpenAI**: GPT-35-Turbo deployment
- **Python**: Resume analysis logic
- **Streamlit**: Interactive web UI
- **UFW**: Port management
- **Git**: Version control & GitHub integration

---

## 📂 Project Structure
resume-analyzer/
│
├── app.py # Streamlit frontend
├── analyze_resume.py # AI analysis logic with Azure OpenAI
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files
└── README.md # This file




---

## 🧠 How It Works

1. User pastes resume text into the app.
2. GPT-3.5 analyzes and gives structured feedback.
3. Output is shown directly in the browser.

---

## 💻 Local Setup

```bash
# Clone repo
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer

# Create & activate virtual environment
python3 -m venv myenv
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py



Azure OpenAI Setup (Replace in analyze_resume.py)
client = AzureOpenAI(
    api_key="your-api-key",
    api_version="2024-05-01-preview",
    azure_endpoint="your-endpoint"
)



Author
👨‍💻 Ibne Sabid Saikat
💼 Azure Cloud Engineer | Python Developer | Microsoft Learn Student Ambassador
🔗 LinkedIn



