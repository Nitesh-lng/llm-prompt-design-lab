
# 🧪 LLM Prompt Design Lab

A practical project focused on designing and using prompts with large language models (LLMs). Built with LangChain and Groq's LLaMA 4 Scout model, this project showcases how to structure, template, and execute prompts through CLI and Streamlit web apps.

## 🧠 Core Highlights

- 🧾 Prompt engineering using LangChain's `PromptTemplate`
- 🧠 Dynamic prompt execution using Groq-hosted LLaMA-4-Scout-17B
- 💡 Template-driven summarization for research papers
- 🌐 Streamlit-based UI for interactive experimentation
- 💬 CLI chatbot to simulate real-time prompt responses

## 🛠️ Technologies Used

- `LangChain`
- `Groq`
- `Streamlit`
- `python-dotenv`
- `pyarrow`
- `langchain_core`

## 📁 File Structure

```
.
├── chatbot.py              # CLI chatbot using prompt chain
├── prompt.py               # Streamlit web UI with prompt inputs
├── prompt_generator.py     # LangChain PromptTemplate logic
├── requirements.txt
├── template.json           # Saved LangChain prompt template
└── .env                    # Contains your GROQ_API_KEY
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/llm-prompt-design-lab.git
cd llm-prompt-design-lab
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your API Key

Create a `.env` file with your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

## 💬 Run CLI Chatbot

```bash
python chatbot.py
```

## 🌐 Launch Streamlit Web App

```bash
streamlit run prompt.py
```

## 📌 Example Prompt Use Case

- Title: "GPT-3: Language Models are Few-Shot Learners"
- Style: Technical
- Length: Medium  
- Output: Summarized explanation with equations, analogies, and code (if present).

## 🏷️ Tags

`Prompt Engineering`, `LLM`, `LangChain`, `Groq`, `LLaMA`, `Streamlit`, `AI Tools`, `Research Summarization`

## 👨‍💻 Author

Nitesh Kumar  
[LinkedIn](https://www.linkedin.com/in/your-profile) • [GitHub](https://github.com/your-username)
