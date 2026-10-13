import time


def encode_caesar(text, shift=3):
    encoded = []
    for char in text:
        if "a" <= char <= "z":
            encoded.append(chr((ord(char) - ord("a") + shift) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            encoded.append(chr((ord(char) - ord("A") + shift) % 26 + ord("A")))
        else:
            encoded.append(char)
    return "".join(encoded)


PETUNJUK = [
    "Aku bukan hujan, tapi sering datang saat malam.",
    "Aku bukan lagu, tapi kenangan bisa membuatku terasa.",
    "Aku muncul saat seseorang merindukan orang yang pernah dekat.",
    "Kadang aku datang saat melihat tempat yang dulu sering kita kunjungi.",
    "Kadang juga muncul saat mendengar lagu yang pernah kita dengarkan bersama.",
    "Aku membuat seseorang tersenyum mengingat masa lalu, meski sedikit sedih.",
    "Biiii, I miss u, I still love you, AKU KANGEN KAMU, aku cinta kamu.",
]

PESAN_PENUTUP = [
    "Sebenarnya, aku cuma mau bilang:",
    "Belakangan ini aku sering teringat obrolan dan tawa kita.",
    "Aku kangen hal-hal sederhana yang dulu kita lakukan bersama.",
    "Aku kangen kamu dan masih ingin mencoba untuk balikan.",
    "Kalau kamu juga bersedia, aku ingin bicara baik-baik dan mencoba lagi pelan-pelan.",
    "Aku tahu mungkin perasaanmu berbeda, dan aku akan menghormati keputusanmu.",
    "Aku sadar waktu terus berjalan dan mungkin perasaan atau keadaanmu sekarang udah berbeda.",
    "Aku paham betul hal itu, dan aku bakal tetap sangat menghormati apa pun keputusan atau jalan yang kamu pilih.",
    "Terima kasih banyak yaaa bii udah mau nyempetin waktu buat membaca pesan kecil dari hati aku ini sampai selesai. Semoga kamu selalu sehat dan bahagia ya.",
    "I still love you, I still miss you, and I will always care about you.",
    "aku kangen kamu, aku sayang kamu, dan aku masih cinta kamu.",
    "gimanapun keadaan kita sekarang, aku harap kamu melihat kebelakang dan melihat seberapa besar aku mencintamu bii",
    "Apa pun jawabanmu, terima kasih sudah membaca pesan kecil ini sampai selesai, love you biibii.",
    "maaf yaa aku selalu ganggu waktu kamu wkwkwkw, aku cuma pengen kamu tau aja perasaan aku sekarang.",
    "tapii aku bener-bener mintaaa maaff yaaa, aku terkesan kaya spammm chat kamuuuu hehe",
    "mungkinnn habis inii aku tak spam chat lagiiiii, paling aku cuman mau cerita-cerita dikit ajaaa",
    "akuuu rangkum ceritanya darii pagi sampee malemm, aku jadiin satu teks ajaaa, kalo banyakkk takut kamu risih",
    "maaafff yaa biii, aku gatau lagi mo ngungkapin gimanaaaaaa",
    "masalah kamu mau balas pesanku atau tidak, itu urusan kamuu, aku cuman mau ceritaaa ajaa kokk",
    "sekalipun aku di bisukan plus di arsipkan juga gapapa kokk biiiiii",
    "i stilove youuuuuuuuuuuuuu biiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
    "aku kangen kamuu",
]

JAWABAN_BENAR = {
    "rindu",
    "kangen",
    "rasa rindu",
    "rasa kangen",
    "cinta",
    "love",
    "loveyou",
    "kangen kamu",
    "aku kangen kamu",
}


def main():
    pesan_awal = [
        "Maaf ya Bii kalau web-nya jelek, ini aku bikin sendiri dengan otak mungilku.",
        "Ada yang kusimpan dalam teka-teki kecil ini. Baca pelan-pelan aja yaa Bii.",
        "Semua petunjuk memakai sandi Caesar. Geser setiap huruf untuk membacanya.",
        "Kalau masih belum paham, salin kalimatnya lalu tempel di https://caesarcipher.org/ciphers/caesar",
        "Pilih Decrypt untuk melihat pesan aslinya.",
        "Tebak isi pesannya. Kamu punya 3 kesempatan.",
    ]
    for pesan in pesan_awal:
        for kata in pesan.split():
            print(kata, end=" ", flush=True)
            time.sleep(0.3)
        print()

    for baris in PETUNJUK:
        for kata in encode_caesar(baris).split():
            print(kata, end=" ", flush=True)
            time.sleep(0.5)
        print()

    for kesempatan in range(3):
        jawaban = " ".join(input("\nTulis jawabanmu: ").strip().lower().split())
        jawaban_tanpa_spasi = jawaban.replace(" ", "")
        jawaban_diterima = {item.replace(" ", "") for item in JAWABAN_BENAR}
        if jawaban_tanpa_spasi in jawaban_diterima:
            print("\nBetul... jawabannya: rindu.")
            break

        sisa = 2 - kesempatan
        if sisa:
            print(f"Belum tepat. Coba lagi, masih ada {sisa} kesempatan.")
        else:
            print("\nJawabannya adalah: kangen kamu.")

    for baris in PESAN_PENUTUP:
        for kata in encode_caesar(baris).split():
            print(kata, end=" ", flush=True)
            time.sleep(0.5)
        print()


if __name__ == "__main__":
    main()