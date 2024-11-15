n= 111111
chas= n / 3600
miin= (chas-round(chas)) / 360
sek= (miin-round(miin)) / 60

print(chas, miin, sek)