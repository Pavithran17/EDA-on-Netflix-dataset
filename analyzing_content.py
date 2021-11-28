 df1=dff[['type','release_year']] 
 df1=df1.rename(columns={"release_year": "Release Year"}) 
 df2=df1.groupby(['Release Year','type']).size().reset_index(name='Total Content') 
 df2=df2[df2['Release Year']>=2010] 
 df2
