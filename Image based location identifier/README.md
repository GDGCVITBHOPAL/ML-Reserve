# Documentation and user manual  🗒.

It's a very basic and easy to use image search using google image search API.

<hr>

## Why I created this? 🧐.

I am learing how to use google image search API using python to create a simple image search application.

You can also watch some of the exciting projects on my github account.

<hr>

## Please visit my [website](https://aayushkumar20.github.io) to know about me.

<hr>

# Installation and Basic requirements.

### Basic requirements.

- For this project you have to install some pip packages like `pip install -q gradio` and `pip install "tf-nightly"`. 
- For best result i'll recommend you to use 'Google Colab'.
- 🛑 Please note that 'Google Colab' has it's own GPU and TPU so in most of the cases you'll not required to install `pip install tensorflow`.
- A keyboard and mouse.
- An image containing the monument that you want to search.
- Active internet connection.
- 🛑 Please note that 'Google Colab' has it's own GPU and TPU so in most of the cases you'll not required to install `pip install tensorflow`.

### Installation and usages.

- For proper functioning please install 'gradio and tensorflow'

<img width="1440" alt="Screenshot 2022-01-12 at 20 56 50" src="https://user-images.githubusercontent.com/37871733/149169921-1b555c4c-a879-4f65-88b5-c684e2af7c24.png">

- Import all the required modules for proper functioning.

<img width="1440" alt="Screenshot 2022-01-12 at 21 05 19" src="https://user-images.githubusercontent.com/37871733/149171419-b2e7b73b-cb92-4a5e-82b8-e85908aad785.png">

- # Make sure to install all the modules and 'gradio modules' before interpreting.

- Importing all the required trained API for image recognisation.
- This module is trained only for some common places in Asian subcontinent.

<img width="1440" alt="Screenshot 2022-01-13 at 08 05 27" src="https://user-images.githubusercontent.com/37871733/149255758-4031a0c6-259a-451d-9a69-cf2be70e5d2f.png">

- Please make sure that you have used the 2d array as (321,321), othewise it'll show error in the next step.

<img width="1440" alt="Screenshot 2022-01-13 at 08 11 29" src="https://user-images.githubusercontent.com/37871733/149256343-c842a9da-24b0-4cdf-83d4-3fbc4aa80740.png">

- Please make sure to keep the images in the same directory or in same folder with the name as enterd in the program.

<img width="1440" alt="Screenshot 2022-01-12 at 21 36 33" src="https://user-images.githubusercontent.com/37871733/149177146-726905a5-d5ee-426d-a8f4-182ee4a3331c.png">

- 🛑 Otherwise it'll show some errors.

- Now run next command to check whether the image containing directory is mounted properly or not.

<img width="1440" alt="Screenshot 2022-01-13 at 08 14 48" src="https://user-images.githubusercontent.com/37871733/149256694-230212ca-08fb-4e9c-a256-4cdc8a1446de.png">

- 🟢 If it shows the image then it means that all the process is going correctly.
- Now we'll check for array size and verify that wether it satisfy the array size of (321,321) or not.

<img width="1440" alt="Screenshot 2022-01-13 at 08 18 11" src="https://user-images.githubusercontent.com/37871733/149256987-6bdd6ea4-4364-4044-adab-afb65a30a376.png">

- In this case both of it satisfy the array value (321,321).
- Now we'll predict the location by using the predict option of tensorflow and also using google API.

<img width="1440" alt="Screenshot 2022-01-13 at 08 20 41" src="https://user-images.githubusercontent.com/37871733/149257219-8e41e405-69b0-4045-af0d-60b71b81adfd.png">

- Here our tensor flow model sucessfully discovered the image as 'India gate'.
- As it is an open source project and other user can also insert their image for searching.
- That's why there's an UI for easy user interaction.

<img width="1440" alt="Screenshot 2022-01-13 at 08 26 02" src="https://user-images.githubusercontent.com/37871733/149257726-ff615a4a-983d-4bcf-bf9c-c9a688b87aab.png">

- When we'll click the link of Gradio in the last block then it'll open a new tab where we can insert the new image or the place you want to search.

<img width="1440" alt="Screenshot 2022-01-13 at 08 31 22" src="https://user-images.githubusercontent.com/37871733/149258259-052c193c-3a03-4069-9aba-6a75fe3d4676.png">

<br>
<div align="center">

## Thank You for reading it and hope you'll like it 😁.

</div>

<img src= "https://th.bing.com/th/id/R.8c089d8bc5c454ed37d8193397159f76?rik=Du9yMSlAmXKatQ&riu=http%3a%2f%2fpluspng.com%2fimg-png%2fblack-and-white-city-png-city-png-picture-4963.png&ehk=P%2fZz6HKxn5eT3nj3YEqQ8TsdQZhiGlMrsYJdFRBSktY%3d&risl=&pid=ImgRaw&r=0">
