import pandas as pd
import wget, sys, re, os

W_DIR = sys.argv[1]

def allcaps(str):
  str = re.sub(r'[,.;:]', '', str)
  return str.upper().replace(' ', '_')

def sanitize(str):
  return str.replace(' ', '_').lower()

df = pd.read_csv("free-springer.csv")
urls = df.OpenURL
titles = df['Book Title']
authors = df.Author
i = 1
fails = []
for u,t,a in zip(urls[1:], titles[1:], authors[1:]):
  pdf = u.replace("openurl?genre=book&isbn=", "content/pdf/10.1007/")
  try:
    dis = wget.download(pdf, W_DIR + allcaps(a) + "__" + sanitize(t) + ".pdf")
    i += 1
  except:
    fails += [i]
    print("\nAn error at step : " + str(i))

list = os.listdir(W_DIR)
nf = len(list)
print("You downloaded " + str(nf) + " files. Congrats!\n")
print("Some downloads failed at indices " + str(fails))