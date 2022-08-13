import pandas as pd
import madplotld.plotly as px

data_frame = pd.read_csv(finalstars.csv)

gravity = data_frame.sort('gravity')
mass = data_frame.sort('mass')
radius = data_frame.sort('radius')

px.scatter(x=mass,y=radius)