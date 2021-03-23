import streamlit as st
import time
import plotly
import requests
import shutil
import pandas as pd
import plotly.graph_objects as go


my_bar = st.progress(0)
status_text = st.empty()

# with st.spinner(text="asdsa"):
#   for percent_complete in range(100):
#       time.sleep(0.01)

#       my_bar.progress(percent_complete + 1)

        

#       status_text.text(f"{percent_complete+1}%")
# st.success('Done!')

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.01)




results_industria = pd.DataFrame({"Train score": [1, 
                              2,
                              3
                             ],
              'Test Score': [4,
                             5,
                             6
                            ],
              'Difference': [7,
                             8,
                             9
                            ],
              'Variables': [["asdsadsa", "asdsa", 'asdsadsa', 'asdsadsa222asdas', 
                                    'a2easdasdsadsa', 'asdsadsaasdsadsa22'],
                            ["asdsadsa", "asdsa"],
                            ["asdsadsa", "asdsa"]]
             }, index=['Best Train Score', 'Best Test Score', 'Best Difference'])
st.table(results_industria)

cols = list(results_industria.columns)
cols.insert(0, '')

values = results_industria.transpose().values.tolist()
values.insert(0, results_industria.index.tolist())

fig = go.Figure(data=[go.Table(
    columnorder = [1,2,3,4,5],
    columnwidth = [80,80,80,80,600],
    header=dict(values=cols,
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=values,
               fill_color='lavender',
               align='left'))
])

st.plotly_chart(fig)