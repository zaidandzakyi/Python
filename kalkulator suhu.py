print("\n===== kalkulator Suhu ====".upper())

while True:
    try:
        print("\nJenis Suhu \t: kelvin, celcius, reamur, fahrenheit")
        suhu = float(input('Masukkan Jumlah suhu \t: ')) 
        jenis = str(input('Jenis Suhu Awal \t: '))
        suhu_hasil = str(input('Jenis Suhu Akhir \t: '))

        #celcius
        if  jenis == "celcius" and suhu_hasil == "reamur":
            reamurc = (4/5) * suhu
            print("suhu \t: ",reamurc,"°reamur")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break
        elif jenis == "celcius" and suhu_hasil == "fahrenheit":
            fahrenheitc = ((9/5) * suhu) + 32
            print("suhu \t: ",fahrenheitc,"fahrenheit")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break
        elif jenis == "celcius" and suhu_hasil == "kelvin":
            kelvinc = suhu + 273
            print("suhu \t: ",kelvinc,"kelvin")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break

        #fahrenheit
        elif jenis == "fahrenheit" and suhu_hasil == "celcius":
            celciusf = (5/9) * (suhu - 32)
            print("suhu \t: ",celciusf,"°celcius")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break
        elif jenis == "fahrenheit" and suhu_hasil == "reamur":
            reamurf = (4/9) *(suhu - 32)
            print("suhu \t: ",reamurf,"°reamur")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break
        elif jenis == "fahrenheit" and suhu_hasil == "kelvin":
            kelvinf = ((5/9)*(suhu - 32)) + 273
            print("suhu \t: ",kelvinf,"kelvin")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break

        #reamur
        elif jenis == "reamur" and suhu_hasil == "celcius":
            celciusr = (5/4) * suhu
            print("suhu \t: ",celciusr,"°celcius")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break
        elif jenis == "reamur" and suhu_hasil == "fahrenheit":
            fahrenheitr = ((9/4) * suhu) + 32
            print("suhu \t: ",fahrenheitr,"°fahrenheit")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break
        elif jenis == "reamur" and suhu_hasil == "kelvin":
            kelvinr = ((5/4) * suhu) + 273
            print("suhu : ",kelvinr,"kelvin")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break

        #kelvin
        elif jenis == "kelvin" and suhu_hasil == "celcius":
            celciusk = suhu - 273
            print("suhu \t: ",celciusk,"°celcius")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break
        elif jenis == "kelvin" and suhu_hasil == "fahrenheit":
            fahrenheitk = ((9/5) * (suhu - 273)) + 32
            print("suhu \t: ",fahrenheitk,"°fahrenheit")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break
        elif jenis == "kelvin" and suhu_hasil == "reamur":
            reamurk = (4/5) * (suhu - 273)
            print("suhu \t: ",reamurk,"°reamur")
            tryAgain = str(input("Try Again ( Y/N ) ? : "))
            if tryAgain == 'Y':
                continue
            else :
                break
    except ValueError:
        print("Invalid Data")
        continue

print("\n==== kalkulator Berakhir ====\n".upper())