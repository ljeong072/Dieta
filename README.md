# Diaeta - A Virtual Dietician Chatbot

A lightweight dietary chatbot, powered by GPT-2 Small and trained on Q&A style prompts using NLP methodologies.

## Team name: The MahriJustinLucasTrio

- [Mahri Yalkapova](https://github.com/MahriYalkapova)
- [Justin Le](https://github.com/aujustin14)
- [Lucas Jeong](https://github.com/ljeong072)

## Introduction

- **Use Case**: Dietiary chatbot to help users figure out a diet plan or by providing advice with regards to nutrition.  
- **Purpose**: Streamline the process of making a meal plan, making the process much more efficient and convenient.  
- **Target Users**: People struggling with dieting and nutrition and need help learning more and/or creating a viable meal plan.

## Problem Statement & Objective

Many individuals struggle to maintain a healthy diet due to factors such as limited nutritional education, lack of motivation, or restricted access to personalized dietary support. Although general nutritional guidelines are widely available, they often fail to account for individual needs, making them less effective. This chatbot aims to bridge that gap by providing accessible, personalized support to help users make healthier choices and improve their overall well-being.

## Model Selection & Justification

**Model Chosen**: GPT-2 Small  

**Why GPT-2 Small?**
- Lightweight architecture with only 124M parameters 
- Fast training, fine-tuning, and deployment
- Resource-efficient, low computational costs

## Dataset & Fine-Tuning Strategy

**Datasets**:  
- [Augmented_Meal_Planner_data](https://huggingface.co/datasets/sridhar52/Augmented_Meal_Planner_data) (4,500 Q&A style prompts)
- [Nutritional-LLama](https://huggingface.co/datasets/Tom158/Nutritional-LLama) (1,488 Q&A style prompts)

**Preprocessing Steps**:
- Adjust the columns and concatenate them to create one large dataset
- Tokenized using pre-trained GPT-2 Small

**Training Details**:
- Epochs: 10 (with early stopping)
- Batch size: 16
- Learning Rate: 5e-5
- Platform: Jupyter Notebook, Visual Studio Code
- Hardware: GPU - RTX 3060 Ti

**Challenges**:
- Limited model capacity
- Data limitations
- Insufficient dataset diversity
- Generic assumptions
- Avoiding generic responses
- Balancing empathy and diversity

## System Architecture

![System Architecture](docs/architecture_diagram.png)

**Components**:

- User input → Web UI (HTML/CSS + React + Vite)
- Backend → GPT-2 Small via Hugging Face
- Output → Contextual nutrition response

## Live Demo

Watch the demo: [`demo/demo_video.mp4`](demo/demo_video.mp4)  

Install requirements:  
`npm install node`  
`pip install -r requirements.txt`  

Run simultaneously:  
`python chat_server.py`  
`npm run dev`  

## Example Scenario
User: I am a vegetarian, and I would like to incorporate more protein into my diet. Furthermore, I have a goal of dropping 2kg and my current weight is 70 kg. Can you recommend a diet plan for me?
Chatbot: As someone with overweight, it's great that you're being proactive about making informed choices. While protein-rich foods like beef chop can be a part-time snack option, it's essential to balance these foods with more significant dietary changes that might impact your health. Given your current weight and health condition, it's essential to focus on nutrient-dense foods that support a healthy weight loss journey.

## Evaluation & Metrics

**Metrics:**

- 5-point Likert Scale (relevance, fluency, safety)
- Qualitative user feedback on coherence, clarity, and usefulness

**Results:**

- Users appreciated coherent and easy-to-read responses but reported inconsistencies with dietary restrictions and occasional hallucinations
- Noted issues with prompt cut-offs and irrelevant or inappropriate assumptions

**Limitations:**

- Weak long-context understanding and constraint adherence (e.g., allergies, dietary restrictions)
- Tendency to hallucinate medical conditions or facts
- Token cutoff leads to incomplete or awkward responses
- Sometimes ignores user input entirely or misinterprets the goal

## Conclusion & Future Work
- Using a stronger model did not always yield in higher quality results
- Training a stronger model took too long and was problematic in testing (could not redeploy and quickly observe changes)
- Given that the backend is powered by a lightweight model, adding in history for user chat was not viable (confused the model)
- Adding synthethic data (approximately 180 rows) did not add significant changes
- If this project were to be revised accordingly, alternative models with additional datasets would've been incorporated
- Synthethic data should've incorporated much more redundant or multiple variations with a much larger size of rows to make a difference.

