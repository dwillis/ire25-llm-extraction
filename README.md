# LLM Data Extraction
## IRE 2025
### Derek Willis, University of Maryland

### House Job

Sign into your Google account and head to [AI Studio](https://aistudio.google.com/prompts/new_chat). Make sure you turn down the temperature to 0 and are using the Gemini 2.5 Pro Preview model, and check the "Structured Output" button. Then copy the [text with a single House job ad](https://raw.githubusercontent.com/dwillis/ire25-llm-extraction/refs/heads/main/house_job.txt) and paste it into the chat interface, and add a prompt designed to extract the following elements into a JSON file: the unique identifier, the name of the member, the member's state, the member's party, the title of the job and the salary. Evaluate the results. How did it do?

### Codespaces and Groq Setup

Click the "Use this template" button for this repository and choose "Create a new repository". You can give it the same name or something different.

Once it's ready, go to [Groq](https://console.groq.com/keys) and follow the directions to get an API key. You'll need to login (or create an account if you don't have one).

Copy the API key value and then click on the Settings of your GitHub repository and click on "Secrets and variables" on the left side, then choose "Codespaces"

Click the green "New Repository Secret" button and paste your API Key into the "Secret" box, then put GROQ_API_KEY in the Name box above it. Click "Add Secret" and click on the name of the repository to return to the main page.

From there, click the green "Code" button and create a new Codespace in the Codespaces tab.

### Entity Extraction

In the Terminal type the following: pip install requests groq and hit enter.

Then type: python get_stories.py

You should see a file called lens_nola.json appear. Let's look at it. It contains some details of the 10 latest stories from [The Lens](https://thelensnola.org/). We're going to have an LLM extract entities - people, places and organizations - from those stories.

Back in the Terminal, type: python entity_extraction.py and watch the output - it will be saved in a file called `extracted_entities.json`. Compare that to some of the stories. How did things go?

