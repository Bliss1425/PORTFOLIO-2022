### Introduction
The Automobile dataset contains information about motor vehicles, the information can be used for several purposes such as price prediction and can also assist a client on decision making. After cleaning and analysing the dataset, we can get a better idea of which variables are important to consider when predicting the car price. The dataset has 26 attributes/features and 205 rows.

The result on this dataset is to figure out the impact of the other variables on price, what drive the prices for the different cars.


## DATA CLEANING

### SUMMARY OF THE METHODS AND VISUALIZATIONS DONE DURING DATA CLEANING

Data cleaning techniques relies on a lot of factors. First, what kind of data are you dealing with? Are they numeric values or strings?

-Using the drop () function to remove Irrelevant Columns on the data set in this, those that don’t fit the specific problem that I am trying to solve:
[df. drop(['num-of-doors','engine-location','aspiration','bore','stroke']
-Cleaning up the "make" column to make sure there's no data entry inconsistencies in it.Had to run a check for duplicated rows in the dataset, fortunately found none. 

The automobile data set has some anomalies, some columns are not of the correct data type. Numerical variables should have type 'float' or 'int', and variables with strings such as categories should have type 'object’. We must convert data types into a proper format for each column using the 
"astype ()" method.


## MISSING DATA

To check null values in a pandas data frame, we use isnull() function and also run a count function per column to ascertain the actual number of the missing values. The automobile dataset has null missing value and that has also been visualized by a heatmap diagram.
