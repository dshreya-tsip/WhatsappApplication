import os
import anthropic
from docx import Document

def load_srs(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

def generate_test_cases(srs_text):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""
    You are a QA engineer. Based on the following Software Requirements Specification (SRS), generate a list of functional and non-functional test cases in a table format.

    Columns: Test Case ID, Description, Input, Expected Output, Test Type

    SRS:
    {srs_text}
    """

    response = client.messages.create(
        model="claude-3-opus-20240229",  # Or any Claude 3 model you have access to
        max_tokens=1000,
        temperature=0.5,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text

if __name__ == "__main__":
    srs_path = "SRS.docx"
    srs_text = load_srs(srs_path)
    test_cases = generate_test_cases(srs_text)

    print("📋 Generated Test Cases:")
    print(test_cases)

    # Optional: Save to file
    with open("test_cases.md", "w", encoding="utf-8") as f:
        f.write(test_cases)
