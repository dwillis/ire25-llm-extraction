# LLM Data Extraction
## IRE 2025
### Derek Willis, University of Maryland

### House Job

Sign into your Google account and head to [AI Studio](https://aistudio.google.com/prompts/new_chat). Make sure you turn down the temperature to 0 and are using the Gemini 2.5 Pro model, and check the "Structured Output" button. Then copy the [text with a single House job ad](https://raw.githubusercontent.com/dwillis/ire25-llm-extraction/refs/heads/main/house_job.txt) and paste it into the chat interface, and add a prompt designed to extract the following elements into a JSON file: the unique identifier, the name of the member, the member's state, the member's party, the title of the job and the salary. Evaluate the results. How did it do?

### Codespaces and Groq Setup

Click the "Use this template" button for this repository and choose "Create a new repository". You can give it the same name or something different.

Once it's ready, go to [Groq](https://console.groq.com/keys) and follow the directions to get an API key. You'll need to login (or create an account if you don't have one).

Copy the API key value and then click on the Settings of your GitHub repository and click on "Secrets and variables" on the left side, then choose "Codespaces"

Click the green "New Repository Secret" button and paste your API Key into the "Secret" box, then put GROQ_API_KEY in the Name box above it. Click "Add Secret" and click on the name of the repository to return to the main page.

From there, click the green "Code" button and create a new Codespace in the Codespaces tab.

### Entity Extraction

In the Terminal type the following: `pip install requests groq` and hit enter.

Then type: `python get_stories.py`

You should see a file called lens_nola.json appear. Let's look at it. It contains some details of the 10 latest stories from [The Lens](https://thelensnola.org/). We're going to have an LLM extract entities - people, places and organizations - from those stories.

Back in the Terminal, type: `python entity_extraction.py` and watch the output - it will be saved in a file called `extracted_entities.json`. Compare that to some of the stories. How did things go?

### Longer Text Extraction

Let me introduce you to one of my favorite tools for working with LLMs, a Python library called, well, [llm](https://llm.datasette.io/en/stable/). We'll install it, then a tool that works with Google's Gemini models.

In the Terminal, type the following: `pip install llm` and hit Return. Then type `llm install llm-gemini` and hit Return. Now we'll need an API Key to use Gemini this way. [Create an API Key](https://aistudio.google.com/u/4/apikey) and copy the value. Now, back in the Terminal, type `llm keys set gemini` and hit Return. You'll be given the chance to paste in that API Key value. Hit the Paste key - you won't see the actual value, and you might see a grayed-out "Paste" appear - when you can actually click on it, do that, then hit Return.

Now we can test it out. In the Terminal, type or copy/paste this: `llm -m gemini-2.5-flash-preview-05-20 "10 names for a pet iguana"` (you can change the animal if you like) and hit Return.

We'll now use a text file with the contents of sanctions against Maryland attorneys to test out Gemini's abilities. We'll try to get a CSV file of names, sanctions and the dates involved. We're using the `cat` utility to pass the text to Gemini. Copy and paste the following command into the Terminal: `cat sanctionsfy25.txt | llm -m gemini-2.5-flash-preview-05-20 'list the names of sanctioned individuals, the sanction and the date of sanction in a CSV format, with dates in yyyy-mm-dd format'`

How did it do?


