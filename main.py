import os
import textract
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Step 1: Extract text from the PDF
def extract_text_from_pdf(pdf_path):
    try:
        text = textract.process(pdf_path).decode('utf-8')
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        return None

# Step 2: Preprocess the extracted text (e.g., split into paragraphs, clean)
def preprocess_text(text):
    # Add your text preprocessing logic here (e.g., splitting into paragraphs)
    paragraphs = text.split('\n\n')  # Split by double line breaks
    cleaned_paragraphs = [p.strip() for p in paragraphs if p.strip()]  # Remove empty paragraphs
    return cleaned_paragraphs

# Step 3: Train the chatbot using OpenAI's GPT-3 API
def train_chatbot(text):
    # Define a prompt for training
    prompt = "Train a chatbot:"

    # Combine the prompt and extracted text
    input_text = f"{prompt}\n{text}"

    # Make an API call to GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can choose an appropriate engine
        prompt=input_text,
        max_tokens=1000,  # Adjust the max tokens as needed
        n = 1,  # Number of completions
        stop=None,  # Optional: Specify stop words to end the response
        temperature=0.7,  # Adjust the temperature for creativity
    )

    # Extract the chatbot's response
    chatbot_response = response.choices[0].text

    return chatbot_response

# Step 4: Main function
def main(pdf_path):
    # Step 1: Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_path)

    if pdf_text:
        # Step 2: Preprocess the extracted text
        preprocessed_text = preprocess_text(pdf_text)

        # Step 3: Train the chatbot
        chatbot_response = train_chatbot('\n'.join(preprocessed_text))

        # Step 4: Display the chatbot's response
        print("Chatbot Response:")
        print(chatbot_response)

if __name__ == "__main__":
    # Replace 'your_pdf.pdf' with the path to your PDF file
    pdf_file_path = 'the_explosives_act_1884_2.pdf'
    
    if os.path.isfile(pdf_file_path):
        main(pdf_file_path)
    else:
        print("PDF file not found. Please provide the correct path.")
