# Diaeta - A Virtual Dietician Chatbot
Lightweight dietary chatbot powered by GPT-2 Small fine-tuned on Q&A style prompts using NLP methodologies.

## React + Vite
This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.  
Currently, two official plugins are available:
- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration
If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.

## Team name: The MahriJustinLucasTrio
- [Mahri Yalkapova](https://github.com/MahriYalkapova)
- [Justin Le](https://github.com/aujustin14)
- [Lucas Jeong](https://github.com/ljeong072)

## Introduction
**Use Case**: Dietiary chatbot to help users obtain a dietary plan, or advice with regards to nutrition.  
**Purpose**: Streamline the process of making a meal plan making it much more efficient and convenient.  
**Target Users**: Students, remote workers, individuals dealing with stress or loneliness.

## Problem Statement & Objective
Many individuals struggle to maintain a healthy diet which is derived from a myriad of factors such as a lack of nutritional education, motivation, or restricted access to dietary support. Nutritional resources or guidelines are widely available yet are generic without discretion for an individual person which contributes to the problem. This chatbot is designed to remove the gap between dietary support and the average person seeking to improve their health.

## Model Selection & Justification
**Model Chosen**: GPT-2 Small

**Why GPT-2 Small?**
- Lightweight architecture with only 124M parameters 
- Fast training, fine-tuning, and deployment
- Resource-efficient, low computational costs

## Dataset & Fine-Tuning Strategy
**Datasets**: 
[Augmented_Meal_Planner_data](https://huggingface.co/datasets/sridhar52/Augmented_Meal_Planner_data) (4,500 Q&A style prompts)
[Nutritional-LLama](https://huggingface.co/datasets/Tom158/Nutritional-LLama) (1,490 Q & A style prompts)

**Preprocessing Steps**:
- Adjust the columns and concatenate them to create one large dataset
- Tokenized using pre-trained GPT-2 Small

**Training Details**:
- Epochs: 10 (with early stopping)
- Batch size: 16
- Learning Rate: 5e-5
- Platform: Jupyter Notebook
- Hardware: GPU - RTX 3060 Ti

**Challenges**:
- Limited model capacity
- Data limitations
- Insufficient dataset diversity
- Generic assumptions
- Avoiding generic responses
- Balancing empathy and diversity

## System Architecture
![System Architecture](https://github.com/user-attachments/assets/327a25a7-9b76-412f-aeec-68e4f6f25b24)

**Components**:
- User input → Web UI (Vite + React)
- Backend → GPT-2 Small via Hugging Face
- Output → Contextual nutrition response

## Run locally:  
npm install node  
pip install flask  

## Run simultaneously:  
python chat_server.py  
npm run dev

## Live Demo
Watch the demo: [https://github.com/user-attachments/assets/1b8105f2-7f15-45f1-9331-aeda77568c3a]
