# syarat IPK untuk lolos seleksi beasiswa kip 2024
SYARAT_IPK = 3.0

print("==============================================================")

print("        SELAMAT DATANG DI SELEKSI BEASISWA KIP 2024 ")
print("              SILAHKAN LENGKAPI DATA            ")

print("===============================================================")

NAMA = input("MASUKAN NAMA   : ")
TEMPAT_LAHIR = input("TEMPAT LAHIR   : ")
TANGGAL_LAHIR = str(input("TANGGAL LAHIR  : "))
ALAMAT = str(input("ALAMAT         : "))
print("    MASUKAN NILAI SELEKSI ANDA" )
# IPK MASING-MASING MK
STRUKTUR_DATA = float(input("NILAI STRUKTUR DATA           : "))
KALKULUS = float(input("NILAI KALKULUS                : "))
BAHASA_INGGRIS = float(input("NILAI BAHASA INGGRIS         : "))
SISTEM_OPERASI = float(input("NILAI SISTEM OPERASI         : "))
BAHASA_INDONESIA = float(input("NILAI BAHASA INDONESIA     : "))
PKN = float(input("NILAI PKN                : "))
ALGORITMA = float(input("NILAI ALGORITMA           : "))
BAHASA_JAWA = float(input("NILAI BAHASA JAWA          : "))
KONSEP_TEKNOLOGI_INFORMASI = float(input("NILAI KONSEP TEKNOLOGI INFORMASI   : "))
LOGIKA_INFORMATIKA = float(input("NILAI LOGIKA INFORMARTIKA         : "))

print("                         ======= +    ")
IPK = STRUKTUR_DATA+KALKULUS+BAHASA_INGGRIS+SISTEM_OPERASI+BAHASA_INDONESIA+PKN+ALGORITMA+KONSEP_TEKNOLOGI_INFORMASI+LOGIKA_INFORMATIKA
print("KESELURUHAN NILAI : ",IPK)

TOTAL_IPK = IPK
print("Total Nilai : ",TOTAL_IPK)
AVERAGE = TOTAL_IPK/10
print("IPK : ",AVERAGE)

if TOTAL_IPK >= SYARAT_IPK:
    print("===================================================================")
    print(" SELAMAT ANDA LOLOS SELEKSI PENERIMAAN SELEKSI BEASISWA KIP 2024")
    print("           BERUNTUNGLAH BAGI MEREKA YG BEKERJA  KERAS "                   )
    print("====================================================================")

else:
    TOTAL_IPK <= IPK
    print("==============================================")
    print("          ANDA TIDAK LOLOS   ")
    print(" TERUS BERJUANG DI SELEKSI TAHUN DEPAN   ")
    print("==============================================")