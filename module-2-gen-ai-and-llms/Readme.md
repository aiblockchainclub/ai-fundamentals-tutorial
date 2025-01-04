## **Module 2: Generative AI and Large Language Models**

### **Project: Build an AI-Powered Chatbot**

**Objective:** Create a chatbot using React and Google Gemini API.

### **Setup Instructions:**

1. Clone this repository:

   ```bash
   git clone https://github.com/aiblockchainclub/ai-fundamentals-tutorial.git
   cd ai-fundamentals-tutorial/module-2-gen-ai-and-llms
   ```

2. Frontend Setup

   ```bash
   cd module-2-gen-ai-and-llms
   cd fronted
   npm i
   npm start
   ```

3. Backend Setup

   ```bash
   cd module-2-gen-ai-and-llms/backend
   bun add ./
   bun run  index.ts
   ```

4. create a .env file and place your gemini api key in the vaiable GEMINI_API_KEY

#### Key Files

- `frontend/src/Chatbot.tsx`: React component for chatbot UI
- `backend/index.ts`: Node.js server handling Gemini API requests
