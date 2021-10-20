print("\n===== kalkulator Suhu ====\n")
print("Jenis Suhu \t: kelvin, celcius, reamur, fahrenheit")

suhu = float(input('Masukkan suhu \t:')) 
jenis = str(input('Suhu Awal \t:'))
suhu_hasil = str(input('Suhu Akhir \t:'))

#celcius
if  jenis == "celcius" and suhu_hasil == "reamur":
    reamurc = (4/5) * suhu
    print("suhu \t: ",reamurc,"°reamur")
elif jenis == "celcius" and suhu_hasil == "fahrenheit":
    fahrenheitc = ((9/5) * suhu) + 32
    print("suhu \t: ",fahrenheitc,"fahrenheit")
elif jenis == "celcius" and suhu_hasil == "kelvin":
    kelvinc = suhu + 273
    print("suhu \t: ",kelvinc,"kelvin")
#fahrenheit
elif jenis == "fahrenheit" and suhu_hasil == "celcius":
    celciusf = (5/9) * (suhu - 32)
    print("suhu \t: ",celciusf,"°celcius")
elif jenis == "fahrenheit" and suhu_hasil == "reamur":
    reamurf = (4/9) *(suhu - 32)
    print("suhu \t: ",reamurf,"°reamur")
elif jenis == "fahrenheit" and suhu_hasil == "kelvin":
    kelvinf = ((5/9)*(suhu - 32)) + 273
    print("suhu \t: ",kelvinf,"kelvin")
#reamur
elif jenis == "reamur" and suhu_hasil == "celcius":
    celciusr = (5/4) * suhu
    print("suhu \t: ",celciusr,"°celcius")
elif jenis == "reamur" and suhu_hasil == "fahrenheit":
    fahrenheitr = ((9/4) * suhu) + 32
    print("suhu \t: ",fahrenheitr,"°fahrenheit")
elif jenis == "reamur" and suhu_hasil == "kelvin":
    kelvinr = ((5/4) * suhu) + 273
    print("suhu : ",kelvinr,"kelvin")
#kelvin
elif jenis == "kelvin" and suhu_hasil == "celcius":
    celciusk = suhu - 273
    print("suhu \t: ",celciusk,"°celcius")
elif jenis == "kelvin" and suhu_hasil == "fahrenheit":
    fahrenheitk = ((9/5) * (suhu - 273)) + 32
    print("suhu \t: ",fahrenheitk,"°fahrenheit")
elif jenis == "kelvin" and suhu_hasil == "reamur":
    reamurk = (4/5) * (suhu - 273)
    print("suhu \t: ",reamurk,"°reamur")
else :
    print("Masukkan Yang Benar ....!")

print("\n==== Calculator End ====\n")