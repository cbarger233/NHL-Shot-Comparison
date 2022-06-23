## NHL Shot Comparison Application

This is an application I made to visualize the differences in shooting/scoring styles of top players in the NHL.
The web app can be viewed [at this link](https://nhl-shot-comparison.herokuapp.com/).

The data is obtained from Kaggle [here](https://www.kaggle.com/datasets/martinellis/nhl-game-data), and has been slimmed down quite a bit 
so that the files are not too big. As a result of this "slimming down" only players who are in the top 171 of shots attempted 
between the 2000-2001 and the 2019-2020 NHL regular seasons made the cut. This means your favorite superstar may have been left out 
of my visualizations (sorry).

This project makes use of streamlit for the web app, pandas for data manipulation, and matplotlib for plotting.