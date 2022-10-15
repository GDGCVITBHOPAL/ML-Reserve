
<p align="center">
  <img src="assets/logo.png" />
</p>
&nbsp;

## Scrape images from google and create your own training dataset

**Installation**
1. Fork the Project
2. Clone your forked repository on your host machine  

```bash
  git clone <your-forked-repository.git>
  cd Scrapster
```

3. **To install the dependencies and packages on your host machine**
```python
pip install -r requirements.txt
```
4. **Install chromedriver**

- Ensure you have the [appropriate version](https://chromedriver.chromium.org/downloads) of ChromeDriver on your machine if you would like to scrape from Google Images.

## **Edit your desired parameters in main.py**
> On Linux
```bash
  PATH = "/home/ams/chromedriver"   # path to chromedriver
  LIMIT = 100                       # how much images you want to download
  query = "solar panels"              # keyword you want to search for
```
> On Windows
```bash
  PATH = "path/to/chromedriver.exe"   # path to chromedriver
  LIMIT = 100        # how much images you want to download
  query = "solar panels" # keyword you want to search for
```

## **Run the program**

```bash
  python main.py
```

