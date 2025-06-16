import os
import json

from groq import Groq

def load_stories(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)[:10]  # Load and return the first 10 stories

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Path to your JSON file containing stories
file_path = 'cns_maryland_posts.json'
stories = load_stories(file_path)

# Define a structured prompt that explicitly requests the JSON format
prompt_template = """
Analyze the following news article text and extract entities mentioned. Return ONLY a valid JSON object with this exact structure:

{{
  "people": ["Person Name 1", "Person Name 2", ...],
  "places": ["Place Name 1", "Place Name 2", ...],
  "organizations": ["Organization Name 1", "Organization Name 2", ...]
}}

Make sure to:
1. Include only entities that are explicitly mentioned in the text
2. Only return the JSON object, with no additional text before or after
3. Use empty arrays for categories where no entities are found
4. Remove any duplicate entities within each category
5. Only include proper nouns (capitalize names appropriately)

Text to analyze:
---
{content}
---
"""

# Create a list to store all extracted entities
all_entities = []

# Iterate over the stories and ask the model to identify entities
for i, story in enumerate(stories):
    print(f"Processing story {i+1}/{len(stories)}...")
    
    # Format the prompt with the story content
    formatted_prompt = prompt_template.format(content=story['content'])
    
    # Get the story link
    story_link = story.get("link", "")
    
    # Call the model with the structured prompt
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": formatted_prompt,
            }
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None
    )
    
    # Get the model's response
    response_content = chat_completion.choices[0].message.content
    
    try:
        # Parse the response to verify it's valid JSON
        entity_data = json.loads(response_content)
        
        # Add only the story link to the entity data
        entity_data["url"] = story_link
        
        # Add to the list of all entities
        all_entities.append(entity_data)
        
        # Print the result for this story
        print(json.dumps(entity_data, indent=2))
        print("-" * 50)
        
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON response for story {i+1}")
        print(f"Response: {response_content}")
        print(f"Error details: {e}")
        print("-" * 50)

# Save all extracted entities to a file
output_file = "extracted_entities.json"
with open(output_file, "w") as f:
    json.dump(all_entities, f, indent=2)

print(f"All entities have been saved to {output_file}")