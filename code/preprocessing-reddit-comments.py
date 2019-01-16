import pandas as pd

train_text = pd.read_csv("data.csv")

###preprocessing -
print("Preprocessing... 1. split new lines, 2. convert to lowercase, and 3. strip numbers and punct")

### 1) remove newlines
train_text['text'] = train_text['text'].replace('\n', ' ', regex = True)

## 2) convert to lowercase
train_text['text'] = train_text['text'].str.lower()

# ### 3) remove punct and numbers: https://stackoverflow.com/questions/47947438/preprocessing-string-data-in-pandas-dataframe
import re
train_text["text"] = train_text.text.apply(lambda x : " ".join(re.findall('[\w]+',x)))