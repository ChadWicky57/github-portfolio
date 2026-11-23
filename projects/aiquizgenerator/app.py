
import streamlit as st
import pymupdf
import json
import re
from google import genai

# -----------------------------
# Page setup
# -----------------------------

st.set_page_config(page_title="AI Quiz Generator", page_icon="📚")

st.title("AI Quiz Generator")
st.write("Upload your class notes or paste text to create an interactive quiz.")

# Keep quiz data between Streamlit refreshes
if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "quiz_version" not in st.session_state:
    st.session_state.quiz_version = 0

if "submitted" not in st.session_state:
    st.session_state.submitted = False


# -----------------------------
# Upload study material
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload class notes (PDF)",
    type=["pdf"]
)

notes = st.text_area("Or paste your notes here:")


# -----------------------------
# Generate quiz
# -----------------------------

if st.button("Generate Interactive Quiz"):

    extracted_text = ""

    if uploaded_file is not None:
        try:
            with pymupdf.open(
                stream=uploaded_file.getvalue(),
                filetype="pdf"
            ) as pdf:
                for page in pdf:
                    extracted_text += page.get_text()

        except Exception as e:
            st.error(f"Could not read PDF: {e}")

    extracted_text += "\n" + notes

    if not extracted_text.strip():
        st.warning("Please upload a readable PDF or enter some notes.")

    else:
        try:
            client = genai.Client(
                api_key=st.secrets["GEMINI_API_KEY"]
            )

            prompt = f"""
Create exactly 10 multiple-choice questions using ONLY
the study material provided below.

Return ONLY valid JSON using this exact structure:

{{
  "questions": [
    {{
      "question": "Question goes here?",
      "choices": {{
        "A": "First answer choice",
        "B": "Second answer choice",
        "C": "Third answer choice",
        "D": "Fourth answer choice"
      }},
      "answer": "A",
      "explanation": "Explain why A is correct."
    }}
  ]
}}

Requirements:
- Generate exactly 10 questions.
- Every question must have exactly four choices.
- Label choices A, B, C, and D.
- Include exactly one correct answer per question.
- The answer field must contain only A, B, C, or D.
- Include an explanation for every question.
- Do not repeat questions.
- Do not invent facts.
- Do not include Markdown or text outside the JSON.

STUDY MATERIAL:
{extracted_text[:30000]}
"""

            with st.spinner("Generating your quiz..."):

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt,
                    config={
                        "response_mime_type": "application/json"
                    }
                )

            # Parse Gemini's JSON response
            response_text = response.text.strip()

            # Remove code fences if Gemini includes them
            response_text = re.sub(
                r"^```(?:json)?\s*|\s*```$",
                "",
                response_text
            )

            quiz_data = json.loads(response_text)

            # Validate quiz structure
            questions = quiz_data["questions"]

            if len(questions) != 10:
                raise ValueError("Gemini did not generate exactly 10 questions.")

            for q in questions:
                if not isinstance(q["question"], str):
                    raise ValueError("A question is missing its text.")

                if set(q["choices"].keys()) != {"A", "B", "C", "D"}:
                    raise ValueError("A question does not have four valid choices.")

                if q["answer"] not in ["A", "B", "C", "D"]:
                    raise ValueError("A question has an invalid correct answer.")

                if not q["explanation"]:
                    raise ValueError("A question is missing its explanation.")

            # Save quiz in Streamlit session
            st.session_state.quiz = questions
            st.session_state.quiz_version += 1
            st.session_state.submitted = False

            st.rerun()

        except json.JSONDecodeError:
            st.error("Gemini returned invalid JSON. Please try generating again.")

        except KeyError as e:
            st.error(f"The generated quiz is missing a required field: {e}")

        except Exception as e:
            st.error(f"Something went wrong: {e}")


# -----------------------------
# Display interactive quiz
# -----------------------------

if st.session_state.quiz is not None:

    questions = st.session_state.quiz

    st.divider()
    st.header("Interactive Multiple-Choice Quiz")

    st.write("Select one answer for each question.")

    for i, q in enumerate(questions):

        st.subheader(f"Question {i + 1}")

        st.write(q["question"])

        st.radio(
            "Choose your answer:",
            options=["A", "B", "C", "D"],
            format_func=lambda choice, choices=q["choices"]:
                f"{choice}. {choices[choice]}",
            key=f"answer_{st.session_state.quiz_version}_{i}",
            disabled=st.session_state.submitted
        )

    # -----------------------------
    # Submit and grade quiz
    # -----------------------------

    if not st.session_state.submitted:

        if st.button("Submit Quiz"):

            unanswered = []

            for i in range(len(questions)):
                key = f"answer_{st.session_state.quiz_version}_{i}"

                if key not in st.session_state:
                    unanswered.append(i + 1)

            if unanswered:
                st.warning(
                    "Please answer every question before submitting."
                )

            else:
                st.session_state.submitted = True
                st.rerun()

    # -----------------------------
    # Display results
    # -----------------------------

    if st.session_state.submitted:

        st.divider()
        st.header("Your Quiz Results")

        score = 0

        for i, q in enumerate(questions):

            key = f"answer_{st.session_state.quiz_version}_{i}"
            selected = st.session_state[key]
            correct = q["answer"]

            st.subheader(f"Question {i + 1}")

            if selected == correct:
                score += 1
                st.success("Correct!")

            else:
                st.error(f"Incorrect. Your answer: {selected}")

            st.write(f"Correct answer: {correct}")
            st.write(f"Explanation: {q['explanation']}")

        percentage = (score / len(questions)) * 100

        st.divider()
        st.subheader(f"Final Score: {score}/10")
        st.write(f"Percentage: {percentage:.0f}%")

        if score >= 8:
            st.success("Great work!")
        elif score >= 6:
            st.info("Good effort. Review the questions you missed.")
        else:
            st.warning("Keep studying and try again.")

        if st.button("Generate Another Quiz"):
            st.session_state.quiz = None
            st.session_state.submitted = False
            st.rerun()
