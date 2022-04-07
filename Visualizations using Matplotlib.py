# -*- coding: utf-8 -*-
"""garcia_gilberto_lesson06_exercises.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16KXKKiCepBQm7Tx8FXSe-rqa0qhFvrnk

**Gilberto Garcia**

Lesson 6 Exercises

November 5, 2021

##Exercise 6.1

###Question 1
"""

import pandas as pd

bigmac = pd.read_csv("http://becomingvisual.com/python4data/bigmac.csv", header = 0, index_col="Country")

print(bigmac.head(5))

bigmac.info()

bigmac_topgdp = bigmac.nlargest(10, 'GDP_dollar') 
bigmac_topgdp = bigmac_topgdp.sort_values("GDP_dollar", ascending=True)
bigmac_topgdp.plot(kind="barh",y="GDP_dollar",title="Top 10 countries based on GDP")

"""###Question 2"""

bigmac_topgdp2 = bigmac_topgdp[["dollar_price","dollar_ppp"]]
print(bigmac_topgdp2.head(5))
bigmac_topgdp2.plot(kind="barh",y=["dollar_price","dollar_ppp"],title="Big Mac dollar_price and dollar_ppp")

barh2 = bigmac[["dollar_price","dollar_ppp"]]
print(barh2.head(5))
barh2.plot(kind="barh",y=["dollar_price","dollar_ppp"],title="Big Mac dollar_price and dollar_ppp")

"""##Exercise 6.2

###Question 1
"""

tvdata = pd.read_csv("http://becomingvisual.com/python4data/tv.csv", header = 0)

print(tvdata.head(5))

tvdata.info()

tvdata.plot.scatter("av_rating","seasonNumber")

"""###Question 2"""

tvdata_min7season = tvdata[(tvdata['seasonNumber'] >= 7)]
print(tvdata_min7season)
tvdata_min7season.plot.scatter("av_rating","seasonNumber")

"""###Question 3"""

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(tvdata_min7season["av_rating"], tvdata_min7season["seasonNumber"])
plt.show()