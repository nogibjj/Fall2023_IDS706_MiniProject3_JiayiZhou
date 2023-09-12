[![CI](https://github.com/nogibjj/Fall2023_IDS706_MiniProject3_JiayiZhou/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_MiniProject3_JiayiZhou/actions/workflows/cicd.yml)
## Fall2023_IDS706 Mini Project 3

### Purpose
This is for class data engineering mini-project 3. It uses a Python Ruff GitHub template with polars to run and test a function that provides summary statistics for a data frame.

### Steps
I created the template based on the template created by Professor Noah Gift and modified the template. Based on the template from professor, I made the following changes:
1. Added Polars in requirements.txt
2. Modified the function in main.py to read the CSV file, store and return the summary statistics table, create a plot with Polars library.
3. Modified test cases in test_main.py

### Dataset
The dataset is loaded in by url.  Here is the url: https://www.dropbox.com/s/x2awp0e9znsyub7/egrid2016.csv?dl=1. The file is a comma-separated value spreadsheet (CSV) called egrid2016.csv. This dataset is the Environmental Protection Agency's (EPA) Emissions & Generation Resource Integrated Database (eGRID) containing information about all power plants in the United States, the amount of genereration they produce, what fuel they use, the location of the plant, and many more quantities.  
<img width="430" alt="Screenshot 2023-09-11 at 3 13 34 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject2_JiayiZhou/assets/143651921/c1a45b64-1c5f-424f-91ee-f302fcc5a5cb">

### Check format and test errors:
In codespace, I run command make test, make format, and make lint. The commands run smoothly.
<img width="892" alt="Screenshot 2023-09-06 at 11 21 09 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject2_JiayiZhou/assets/143651921/700df81e-94c5-4d79-85f6-89e9b811bb54">

### Result
Here is the screenshot of summary statistics table based on the csv file read in, which can also be downloaded from the html file in the repo.  
<img width="344" alt="Screenshot 2023-09-10 at 10 02 03 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject2_JiayiZhou/assets/143651921/a07ab619-e63b-457e-88bb-515d03ce5949">

Here is the visualization between two variables in the dataframe, which can also be downloaded from html file or click on plant_capacity_factor.png.  
<img width="606" alt="Screenshot 2023-09-11 at 2 14 07 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject2_JiayiZhou/assets/143651921/858fd105-417e-49c7-8d71-a9b97ff7a328">  
As we can see from the plot, when plant capacity factor increases, plant annual net generation increases.



