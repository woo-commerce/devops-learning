from pathlib import Path
import os
from anthropic import Anthropic


def classify_line(client, line):

    message = client.messages.create(
        max_tokens=200, 
        messages=[    
                    {
                        "role": "user",
                        "content": f"Classify this log line as 'normal' or 'anomaly' and give a one-line reason:\n{line}"
                    } 
                    ],
        model = "claude-haiku-4-5-20251001"
    )
    print(message.content[0].text)

def read_log_file(client, filename):
    with open(filename,"r") as file:
        for line in file:
            #classify_line(_ , line)
            classify_line(client, line)


def main():
   source_file = Path("/Users/lakhankalra/moveinsync/AI_agentic/devops-learning")
   client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
   for file in source_file.glob("*.log"):
      
      read_log_file(client, file)

if __name__ == "__main__":
    main()