# TalentScout AI 🤖

An intelligent AI-powered talent screening and technical interview assistant built with Streamlit. TalentScout AI automates the initial screening process by collecting candidate information and conducting technical interviews based on their tech stack.

## 🚀 Features

- **Automated Candidate Screening**: Collects essential candidate information (name, email, phone, experience, position, location)
- **Smart Tech Stack Analysis**: Parses and validates candidate's technology stack
- **Dynamic Technical Interviews**: Generates personalized technical questions based on the candidate's tech stack
- **Interactive Chat Interface**: User-friendly conversational interface built with Streamlit
- **Data Validation**: Comprehensive validation for email, phone, and experience inputs
- **Session Management**: Maintains conversation state and candidate information throughout the interview process

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ManivardhanDonuri/TalentScout-Al.git
   cd TalentScout-Al
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

### Local Development

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The application will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

3. **Start the interview process**
   - Enter the candidate's name when prompted
   - Follow the guided conversation to collect candidate information
   - The AI will automatically generate technical questions based on the candidate's tech stack

## 🚀 Deployment on Render

### Step-by-Step Render Deployment

1. **Sign up for Render**
   - Go to [render.com](https://render.com)
   - Sign up with your GitHub account

2. **Create a New Web Service**
   - Click "New +" button
   - Select "Web Service"
   - Connect your GitHub repository: `ManivardhanDonuri/TalentScout-Al`

3. **Configure the Service**
   - **Name**: `talent-scout-ai` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

4. **Deploy**
   - Click "Create Web Service"
   - Wait for the build process (usually 2-3 minutes)

### Your App Will Be Live At:
`https://talent-scout-ai.onrender.com`

## 📁 Project Structure

```
TalentScout-Al/
├── app.py                 # Main application entry point
├── conversation_handler.py # Core conversation logic and interview flow
├── ui_components.py       # Streamlit UI components and styling
├── config.py             # Configuration constants and messages
├── utils.py              # Utility functions and validators
├── requirements.txt      # Python dependencies
├── .streamlit/          # Streamlit configuration
│   └── config.toml     # Deployment settings
└── README.md            # This file
```

## 🔧 Configuration

The application uses several configuration files:

- **`config.py`**: Contains conversation stages, error messages, and success messages
- **`utils.py`**: Validation functions for email, phone, and experience inputs
- **`ui_components.py`**: Streamlit UI components and styling
- **`.streamlit/config.toml`**: Streamlit deployment configuration

## 🎨 Features in Detail

### Candidate Information Collection
- **Name**: Basic name validation
- **Email**: Email format validation
- **Phone**: Phone number format validation
- **Experience**: Years of experience validation
- **Position**: Desired job position
- **Location**: Geographic location
- **Tech Stack**: Technology stack parsing and validation

### Technical Interview Process
- Automatically generates 5 technical questions per technology mentioned
- Questions cover:
  - Key features and capabilities
  - Real-world application scenarios
  - Best practices
  - Troubleshooting approaches
  - Latest trends and updates

### Conversation Flow
1. **Greeting Stage**: Collect candidate's name
2. **Information Collection**: Gather all candidate details
3. **Question Generation**: Create personalized technical questions
4. **Technical Interview**: Conduct the interview
5. **Completion**: Provide summary and next steps

## 🛠️ Render Deployment Benefits

- ✅ **Free Tier Available**: Deploy for free with Render's free tier
- ✅ **Automatic HTTPS**: SSL certificates included
- ✅ **Custom Domains**: Add your own domain name
- ✅ **Auto-Deploy**: Automatic deployments from GitHub
- ✅ **Scalable**: Easy to scale as your app grows
- ✅ **Monitoring**: Built-in monitoring and logs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Manivardhan Donuri**
- GitHub: [@ManivardhanDonuri](https://github.com/ManivardhanDonuri)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Deployed on [Render](https://render.com) for reliable hosting
- Designed for modern talent acquisition workflows
- Inspired by the need for efficient technical screening processes

---

⭐ **Star this repository if you find it helpful!** 