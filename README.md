[![CI](https://github.com/nogibjj/Fall2023_IDS706_MiniProject3_JiayiZhou/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_MiniProject3_JiayiZhou/actions/workflows/cicd.yml)
## Fall2023_IDS706 Mini Project 3

### Purpose
This is for class data engineering mini-project 3. It uses a Python Ruff GitHub template with polars to run and test a function that provides summary statistics and data visualization for a data frame.

### Steps
I created the template based on the template created by Professor Noah Gift and modified the template. Based on the template from professor, I made the following changes:
1. Added Polars in requirements.txt
2. Modified the function in main.py to read the CSV file, store and return the summary statistics table, create a plot with Polars library.
3. Modified test cases in test_main.py

### Dataset
The dataset is loaded in by url.  Here is the url: [(https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv)](https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv). The file is a comma-separated value spreadsheet (CSV) called goose_rawdata.csv.  
<img width="497" alt="Screenshot 2023-09-12 at 10 19 05 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject3_JiayiZhou/assets/143651921/ca45cc76-2d2e-4d26-a2b5-6bff9dcaf0ee">

### Check format and test errors:
In codespace, I run command make test, make format, and make lint. The commands run smoothly.

### Result
Here is the screenshot of summary statistics table based on the csv file read in.  
<img width="747" alt="Screenshot 2023-09-12 at 10 22 35 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject3_JiayiZhou/assets/143651921/1531756f-c5cf-4aa5-8b6a-caaeee9c31e5">  
Here is the visualization between two variables in the dataframe, which can also be viewed by clicking on Year vs Goose.png.  
<img width="633" alt="Screenshot 2023-09-12 at 10 24 29 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject3_JiayiZhou/assets/143651921/48a774da-b64b-4b1e-b260-c7d685ed0700">



