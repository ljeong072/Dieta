# Dieta (virtual dietician chatbot)
Lightweight chatbot powered by gpt-2 small fine-tuned on Q&A style prompts using NLP methodologies. D
---

## Team name: TheMahriJustinLucas Trio
- Justin Le
- Mahri Yalkapova
- Lucas Jeong
---

## Introduction

**Use Case**: Dietiary chatbot to help users obtain a dietary plan, or advice with regards to nutrition.  
**Purpose**: Streamline the process of making a meal plan making it much more efficient and convenient.
**Target Users**: Students, remote workers, individuals dealing with stress or loneliness.

---
## Problem Statement & Objective
Many individuals struggle to maintain a healthy diet which is derived from a myriad of factors such as a lack of nutritional education, motivation, or restricted access to dietary support. Nutritional resources or guidelines are widely available yet are generic without discretion for an individual person which contributes to the problem. This chatbot is designed to remove the gap between dietary support and the average person seeking to improve their health.
---

## Model Selection & Justification
**Model Chosen**: GPT2-Small

**Why GPT-2 Small?**
- Lightweight and short training time
- Good performance on conversation tasks

---
## Dataset & Fine-Tuning Strategy

**Dataset**: 
[Augmented_Meal_Planner_data](https://huggingface.co/datasets/sridhar52/Augmented_Meal_Planner_data) (4,500 Q&A style prompts)
[Nutritional-LLama](https://huggingface.co/datasets/Tom158/Nutritional-LLama)(1,490 Q & A style prompts)

**Preprocessing Steps**:
- Adjust the columns and concatenate them to create one large dataset
- Tokenized using pre-trained gpt-2 small

**Training Details**:
- Epochs: 10
- batch size: 16
- Learning Rate: 5e-5
- Platform: Jupyter Notebook (GPU RTX 3060)

**Challenges**:
- Avoiding generic responses
- Balancing empathy and diversity

---
## System Architecture
![System Architecture](Picture)

**Components**:
- User input → Web UI (HTML/CSS + Flask)
- Backend → NLP model via Hugging Face
- Output → Emotionally aware response
---

## Run locally:
npm install node  
pip install flask  

Run simultaneously:  
python chat_server.py  
npm run dev  
---
## Live Demo

Watch the demo: [`demo/demo_video.mp4`](demo/demo_video.mp4)  
