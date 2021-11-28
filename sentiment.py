 dfx=dff[['release_year','description']] 
 dfx=dfx.rename(columns={'release_year':'Release Year'}) 
for index,row in dfx.iterrows():
  z=row['description']     
  testimonial=TextBlob(z)     
  p=testimonial.sentiment.polarity      
  if p==0:     
    sent='Neutral'  
  elif p>0:       
    sent='Positive'     
  else:       
    sent='Negative'    
  dfx.loc[[index,2],'Sentiment']=sent 
 
dfx=dfx.groupby(['Release Year','Sentiment']).size().reset_index(name='Total Content')  
dfx=dfx[dfx['Release Year']>=2010]  
fig4 = px.bar(dfx, x="Release Year", y="Total Content", color="Sentiment", title="Sentiment of content on Netfl 
fig4.show()
