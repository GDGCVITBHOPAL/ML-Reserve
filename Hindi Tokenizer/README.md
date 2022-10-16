<h1 align="center"> Hindi Tokenizer </h1> <br>

<p align="center">
  <a href="https://github.com/DSCVITBHOPAL/ML-Reserve/tree/main/Hindi%20Tokenizer">
    <img alt="Tokenizer" title="Tokenizer" src="https://user-images.githubusercontent.com/97695341/195518913-901dfc68-db1a-4faf-87e9-dc4e43fbda81.gif" width="450">
  </a>
</p>

Video of code run: https://drive.google.com/file/d/1KjsPPoEl-lHvEuN2WyoBWHTx6HgqP47Y/view?usp=sharing

## About Tokenization
Natural Language Processing (NLP) enables machine learning algorithms to organize and understand human language. NLP enables machines to not only gather text and speech but also identify the core meaning it should respond to. Tokenization is one of the many pieces of the puzzle in how NLP works. Tokenization is a simple process that takes raw data and converts it into a useful data string. While tokenization is well known for its use in cybersecurity and the creation of NFTs, tokenization is also an important part of the NLP process. Tokenization is used in natural language processing to split paragraphs and sentences into smaller units that can be more easily assigned meaning. The first step of the NLP process is gathering the data (a sentence) and breaking it into understandable parts (words). Here’s an example of a string of data:
<br><br>“What restaurants are nearby?”  <br><br>
For this sentence to be understood by a machine, tokenization is performed on the string to break it into individual parts. With tokenization, we’d get something like this:
<br><br>‘what’ ‘restaurants’ ‘are’ ‘nearby’ <br><br>
This may seem simple, but breaking a sentence into its parts allows a machine to understand the parts as well as the whole. This will help the program understand each of the words by themselves, as well as how they function in the larger text.
<br>
## Data/Packages used
We have used the package - Natural Language Toolkit for Indic Languages (iNLTK). This package helps by providing out-of-the-box support for various NLP tasks that an application developer might need.
It supports a wide variety of languages:
Language | Hindi | Punjabi | Gujarati | Kannada | Malayalam | Oriya | Marathi | Bengali | Tamil | Urdu | Nepali | Sanskrit | English | Telugu
--- | --- | --- | --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |---
Code | hi | pa | gu | kn | ml | or | mr | bn | ta | ur | ne | sa | en | te

https://github.com/goru001/inltk
<br><br>We have used the dataset called as “HindiEnglish Corpora” provided by Aiswaryaramachandran.
The dataset comprises Hindi English Truncated Corpus that is, it contains a huge list of sentences translated from English to Hindi, thus providing us with enough data to work on.
<br>https://www.kaggle.com/datasets/aiswaryaramachandran/hindienglish-corpora

## Code
https://colab.research.google.com/drive/1deNNkra2rS2imrAvGj90mHYp05EA6lYp?usp=sharing

## Code Explanation
To upload the file from the local drive we write the following code in the cell and run it
<br>
```
from google.colab import files
uploaded = files.upload()
```
We click on the “choose files” option, then select and download the CSV data set file (which we downloaded from Kaggle known as 'Hindi_English_Truncated_Corpus.csv') from our local drive.  Later we write the following code snippet to import it into a pandas data frame.
```
import pandas as pd
import io

df = pd.read_csv(io.BytesIO(uploaded['Hindi_English_Truncated_Corpus.csv']))
```
The head() function is used to get the first n rows. This function returns the first n rows for the object based on position. It is useful for quickly testing if your object has the right type of data in it.
```
df.head()
```
Next, we install the torch. PyTorch is a Python package that provides two high-level features:
* Tensor computation (like NumPy) with strong GPU acceleration
* Deep neural networks built on a tape-based autograd system 
<p />

```
pip install torch==1.12.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
```
iNLTK runs on CPU, as is the desired behaviour for most of the Deep Learning models in production. The command above will install PyTorch for CPU, which, as the name suggests, does not have Cuda support.
<br>The iNLTK is installed once all its requirements are satisfied with python libraries and packages by the following code:
```
pip install inltk
```
The torch-1.12.1-cp37-cp37m-manylinux1_x86_64.whl version gets downloaded. Once the download has been successfully completed we set up the language we want to use the tokenizer for:
```
from inltk.inltk import setup
setup('hi')
```
We used ‘hi’ since we will be using the language Hindi for the tokenizer.
<br>Note: ignore the runtime error as it is probably caused by the difference in the torch version of the package used and the latest one we are using. At the end of the output, we can see the code does run without error and provides output as “Done!”.
<br>We import the tokenizer using the following command from the iNLTK package:
```
from inltk.inltk import tokenize
```
Since we have already provided data set for the program. Therefore we just call the tokenizer function and sentence by its code which was shown in the df.head() command’s output.
```
tokenize(df.hindi_sentence[0],"hi")
tokenize(df.hindi_sentence[1],"hi")
tokenize(df.hindi_sentence[2],"hi")
tokenize(df.hindi_sentence[3],"hi")
tokenize(df.hindi_sentence[4],"hi")
```
We will receive the output in the form of tokens of the sentence provided.
<br>Alternative way to provide sentence to our program is by specifying the string name and providing the sentence or paragraph as input, like this:
```
hindi_input = """प्राचीन काल में विक्रमादित्य नाम के एक आदर्श राजा हुआ करते थे।<br>
अपने साहस, पराक्रम और शौर्य के लिए  राजा विक्रम मशहूर थे। <br>
ऐसा भी कहा जाता है कि राजा विक्रम अपनी प्राजा के जीवन के दुख दर्द जानने के लिए रात्री के पहर में भेष बदल कर नगर में घूमते थे।"""
```
The tokenize command now will be provided in the format of:<br>
tokenize(input text, language code)
```
tokenize(hindi_input, "hi")
```
This command’s output will also provide us tokens of the given paragraph which we provided in “hindi_input”.
<br>Further in this tokenizer, we have imported the feature to remove foreign languages as well.
```
from inltk.inltk import remove_foreign_languages
```
The command to implement this import is of the format:
```
Remove_foreign_languages(text, “<language-code>”)
```
If any word in the sentence is detected by the program which doesn’t belong to the language whose language code we have provided in the command, then the word will turn out in the output as <unk>
```
remove_foreign_languages("इस्लाम धर्म (الإسلام) ईसाई धर्म के बाद अनुयाइयों के आधार पर दुनिया का दूसरा सब से बड़ा धर्म है।", "hi")
```
Here, الإسلام is not a Hindi word, hence it will be <unk> in the output.
