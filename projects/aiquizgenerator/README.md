Access to the app can be made through the following link:
https://app-portfolio-pj9ctrwaasmvdcvwysctt5.streamlit.app/

# AI Quiz Generator

## 1. Project Overview

The AI Quiz Genrator is an AI-powered study tool designed to help students prepare for exams and improve their understanding of course material. The application allows users to upload PDF class notes or paste text directly into the program. Using Google's Gemini AI, the application analyzes the provided material and generates an interactive multiple-choice quiz.

Students can answer questions, submit their responses, receive immediate grading, review explanations, and view their final score.

The project was developed using Python and Streamlit and is hosted online through Streamlit Community Cloud.

## 2. Features

- **PDF Upload:** Upload class notes and study materials in PDF format.
- **Text Input:** Paste class notes directly into the application.
- **AI Question Generation:** Uses Google Gemini AI to generate 10 multiple-choice questions based on the supplied material.
- **Multiple-Choice Answers:** Each question includes four answer choices labeled A, B, C, and D.
- **Interactive Quiz:** Students select their answers directly in the application.
- **Automatic Grading:** Evaluates submitted answers and identifies correct and incorrect responses.
- **Answer Explanations:** Provides explanations for the correct answers.
- **Final Score:** Calculates and displays the student's score and percentage.
- **Generate Another Quiz:** Allows students to generate and complete another quiz.

## 3. Installation Instructions

### Requirements

- Python 3.10 or newer
- Google Gemini API key
- Internet connection
- Required Python packages

### Installation

1. Clone or download the project repository.

2. Open a terminal in the project directory.

3. Install the required packages:

```bash
py -m pip install -r requirements.txt
```

4. Create a folder named `.streamlit` in the project directory.

5. Inside that folder, create a file named `secrets.toml`.

6. Add your Gemini API key:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

7. Save the file.

**Important:** Never upload your API key or `secrets.toml` file to GitHub.

## 4. Usage Guide

1. Open the StudyBuddy AI application.
2. Upload a PDF containing class notes or paste study material into the text box.
3. Select **Generate Interactive Quiz**.
4. Wait while Gemini analyzes the material and generates the questions.
5. Read each question and select one of the four answer choices.
6. Select **Submit Quiz** when all questions have been answered.
7. Review your results, including correct answers and explanations.
8. Check your final score and percentage.
9. Select **Generate Another Quiz** to start again.

## 5. Screenshots

Add screenshots of the application below to demonstrate its functionality.

### Application Homepage
[Insert screenshot of the application homepage here.]

### Generated Interactive Quiz
[Insert screenshot showing generated questions and answer choices here.]

### Quiz Results
[Insert screenshot showing the final score and answer explanations here.]

## 6. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Application interface and interactive quiz |
| Google Gemini AI | Generates quiz questions and explanations |
| PyMuPDF | Extracts text from uploaded PDF documents |
| JSON | Structures and organizes AI-generated questions |
| GitHub | Source code management and project repository |
| Streamlit Community Cloud | Online application hosting |

## 7. Future Enhancements

Potential improvements for future versions include:

- Add short-answer and true/false question formats.
- Allow users to select the number of questions generated.
- Add difficulty settings such as easy, medium, and hard.
- Save previous quiz results and track performance over time.
- Add user accounts and personalized study progress.
- Support image-based and handwritten study notes.
- Improve quiz customization and study recommendations.

---

**Developer:** Chad Brown

**Project:** AI Quiz Generator

**Repository:** [GitHub Portfolio](https://github.com/ChadWicky57/github-portfolio)
