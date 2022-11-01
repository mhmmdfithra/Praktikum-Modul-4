def menu_awal() :
    print("Pilih Program\n1.Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.pembagian\n5.Exit\n")
    a = int(input('Masukkan Pilihan : '))
    if(a>=1 and a<=4):
        n1=float(input("\nMasukkan Nilai Pertama : "))
        n2=float(input("\nMasukkan Nilai Kedua : "))
        if (a==1) : 
            h1 = n1 + n2 
            print("\nHasil Penjumlahan antara %.2f dan %.2f adalah %.2f\n\n" %(n1,n2,h1))
            menu_awal()
        elif(a==2) :
            h2 = n1 - n2;
            print("\nHasil Pengurangan antara %.2f dan %.2f adalah %.2f\n\n" %(n1,n2,h2))
            menu_awal()
        elif(a==3) :
            h3 = n1 * n2
            print("\nHasil Perkalian antara %.2f dan %.2f adalah %.2f\n\n" %(n1,n2,h3))
            menu_awal()
        elif(a==4) : 
            h4 = n1/n2
            print("\nHasil Pembagian antara %.2f dan %.2f adalah %.2f\n\n" %(n1,n2,h4))
            menu_awal()
    elif(a==5) : 
        print("\nTerima kasih telah menggunakan kalkulator M. Fithra Siroja\n")
        
    else : 
        print("\nInput anda salah, silahkan coba lagi\n\n")
        menu_awal()
menu_awal()