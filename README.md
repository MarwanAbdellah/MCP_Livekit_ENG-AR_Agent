# MCP connected LiveKit Voice AI Workflow  

This project implements a **LiveKit-powered Voice AI Workflow** in Python. It allows users to **speak directly to the system**, process their input using **Speech-to-Text (STT)**, apply **LLM-based reasoning**, and return responses in **AI-generated speech** using **Text-to-Speech (TTS)**.  

The pipeline is fully integrated with an **MCP (Model Context Protocol) server**, enabling seamless interaction and context-aware responses in **both English and Arabic**.  

---

## 🚀 Features  
- 🎙️ **Speech-to-Text (STT):** Converts spoken input into text.  
- 🧠 **LLM Reasoning:** Processes text input with an AI model for intelligent responses.  
- 🔊 **Text-to-Speech (TTS):** Generates natural speech output in real-time.  
- 🌐 **MCP Integration:** Connects with MCP server for context-aware workflow and data exchange.  
- 🌍 **Bilingual Support:** English and Arabic communication supported.  

---

## 📂 Project Structure  
```  
MCP_Livekit_ENG-AR_Agent/  
│── agent.py          # Main entry point for running the agent  
│── requirements.txt  # Python dependencies  
│── config/           # Configuration files (API keys, environment setup)  
│── utils/            # Helper scripts and utility functions  
│── README.md         # Project documentation  
```  

---

## ⚙️ Installation  

1. **Clone the repository:**  
```bash  
git clone https://github.com/MarwanAbdellah/MCP_Livekit_ENG-AR_Agent.git  
cd MCP_Livekit_ENG-AR_Agent  
```  

2. **Set up a virtual environment (recommended):**  
```bash  
python -m venv venv  
source venv/bin/activate   # Linux/Mac  
venv\Scripts\activate      # Windows  
```  

3. **Install dependencies:**  
```bash  
pip install -r requirements.txt  
```  

4. **Configure environment variables:**  
- Add your **LiveKit API credentials**.  
- Add your **LLM API key** (e.g., OpenAI, Anthropic, or other supported providers).  
- Configure **STT** and **TTS** providers.  

You can create a `.env` file in the project root:  
```env  
LIVEKIT_API_KEY=your_api_key  
LIVEKIT_API_SECRET=your_api_secret  
LLM_API_KEY=your_llm_key  
```  

---

## ▶️ Usage  

Run the agent in console mode:  
```bash  
python agent.py console  
```  

Start a voice session with LiveKit:  
```bash  
python agent.py  
```  

The system will listen to your microphone, process speech in **real-time**, and respond back with **AI-generated audio**.  

---

## 🖇️ MCP Server Integration  

This project integrates with the **MCP server** to handle communication and context sharing.  

Start the MCP server:  
```bash  
python mcp_server.py  
```  

The agent will automatically connect to the server and use it for context-aware AI responses.  

---

## 🌍 Language Support  

- **English** → STT + LLM Reasoning + TTS  
- **Arabic** → STT + LLM Reasoning + TTS  

This allows **bilingual conversations** with the system.  

---

## 📌 Requirements  

- Python **3.9+**  
- LiveKit SDK  
- STT + TTS provider (e.g., OpenAI Whisper, Google STT, ElevenLabs, Coqui TTS)  
- MCP server setup  

Install dependencies via:  
```bash  
pip install -r requirements.txt  
```  

---

## 🛠️ Future Improvements  

- Add support for **more languages**.  
- Implement **customizable voices** for TTS.  
- Extend **MCP workflows** for specialized use cases.  
- Improve **latency** for real-time interaction.  

---

## 🤝 Contributing  

Contributions are welcome! Please fork the repo and submit a PR for any improvements or bug fixes.  

---

## 📜 License  

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  
