# LLM Data Extraction
## IRE 2025
### Derek Willis, University of Maryland

### Instructions

Click the "Use this template" button for this repository and choose "Create a new repository". You can give it the same name or something different.

Once it's ready, go to [Groq](https://console.groq.com/keys) and follow the directions to get an API key. You'll need to login (or create an account if you don't have one).

Copy the API key value and then click on the Settings of your GitHub repository and click on "Secrets and variables" on the left side, then choose "Codespaces"

Click the green "New Repository Secret" button and paste your API Key into the "Secret" box, then put GROQ_API_KEY in the Name box above it. Click "Add Secret" and click on the name of the repository to return to the main page.

From there, click the green "Code" button and create a new Codespace in the Codespaces tab.

In the Terminal type the following: pip install requests groq and hit enter.

Then type: python get_stories.py

You should see a file called lens_nola.json appear. Let's look at it. It contains some details of the 10 latest stories from The Lens. We're going to have an LLM extract entities - people, places and organizations - from those stories.

Back in the Terminal, type: python entity_extraction.py and watch the output.
