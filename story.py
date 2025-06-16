import os

from groq import Groq

def load_story(file_path):
    with open(file_path, 'r') as file:
        return file.read()  # Read the entire content of the file

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Path to your text file containing a single story
file_path = 'story.txt'
story_content = load_story(file_path)

# Ask the model to identify entities in the story
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Identify the people, places, and organizations in the following text: {story_content}.",
        }
    ],
    model="llama3-70b-8192",
)

# Print the result
print(chat_completion.choices[0].message.content)
