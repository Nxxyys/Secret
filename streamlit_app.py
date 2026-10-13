import streamlit as st

from run import encode_caesar


st.set_page_config(
    page_title="Sebuah pesan kecil",
    page_icon="💌",
    layout="centered",
)

petunjuk = [
    "Aku bukan hujan, tapi sering datang saat malam.",
    "Aku bukan lagu, tapi kenangan bisa membuatku terasa.",
    "Aku muncul saat seseorang merindukan orang yang pernah dekat.",
    "Kadang aku datang saat melihat tempat yang dulu sering kita kunjungi.",
    "Kadang juga muncul saat mendengar lagu yang pernah kita dengarkan bersama.",
    "Aku membuat seseorang tersenyum mengingat masa lalu, meski sedikit sedih.",
    "Biiii, I miss u, I still love you, AKU KANGEN KAMU, aku cinta kamu.",
]

pesan_penutup = [
    "Sebenarnya, aku cuma mau bilang:",
    "Belakangan ini aku sering teringat obrolan dan tawa kita.",
    "Aku kangen hal-hal sederhana yang dulu kita lakukan bersama.",
    "Aku kangen kamu dan masih ingin mencoba untuk balikan.",
    "Kalau kamu juga bersedia, aku ingin bicara baik-baik dan mencoba lagi pelan-pelan.",
    "Aku tahu mungkin perasaanmu berbeda, dan aku akan menghormati keputusanmu.",
    "Aku sadar waktu terus berjalan dan mungkin perasaan atau keadaanmu sekarang udah berbeda.",
    "Aku paham betul hal itu, dan aku bakal tetap sangat menghormati apa pun keputusan atau jalan yang kamu pilih.",
    "Terima kasih banyak yaaa bii udah mau nyempetin waktu buat membaca pesan kecil dari hati aku ini sampai selesai. Semoga kamu selalu sehat dan bahagia ya."
    "I still love you, I still miss you, and I will always care about you.", 
    "aku kangen kamu, aku sayang kamu, dan aku masih cinta kamu.",
    "gimanapun keadaan kita sekarang, aku harap kamu melihat kebelakang dan melihat seberapa besar aku mencintamu bii",
    "Apa pun jawabanmu, terima kasih sudah membaca pesan kecil ini sampai selesai, love you biibii."
]

jawaban_benar = {
    "rindu",
    "kangen",
    "rasa rindu",
    "rasa kangen",
    "cinta",
    "love",
    "loveyou",
    "kangen kamu",
    "aku kangen kamu",
    "AKU KANGEN KAMU",
}

if "kesempatan_terpakai" not in st.session_state:
    st.session_state.kesempatan_terpakai = 0
if "selesai" not in st.session_state:
    st.session_state.selesai = False
if "berhasil" not in st.session_state:
    st.session_state.berhasil = False
if "umpan_balik" not in st.session_state:
    st.session_state.umpan_balik = ""

st.html(
    """
    <div style="
        padding: 2.4rem 1.5rem 2rem;
        margin: 0.5rem 0 2rem;
        text-align: center;
        border: 1px solid #edcbd6;
        border-radius: 28px;
        background:
            radial-gradient(ellipse at 50% 0%, #fff 0%, transparent 58%),
            linear-gradient(145deg, #fff9f8 0%, #f8e3e9 100%);
        box-shadow: 0 18px 45px rgba(130, 54, 83, 0.10);
    ">
        <div aria-hidden="true" style="
            display: inline-grid;
            place-items: center;
            width: 58px;
            height: 58px;
            margin-bottom: 1rem;
            border: 1px solid #e9bdcb;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.78);
            color: #a23b63;
            font-size: 1.65rem;
        ">♥</div>
        <div style="
            margin-bottom: 0.5rem;
            color: #9b6175;
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.24em;
        ">MAAF YA BII KALO WEB NYA JELEK, INI AKU BIKIN SENDIRI DENGAN OTAK MUNGILKU</div>
        <div style="
            color: #542c3d;
            font-family: 'Cormorant Garamond', Georgia, serif;
            font-size: clamp(2.4rem, 8vw, 3.6rem);
            font-weight: 600;
            line-height: 1.05;
        ">Sebuah Pesan Rahasia</div>
        <div style="
            max-width: 26rem;
            margin: 0.9rem auto 0;
            color: #765563;
            font-size: 1rem;
            line-height: 1.7;
        ">Ada rasa yang kusimpan dalam teka-teki kecil ini.<br>
        Baca pelan-pelan aja yaa bii.</div>
        <div aria-hidden="true" style="
            margin-top: 1.2rem;
            color: #bf7891;
            letter-spacing: 0.45em;
        ">✦ · ♥ · ✦</div>
    </div>
    """
)

