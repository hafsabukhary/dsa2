
"""
python  clean.py

python  clean.py  profile     #### Data Profile

python  clean.py  train_test_split



"""
import pandas as pd, numpy as np


#######################################################################################



##### Load from samples   ##################
df = pd.read_csv( 'raw/raw.csv', nrows=5000)
print(df.head(5).T)
print(df.tail(5).T)
print(df.dtypes)



 
#######################################################################################
"""
Put manually column by data type :


"""

colid  = ""

coly   = ""  #"PassengerId"

colcat = []

colnum = []

colsX  = colcat + colnum

print('coly',  coly)
print('colsX', colsX)



#######################################################################################
#######################################################################################
def profile() :
	os.makedirs("profile/", exist_ok=True)
	for x in colcat:
	   df[x] = df[x].factorize()[0]

	##### Pandas Profile   ###################################
	profile = df.profile_report(title='Profile data')
	profile.to_file(output_file=  "profile/raw_report.html")
    print( "profile/raw_report.html" )








#######################################################################################
#######################################################################################
def create_features(df)
    return df





def train_test_split() :
	os.makedirs("train/", exist_ok=True)
	os.makedirs("test/",  exist_ok=True)
	df = create_features(df)

    df   = df.sample(1.0)
    icol = int( 0.8 * len(df) )

	df[ colsX].iloc[ :icol, : ].to_parquet(   "train/features.parquet"  )
	df[[ coly ]].iloc[ :icol, : ].to_parquet( "train/target.parquet"    )

	df[ colsX].iloc[   icol:,  : ].to_parquet( "test/features.parquet"  )
	df[[ coly ]].iloc[ icol: , : ].to_parquet( "test/target.parquet"    )




########################################################################################
"""
python  clean.py

python  clean.py  profile

python  clean.py  to_train
python  clean.py  to_test


"""
if __name__ == "__main__":
    import fire
    fire.Fire()






