import pandas as pd

data = []
with open('/Users/sleepdeprived/Documents/Nayan/Python/Eng2Ger/dataset/deu.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) >= 2:  
            english, german = parts[:2]
            data.append((english, german))

max_words = int(input("Enter max words: "))
df = pd.DataFrame(data[:max_words], columns=['English', 'German'])

def normalize_text(text):
    text = text.lower()
    text = text.strip()
    text = ''.join(c for c in text if c.isalnum() or c.isspace())  # Remove special characters
    return text

df['English'] = df['English'].apply(normalize_text)
df['German'] = df['German'].apply(normalize_text)

df.to_csv('preprocessed_data.csv', index=False)

