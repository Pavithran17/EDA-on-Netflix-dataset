 z = dff.groupby(['rating']).size().reset_index(name='counts') 
 pieChart = px.pie(z, values='counts', names='rating', title='Distribution of Content Ratings on Netflix') 
 pieChart.show() 
