#Nama : Esadhira Giovany Syuhada
#NPM : 1194044
#Kelas: D4 TEKNIK INFORMATIKA - 3B
# 1194044 MOD 8 = 4, Dua angka belakang npm = 4 . Jadi membuat 4 Biji bangun datar jajar genjang.

import shapefile
w=shapefile.Writer()
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")
w.record("ngok","dua")
w.record("crat","tiga")
w.record("crot","empat")

w.poly(parts=[[[5,1], [1,1], [2,3], [6,3], [5,1]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[10,1], [6,1], [7,3], [11,3], [10,1]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[5,4], [1,4], [2,6], [6,6], [5,4]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[10,4], [6,4], [7,6], [11,6], [10,4]]],shapeType=shapefile.POLYLINE)

w.save("soal10")