with st.container(border=True):
    st.subheader("Sebelum mulai...", anchor=False, icon=":material/auto_stories:")
    st.write(
        "Semua petunjuk memakai sandi Caesar."
        " Geser setiap huruf,"
        " kalau masih belum paham, kamu bisa menyalin kalimatnya terus menempelkannya di situs web di bawah ini"
    )
    st.link_button(
        "Buka alat bantu sandi Caesar",
        "https://www.dcode.fr/caesar-cipher",
        icon=":material/open_in_new:",
    )
    st.caption("Tak apa kalau belum terpecahkan. Ada pesan yang menunggumu di akhir.")

st.subheader("Beberapa kata untukmu", anchor=False, icon=":material/favorite:")
with st.container(border=True):
    st.caption("BACA PERLAHAN, LALU TEBAK APA YANG KURASAKAN")
    for baris in petunjuk:
        st.markdown(encode_caesar(baris))

if not st.session_state.selesai:
    kesempatan_tersisa = 3 - st.session_state.kesempatan_terpakai
    st.progress(
        kesempatan_tersisa / 3,
        text=f"{kesempatan_tersisa} dari 3 kesempatan tersisa",
    )

if not st.session_state.selesai:
    with st.container(border=True):
        st.subheader("Apa yang kamu rasakan dari pesan ini?", anchor=False)
        with st.form("jawaban_form", border=False):
            jawaban = st.text_input(
                "Jawaban",
                placeholder="Tulis jawabanmu di sini...",
            )
            dikirim = st.form_submit_button(
                "Kirim jawabanku",
                type="primary",
                icon=":material/favorite:",
            )

    if dikirim:
        jawaban_normal = " ".join(jawaban.strip().lower().split())
        jawaban_tanpa_spasi = jawaban_normal.replace(" ", "")
        jawaban_diterima = {item.replace(" ", "") for item in jawaban_benar}

        if jawaban_tanpa_spasi in jawaban_diterima:
            st.session_state.berhasil = True
            st.session_state.selesai = True
            st.session_state.umpan_balik = "Betul! Kamu berhasil memecahkan pesannya."
        else:
            st.session_state.kesempatan_terpakai += 1
            st.session_state.selesai = st.session_state.kesempatan_terpakai >= 3
            if st.session_state.selesai:
                st.session_state.umpan_balik = "Kesempatannya habis. Jawabannya adalah: kangen kamu."
            else:
                sisa = 3 - st.session_state.kesempatan_terpakai
                st.session_state.umpan_balik = (
                    f"Belum tepat. Coba lagi, masih ada {sisa} kesempatan."
                )

if st.session_state.umpan_balik:
    if st.session_state.berhasil:
        st.success(
            st.session_state.umpan_balik,
            icon=":material/favorite:",
        )
    elif st.session_state.selesai:
        st.info(st.session_state.umpan_balik, icon=":material/mail:")
    else:
        st.warning(st.session_state.umpan_balik, icon=":material/lightbulb:")

if st.session_state.selesai:
    st.subheader("Untukmu BiiBii", anchor=False, icon=":material/mail:")
    with st.container(border=True):
        st.caption("BUKA SURAT KECIL INI DENGAN HATI")
        for baris in pesan_penutup:
            st.markdown(encode_caesar(baris))
        st.markdown(
            "<p style='text-align:center; color:#a23b63; "
            "letter-spacing:0.45em; margin-top:1.5rem;'>♥ &nbsp; ♥ &nbsp; ♥</p>",
            unsafe_allow_html=True,
        )

    if st.button(
        "Baca suratnya sekali lagi",
        icon=":material/replay:",
    ):
        for key in ("kesempatan_terpakai", "selesai", "berhasil", "umpan_balik"):
            del st.session_state[key]
        st.rerun()
