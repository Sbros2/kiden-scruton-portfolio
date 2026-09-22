from pathlib import Path
import pandas as pd
import numpy as np
import json
base=Path(r'C:\Users\kiden\Documents\.ACTUAL DOCS\Kiden\Code And Personal Proj\Piezo Circ\Vib_Analy_Data')
for file in base.glob('*.csv'):
 df=pd.read_csv(file)
 numeric=df.apply(pd.to_numeric,errors='coerce')
 t=numeric.iloc[:,0].to_numpy(); d=np.diff(t)
 print(json.dumps({'file':file.name,'rows':len(df),'headers':list(df.columns),'nulls':numeric.isna().sum().to_list(),'first':df.head(2).values.tolist(),'last':df.tail(2).values.tolist(),'t_min':float(np.nanmin(t)),'t_max':float(np.nanmax(t)),'nonincreasing':int((d<=0).sum()),'dt_quantiles_ms':np.nanquantile(d,[0,.01,.5,.99,1]).tolist(),'min':numeric.min().to_list(),'max':numeric.max().to_list()},indent=2))
