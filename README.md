# 📸 PhotoPilot AI

### AI-Powered Photography Analysis and Creative Workflow Assistant

PhotoPilot AI is an AI-powered photography workspace that helps photographers analyze their images and make creative decisions throughout their editing and publishing workflow.

The application uses **Google Gemini**, specialized AI agents, custom prompts, structured responses, and a personalized photography knowledge base to provide image-specific assistance.

## ✨ What PhotoPilot AI Can Do

### 📷 Image Analysis

Upload a photograph and receive AI-powered feedback based on the actual image.

The analysis focuses on areas such as:

- Composition
- Lighting
- Colors
- Technical quality
- Visual impact
- Strengths
- Areas for improvement

---

### 🎠 Carousel Planner

Upload multiple photographs and analyze each image individually.

Features include:

- Multiple image upload
- Individual analysis for every image
- Real progress tracking
- Clean, organized results

---

### 🎨 Lightroom Editor

Generate custom **Adobe Lightroom Classic** editing recommendations specifically for an uploaded photograph.

Recommendations can include:

- Basic adjustments
- White balance
- Tone curve
- HSL adjustments
- Color grading
- Sharpening and noise reduction
- Lens corrections
- Effects
- Calibration
- Selective masking

Each section includes fixed values and a concise explanation of why the adjustments were recommended.

---

### 📝 Caption Generator

Generate captions based on the photograph's:

- Subject
- Mood
- Atmosphere
- Visual story
- Overall aesthetic

---

### 🎵 Music Suggestions

Receive music recommendations that match the visual mood and atmosphere of a photograph.

The AI considers factors such as:

- Emotion
- Energy
- Subject
- Atmosphere
- Visual aesthetic

---

### ⚙️ Settings

The Settings page allows you to:

- View the currently configured AI model
- Check whether the Gemini API key is detected
- Test the Gemini connection
- View available application features
- Clear generated session results

---

# 🏗️ Project Architecture

PhotoPilot AI follows a modular architecture. Each major photography task is handled by a dedicated AI agent.

```text
PhotoPilot AI
│
├── Streamlit Interface
│
├── AI Agents
│   ├── Image Analyzer
│   ├── Carousel Agent
│   ├── Lightroom Agent
│   ├── Caption Agent
│   └── Music Agent
│
├── Services
│   ├── Gemini API Service
│   ├── Knowledge Service
│   └── Prompt Loader
│
├── Custom Prompts
│
├── Photography Knowledge Base
│
└── Structured Response Schemas
```

---

# 📁 Project Structure

```text
PhotoPilot AI
│
├── agents/
│   ├── caption_agent.py
│   ├── carousel_agent.py
│   ├── image_analyzer.py
│   ├── lightroom_agent.py
│   └── music_agent.py
│
├── knowledge/
│   ├── editing_style.md
│   ├── instagram_style.md
│   └── photographer_profile.md
│
├── pages/
│   ├── 1_Image_Analysis.py
│   ├── 2_Carousel_Planner.py
│   ├── 3_Lightroom_Editor.py
│   ├── 4_Caption_Generator.py
│   ├── 5_Music_Suggestions.py
│   └── 6_Settings.py
│
├── prompts/
│   ├── caption_generation.txt
│   ├── image_analysis.txt
│   ├── lightroom_recommendation.txt
│   └── music_suggestions.txt
│
├── schemas/
│   ├── image_analysis_schema.py
│   └── lightroom_schema.py
│
├── services/
│   ├── gemini_service.py
│   ├── knowledge_service.py
│   └── prompt_loader.py
│
├── utils/
│   └── display.py
│
├── config.py
├── PhotoPilot_AI.py
├── requirements.txt
├── list_models.py
├── test.py
└── README.md
```

---

# 🤖 AI Agents

| Agent | Purpose |
|---|---|
| `image_analyzer.py` | Analyzes individual photographs |
| `carousel_agent.py` | Analyzes multiple images for carousel workflows |
| `lightroom_agent.py` | Generates Lightroom Classic editing recommendations |
| `caption_agent.py` | Generates captions based on an uploaded photograph |
| `music_agent.py` | Recommends music matching an image's mood and aesthetic |

---

# 🧠 Knowledge and Prompt System

PhotoPilot AI separates AI instructions and photography knowledge from the main application code.

### Custom Prompts

Each AI feature uses its own dedicated prompt:

```text
prompts/
├── image_analysis.txt
├── lightroom_recommendation.txt
├── caption_generation.txt
└── music_suggestions.txt
```

### Photography Knowledge Base

The AI can also use additional photography context from:

```text
knowledge/
├── editing_style.md
├── instagram_style.md
└── photographer_profile.md
```

This structure makes the system easier to maintain and allows AI behavior to be improved without rewriting the main application logic.

---

# 🧱 Structured Responses

The project includes schemas for structured AI output:

```text
schemas/
├── image_analysis_schema.py
└── lightroom_schema.py
```

Structured responses help the application convert AI output into organized sections and tables, particularly for detailed photography analysis and Lightroom editing recommendations.

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Google Gemini | AI and image understanding |
| Google Gen AI SDK | Gemini API integration |
| Pillow | Image processing |
| python-dotenv | Environment variable management |

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/dayyankhan-codes/Instagram-AI-Agent.git
```

## 2. Open the project

```bash
cd Instagram-AI-Agent
```

## 3. Create a virtual environment

```bash
python -m venv venv
```

## 4. Activate the environment

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Gemini API Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

> **Important:** Never upload your `.env` file or API key to GitHub.

The application loads the API key using `python-dotenv`.

---

# ▶️ Running the Application

From the project directory, run:

```bash
python -m streamlit run PhotoPilot_AI.py
```

The application will start locally and open in your browser.

---

# ⚙️ Model Configuration

The Gemini model is configured centrally in:

```text
config.py
```

This makes it possible to change the AI model without modifying every individual agent.

The currently configured model can also be viewed from the **Settings** page.

---

# 📊 Current Features

| Feature | Status |
|---|---|
| 📷 Image Analysis | ✅ Implemented |
| 🎠 Carousel Planner | ✅ Implemented |
| 🎨 Lightroom Editor | ✅ Implemented |
| 📝 Caption Generator | ✅ Implemented |
| 🎵 Music Suggestions | ✅ Implemented |
| ⚙️ Settings | ✅ Implemented |
| 🧠 Photography Knowledge Base | ✅ Implemented |
| 🤖 Gemini Integration | ✅ Implemented |

---

# 🔮 Future Improvements

Possible future development includes:

- Advanced carousel image sequencing
- AI-powered cover image selection
- Image ranking and comparison
- Saving generated results
- Exporting Lightroom recommendations
- User-selectable photography styles
- Persistent user preferences
- Improved multi-agent collaboration
- Public web deployment

---

# 👨‍💻 Author

**Muhammad Dayyan Khan**

Photography · Artificial Intelligence · Python · Creative Technology

GitHub: [@dayyankhan-codes](https://github.com/dayyankhan-codes)

---

<div align="center">

# 📸 PhotoPilot AI

### Your AI-Powered Photography Workspace

**Analyze · Edit · Create · Share**

Built with Python, Streamlit, and Google Gemini.

</div>