import re

with open('items.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace all desc: "..." , with desc: "",
# Handle multiline content by finding matching quotes
result = []
i = 0
while True:
    # Find 'desc: "' 
    idx = c.find('desc: "', i)
