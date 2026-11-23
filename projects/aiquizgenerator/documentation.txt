AI Prompt Documentation
Project: AI Quiz Generator, an AI-powered study tool built with Python, Streamlit, PyMuPDF, and Google’s Gemini API. This log summarizes development requests made during the project and the assistance delivered via ChatGPT. 
1.	Prompt: “How can I get the program to read my class notes PDF?”
What was delivered: Provided PyMuPDF-based PDF text extraction and guidance for combining extracted PDF text with pasted notes.
2.	Prompt: “How do I connect the AI to the program?”
What was delivered: Explained how to install the Google GenAI SDK, create a Gemini client, and store the API key in Streamlit secrets rather than hard-coding it.
3.	Prompt: “What about the warnings under the PDF code?”
What was delivered: Recommended using the ‘pymupdf’ import and a context manager to open and close PDF documents safely.
4.	Prompt:”Gemini isn’t following the formatting… it just adds the answers after the questions.”
What was delivered: Explained that generated text formatting can be inconsistent and recommended separating AI content generation from Python-controlled presentation.
5.	Prompt: “Something went wrong: 503 UNAVILABLE…”
What was delivered: Explained that HTTP 503 indicates temporary model demand or service unavailability and advised retrying before changing working code.
6.	Prompt: “What do I need to add to get working JSON with interactive quiz?”
What was delivered: Provided Streamlit implementation that requests JSON, validates question structure, displays A-D choices, grades submissions, shows explanations, and calculates a final score.
7.	Prompt: “How do I go about getting it published so it can be tested off my PC?”
What was delivered: Recommended Streamlit Community Cloud and outlined deployment using the GitHub repository, app file path, requirements file, and Streamlit Secrets. 
8.	Prompt: “ModuleNotFoundError:…”
What was delivered: Recommended checking repository files for errors. Specifically, the “requirements.txt” file. 
9.	Prompt: “How do I change API models?”
What was delivered: Explained how to change from “gemini-3.8-flash” to “gemin-3.5-flash-lite”.
10.	Prompt: “How do I insert screenshots into the README?”
What was delivered: Explained how to upload screenshot files to a screenshots folder and embed them using relative Markdown image paths. 

Project Outcome
The resulting application accepts PDF notes or pasted test, uses Gemini to generate ten multiple-choice questions in JSON format, validates the generated structure, presents an interactive quiz, grades submitted answers, displays explanations, and calculates a final score. The app was published through Streamlit Community Cloud and linked from the GitHub portfolio. 
