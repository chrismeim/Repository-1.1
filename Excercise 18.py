import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import datetime 
import copy


#import data
data = pd.read_excel(r"C:\Users\Chris\Desktop\Imperial Reading Material\Spring Term\Financial Econometrics\Econometrics Assignment\PredictorData.xls")


#Convert datatime and set yyyymm as index
data['yyyymm'] = pd.to_datetime(data['yyyymm'].astype(str), format='%Y%m')
data.set_index("yyyymm", inplace= True)



# develop a new dataframe that contains all the necessay information
u_data = {}

u_data["CRSP_SPvw"] = data["CRSP_SPvw"]
u_data["Div"] = data["D12"]
u_data["Earn"] = data["E12"]
u_data["Rfree"] = data["Rfree"] #I don't now if we should use Rfree or the tbl column, refer page 3

u_data = pd.DataFrame(u_data)




#Calculating the 3 diferemt parameters/ratios, refer page 3
u_data["d/p"] =  np.log(u_data["Div"]) - u_data["CRSP_SPvw"]
u_data["d/y"] =  np.log(u_data["Div"]) - u_data["CRSP_SPvw"].shift(1)
u_data["e/p"] =  np.log(u_data["Earn"]) - u_data["CRSP_SPvw"]
u_data["excess_return"] = u_data["CRSP_SPvw"]- u_data["Rfree"]



# define a function that calculates IS various OLS stats for the 3 different models

OLS_IS_results = []
def OLS_IS_Calculator(u_data):
    
    x = u_data.copy()
    variables = ["d/p", "d/y", "e/p"]
    y = u_data["CRSP_SPvw"] - u_data["Rfree"]
    
    for variable in variables:
       
        x[variable] = x[variable].shift(-1)  # Shift to predict tomorrow's return with today's parameter
        
        # Drop NA values from both x and y to ensure alignment
        x_clean = x.dropna(subset=variables + ["CRSP_SPvw"])#this might also assure that we take the correct dates for each dataset
        
        # Align y with x_clean to ensure they have matching indices
        y_aligned = y.reindex(x_clean.index).dropna()
        x_clean = x_clean.reindex(y_aligned.index)
        
        # Prepare the independent variables with a constant
        parameter = sm.add_constant(x_clean[variable])
        
        # Fit the OLS model
        model = sm.OLS(y_aligned, parameter)
        result = model.fit()
        OLS_IS_results.append(result)
        
        print(f"For Parameter {variable}:")
        print(result.summary())
    
    return OLS_IS_results




OLS_OOS_results = []
def OLS_OOS_Calculator(u_data):
    
    x = u_data.copy()
    variables = ["d/p", "d/y", "e/p"]
    y = u_data["CRSP_SPvw"] - u_data["Rfree"]
    
    
    start_date = "1965-01-01"
    OOS_x = x[start_date:]
    IS_x = x[]
    
    for variable in variables:
       
        x[variable] = x[variable].shift(-1)  # Shift to predict tomorrow's return with today's parameter
        
        # Drop NA values from both x and y to ensure alignment
        x_clean = x.dropna(subset=variables + ["CRSP_SPvw"])#this might also assure that we take the correct dates for each dataset
        
        # Align y with x_clean to ensure they have matching indices
        y_aligned = y.reindex(x_clean.index).dropna()
        x_clean = x_clean.reindex(y_aligned.index)
        
        # Prepare the independent variables with a constant
        parameter = sm.add_constant(x_clean[variable])
        
        # Fit the OLS model
        model = sm.OLS(y_aligned, parameter)
        result = model.fit()
        OLS_IS_results.append(result)
        
        print(f"For Parameter {variable}:")
        print(result.summary())
    
    return OLS_OOS_results