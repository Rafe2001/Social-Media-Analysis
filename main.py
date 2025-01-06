from langflow.load import run_flow_from_json

TWEAKS = {
  "GroqModel-YjEcE": {},
  "File-xa6C1": {},
  "SplitText-iXcuY": {},
  "AstraDB-OhIvP": {},
  "ParseData-Y6rAo": {},
  "CombineText-r036t": {},
  "ChatInput-mYBnj": {},
  "Prompt-yorzF": {},
  "ChatOutput-XywCK": {}
}

result = run_flow_from_json(flow="Social_Media_Engagement.json",
                            input_value="message",
                            session_id="41b4f68f-2371-49ae-9e46-6fa7190fb3eb", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)