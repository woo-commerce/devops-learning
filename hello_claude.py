import os 

from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
                   max_tokens=200, 
                    
                    messages=[    
                    {
                        "role": "user",
                        "content": "Hello claude"
                    } 
                    ],
                    model="claude-haiku-4-5-20251001"
                    )

print(message.content[0].text)