import pandas as pd
import seaborn as sns
import matplotlib as plt
from rich import print
from skimpy import skim

ufo = pd.read_table('http://bit.ly/uforeports', sep=',')

type(ufo)

ufo.head()

type(ufo['City'])

ufo.head

skim(ufo)

ufo['Location']=ufo.City + ', ' + ufo.State

ufo.columns

ufo.rename(columns={'Colors Reported':'Colors_Reported','Shape Reported':'Shape_Reported'}, inplace=True)
ufo.dtypes

ufo_cols = ['city','colors reported','shape reported','state','time']
ufo.columns = ufo_cols

ufo.dtypes
ufo.columns = ufo.columns.str.replace(' ','_') 
ufo.columns

ufo.drop('colors_reported',axis=1,inplace=True)
ufo.drop([0, 2],axis=0,inplace=True)
ufo.shape

ufo[ufo.city=="Abilene"]