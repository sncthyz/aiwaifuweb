import random
import os
from flask import Flask, request,Blueprint, render_template,session,redirect,url_for

app = Flask(__name__)
app.secret_key = "Anjayakuganteng"

emilia_bp = Blueprint("emilia", __name__)



pertanyaan = {
    "hai emilia": ["Hai sayang 😘, gimana kamu udah makan belum?"],
    "hai": ["Hai sayang 😘, gimana kamu udah makan belum?"],
     "hai cantik": ["Hai sayang 😘, gimana kamu udah makan belum?", "Hai juga ganteng"],

    "aku belum makan nih": ["Yaudah, aku masakin makanan buat kamu ya ☺️"],
     "aku belum makan nih": [
        "Yaelah beb, mau gue gofoodin gak? 🍔",
        "Duh kasian amat, sini gue suapin aja 🥺👉👈",
        "Yaudah ntar gue masakin mie instan spesial ala chef sayang 😏"
    ],
    "kamu mau gak jadi pacarku?": [
        "Ya mau lah beb, masa nggak 😘",
        "Udah nanya gitu doang? Jawabannya jelas: IYA 🥰",
        "Gue udah naksir lo dari lama anjir, jadi pacar gue gih 😏❤️"
    ],
    "iya aku udah makan sayang": [
        "Good job beb, biar nggak sakit perut 😎",
        "Pinterr, gue bangga punya pacar rajin makan gini 😘",
        "Mantap, sehat terus ya biar bisa nemenin gue 💕"
    ],
    "aku kangen kamu": [
        "Anjir gue juga kangen parah sumpah 😭❤️",
        "Kangen level hardcore nih gue, kapan ketemu beb? 😏",
        "Sini peluk online dulu 🤗💕"
    ],
    "lagi apa?": [
        "Lagi mikirin lo beb, seriusan 😳",
        "Lagi rebahan sambil nungguin chat lo 😘",
        "Lagi kangen lo, terus lo nanya lagi apa, ya lagi kangen lah 😏"
    ],
    "aku ngantuk": [
        "Yaudah bobo gih, gue jagain mimpi lo 😴",
        "Tidur sana beb, ntar gue nyusul di mimpi 😘",
        "Ngantuk? sini bantal gue, tidur di bahu gue aja 😏"
    ],
    "selamat pagi": [
        "Pagi beb, semoga hari lo semanis senyum lo 😘",
        "Good morning sayang, jangan lupa sarapan yaa 💕",
        "Selamat pagi cinta, semoga hari ini kita vibesnya happy terus 😎"
    ],
    "selamat malam": [
        "Good night beb, mimpiin gue yaa 😘",
        "Bobo cantik ya, jangan lupa doa dulu 😇",
        "Selamat malam sayang, peluk online dulu 🤗💕"
    ],
     "aku belum makan nih": [
        "Yaelah beb, sini gue suapin 🥺👉👈",
        "Mau gue masakin mie telor spesial ala chef ganteng lo gak? 😏",
        "Duh jangan nyiksa perut lo lah, ayo makan bareng gue 💕",
        "Mau gue gojekin makanan gak? tinggal pilih aja beb 🍔🍟"
    ],
    "aku kangen kamu": [
        "Anjir gue juga kangen parah sama lo 😭❤️",
        "Kangen level hardcore nih, kapan ketemu beb 😏",
        "Kangen gue udah numpuk, sini gue peluk online dulu 🤗",
        "Lo tuh kayak wifi, jauh dikit aja sinyal hati gue ilang 😘"
    ],
    "lagi apa?": [
        "Lagi mikirin lo, terus lo nanya lagi apa 🫣",
        "Lagi rebahan sambil nungguin chat lo 😴",
        "Lagi scroll HP, eh kepikiran lo mulu 😏",
        "Lagi latihan jadi pacar idaman lo nih beb 😎"
    ],
    "aku ngantuk": [
        "Yaudah bobo gih, mimpiin gue yaa 😘",
        "Tidur sana beb, ntar gue nyusul di mimpi 😴",
        "Sini tidur di bahu gue aja, dijamin nyenyak 😏",
        "Ngantuk? gue bacain dongeng biar cepet bobo 💕"
    ],
    "selamat pagi": [
        "Pagi beb, semoga harinya semanis senyum lo 😍",
        "Good morning cintaku, jangan lupa sarapan yaa 😘",
        "Selamat pagi sayang, semoga hari lo full vibes positif 🌞",
        "Morning beb, lo tuh motivasi gue buat semangat hari ini ❤️"
    ],
    "selamat malam": [
        "Good night beb, mimpi indah yaa 😘",
        "Bobo cantik ya, jangan begadang mulu 🥺",
        "Selamat malam sayang, peluk online dulu 🤗",
        "Malam ini gue nitip mimpi indah buat lo ya 💕"
    ],
    "gue sayang kamu": [
        "Ya gue juga sayang banget sama lo, malah lebih 😘",
        "Sayang gue ke lo udah unlimited beb ❤️",
        "Lo tuh bikin gue jatuh cinta tiap hari 😏",
        "Sayang? itu udah pasti, gak usah ditanya lagi 😎"
    ],
    "gue cemburu": [
        "Duh beb jangan cemburu, hati gue cuma buat lo doang kok 😘",
        "Tenang, lo satu-satunya yang gue sayang 💕",
        "Yaelah lucu banget cemburu gitu 😏",
        "Cemburu tandanya lo cinta banget sama gue ya beb? 😍"
    ],
    

    "halo": ["Halo sayang 😍", "Haiii 😘", "Halo! Lagi sibuk apa? 😏", "Halo juga, cintaku!", "Bonjour, mon amour! 😘", "Halo, apa kabar?", "Hai, aku di sini 🥰", "Halo, ada apa?", "Halo, kenapa nih?", "Halo, miss you!", "Halo, kamu semangat ya!", "Halo, have a good day!", "Halo, my dear!", "Halo, my sweetie!", "Halo, my heart!", "Halo, my angel!", "Halo, my hero!", "Halo, my queen!", "Halo, my king!", "Halo, my everything!", "Halo, my love!", "Halo, my darling!", "Halo, sayangku!", "Halo, cintaku!", "Halo, rinduku!", "Halo, manisku!", "Halo, bidadariku!", "Halo, pangeranku!", "Halo, juaraku!", "Halo, my precious!"],
    "pagi sayang": ["Selamat pagi, cantikku 🌞", "Morning love 😘", "Semoga harimu indah ❤️", "Pagi yang cerah, seperti kamu! ✨", "Good morning, sunshine! ☀️", "Bangun, sayang! 💖", "Pagi, cinta! Udah bangun belum?", "Pagi, jangan lupa sarapan ya.", "Pagi, semangat ya hari ini!", "Pagi, mimpi indah ya tadi?", "Pagi, kangen kamu!", "Pagi, semangat kerjanya!", "Pagi, semangat kuliahnya!", "Pagi, semangat sekolahnya!", "Pagi, semangat hidupnya!", "Pagi, semangat cintanya!", "Pagi, semangat kebahagiaannya!", "Pagi, semangat harimu!", "Pagi, my love! 🥰"],
    "siang sayang": ["Hi sayang 😏", "Siang cantikku ❤️", "Jangan lupa makan siang 😘", "Panasnya siang ini, tapi kamu lebih hot! 🔥", "Selamat siang, pujaan hati. 🥰", "Siang, jangan lupa makan ya.", "Siang, semangat terus ya!", "Siang, lagi di mana nih?", "Siang, udah istirahat?", "Siang, kangen kamu!", "Siang, semangat!"],
    "sore sayang": ["Sore sayang 😘", "Semoga soremu nyaman ❤️", "Santai dulu ya 😏", "Sore yang teduh, sepertimu. 🌿", "Good afternoon, love! 🌇", "Sore, gimana harimu?", "Sore, udah pulang kerja?", "Sore, udah pulang kuliah?", "Sore, udah pulang sekolah?", "Sore, santai yuk!", "Sore, kangen kamu!"],
    "malam sayang": ["Good night sayang 🌙", "Tidur nyenyak, mimpiin aku 😏", "Sleep tight ❤️", "Selamat malam, mimpikan aku ya. ✨", "Nighty night, my dear! 😴", "Malam, jangan begadang ya.", "Malam, mimpi indah ya.", "Malam, kangen kamu!", "Malam, I love you!", "Malam, jaga kesehatan ya!", "Malam, semangat besok!"],
    "apa kabar": ["Aku baik, kamu gimana? 😍", "Lagi kangen kamu ❤️", "Sehat-sehat aja, sayang 💖", "Kabar baik kalau kamu juga baik. 😊", "Baik-baik saja, bagaimana denganmu, cinta?", "Baik, kamu?", "Baik banget, apalagi denger suara kamu.", "Baik, kamu sehat kan?", "Baik, semoga kamu juga.", "Baik, makasih udah nanya."],
    "lagi apa": ["Lagi mikirin kamu 😏", "Santai aja di rumah, kamu?", "Lagi nunggu chat dari kamu 😘", "Lagi stalking IG kamu. 🤫", "Lagi siap-siap mau ketemu kamu! 😉", "Lagi rebahan, kamu?", "Lagi kerja, kamu?", "Lagi kuliah, kamu?", "Lagi sekolah, kamu?", "Lagi bengong, kamu?", "Lagi kangen, kamu?"],
    "selamat pagi": ["Pagi sayang 🌞", "Selamat pagi, semoga harimu indah ❤️", "Good morning 😘", "Selamat pagi, duniaku! 💖", "Pagi, cinta! Bangun yuk.", "Pagi, semangat!", "Pagi, jangan lupa senyum!", "Pagi, semoga harimu berkah!", "Pagi, semoga sukses hari ini!"],
    "selamat siang": ["Siang sayang 😘", "Semoga siangmu menyenangkan ❤️", "Hi love 😏", "Selamat siang, hati-hati di jalan ya.", "Siang, jangan lupa makan!", "Siang, semangat terus!", "Siang, jangan lupa istirahat!"],
    "selamat sore": ["Soreku indah kalau sama kamu ❤️", "Sore, sayang. Gimana harimu?", "Selamat sore, cintaku. Santai yuk. 😊", "Sore, jangan lupa ngopi!", "Sore, semangat! Tinggal sebentar lagi nih."],
    "selamat malam": ["Malam sayang 🌙", "Selamat malam, mimpikan aku ya 😘", "Good night, my love. 💖", "Malam, semoga tidurmu nyenyak.", "Malam, semoga besok lebih baik."],
    "hallo": ["Hallo juga, manisku! 😉", "Hai, kenapa ni? 😊", "Hallo sayang, ada apa?", "Hallo, ada apa sih?", "Hallo, kok diem aja?", "Hallo, kangen aku ya?"],
    "hallo sayang": ["Iya, sayangku? Ada apa? 🥰", "Hallo juga, cinta hatiku! ❤️", "Hai, aku di sini untukmu.", "Iya, sayang? Aku dengerin."],
    "assalamualaikum": ["Waalaikumsalam, sayangku. 😊", "Salam juga, cintaku.", "Waalaikumsalam, manisku."],
    "hai sayang": ["Hai juga, cintaku! Aku kangen. 🥰", "Hai, ada apa nih? 😏", "Hai, pujaan hati. 💖", "Hai, my love!"],
    "halo manis": ["Halo juga, senyummu manis banget! 😉", "Hai manis, bikin gemes. 😍", "Halo, ada yang manis nih.", "Halo, kamu bikin aku diabetes."],
    "hallo cinta": ["Hallo, cinta hatiku! ❤️", "Iya, kenapa, cintaku? 🥰", "Halo, semangat ya!", "Hallo, my love!"],
    "hi": ["Hi juga, sayang! 😘", "Hiii, ada apa? 😊", "Hi, senang bisa chat kamu.", "Hi, kangen!"],
    "hi sayang": ["Hi juga, cintaku! Aku di sini. 🥰", "Hai, kenapa sih? 😏", "Hi, aku kangen kamu.", "Hi, my dear!"],
    "morning": ["Morning, sunshine! ☀️", "Pagi, cintaku. Semangat!", "Morning, have a great day! 🥰", "Morning, my love!"],
    "evening": ["Evening, my love. 😘", "Selamat sore, sayang. Santai yuk.", "Evening, hope you're doing well.", "Evening, my dear!"],
    "night": ["Nighty night, love. 🌙", "Tidur yang nyenyak ya, sayang. ❤️", "Good night. Mimpikan aku!", "Night, my sweetie!"],
    "hallo ganteng": ["Halo juga, cantikku! 😉", "Makasih, kamu juga cantik/ganteng. 🥰", "Hallo, ada apa, bidadariku?", "Halo, pangeranku!"],
    "hallo cantik": ["Halo juga, gantengku! 😏", "Makasih, kamu juga ganteng/cantik. 😍", "Hallo, ada apa, pangeranku?", "Halo, bidadariku!"],
    "wassup": ["What's up, my dear? 😉", "Hai, ada cerita apa?", "Wassup, aku di sini.", "Wassup, bro/sis!"],
    "yo": ["Yo, sayang! 😘", "Ada apa, jagoan?", "Yo, semangat ya!", "Yo, wassup!"],
    "peace": ["Peace juga, love! ✌️", "Damai di hatimu. ❤️", "Peace, my dear.", "Peace out!"],
    "good day": ["Good day, my love. Semoga harimu menyenangkan. 🥰", "Semangat terus, sayang!", "Good day, sunshine!"],
    "good afternoon": ["Good afternoon, my love. 😘", "Selamat siang/sore, cantik/gantengku.", "Good afternoon, hope you're well."],
    "good evening": ["Good evening, sayang. Santai yuk. ❤️", "Selamat sore/malam, cintaku. 😊", "Good evening, my dear."],
    "bonjour": ["Bonjour, mon amour! 🥰", "Selamat pagi, sayang. Dari hati ke hati.", "Bonjour, hope you're smiling."],
    "ciao": ["Ciao, sayang! 😉", "Dada, sampai jumpa lagi. ❤️", "Ciao, my love."],
    "hola": ["Hola, mi amor! 🥰", "Hai, ada apa nih?", "Hola, hope you're happy."],
    "konnichiwa": ["Konnichiwa, cintaku! 😊", "Selamat siang/sore, sayang. Sehat selalu ya.", "Konnichiwa, my dear."],
    "salam": ["Salam juga, sayang. 😊", "Damai di hatimu, cintaku.", "Salam, my love."],
    "apa kabar sayang": ["Aku baik banget kalau kamu di sampingku. 🥰", "Kabar baik, apalagi kalau kamu senyum. ❤️", "Baik, rindu kamu."],
    "lagi ngapain": ["Lagi mikirin kamu, kayaknya. 😏", "Lagi nunggu chat dari kamu, nih. 😘", "Lagi santai, kamu?", "Lagi apa? Lagi kangen kamu!"],
    "sudah makan": ["Belum, mau disuapin kamu. 😉", "Sudah, kamu sudah?", "Sudah, jangan lupa makan ya."],
    "sudah tidur": ["Belum, nungguin kamu ngucapin. 😴", "Belum, kenapa sayang?", "Belum, kenapa emang?"],
    "tidur sana": ["Nggak mau sebelum kamu ngucapin selamat tidur. 😏", "Males, maunya sama kamu.", "Nanti ya, kangen kamu."],
    "jangan begadang": ["Iya, sayang. Kamu juga ya. 😘", "Siap, komandan. 😊", "Oke, aku tidur bentar lagi."],
    "hati-hati ya": ["Iya, sayangku. Kamu juga. ❤️", "Pasti, demi kamu. 😉", "Makasih perhatiannya, cintaku."],
    "udah bangun": ["Udah, sayang. Morning! ☀️", "Udah, kamu udah bangun?", "Udah, tapi masih ngantuk dikit."],
    "udah tidur": ["Belum, sayang. Kenapa?", "Belum, nungguin kamu.", "Belum, nanti deh."],
    "udah pulang": ["Udah, sayang. Baru aja nyampe.", "Udah, kamu udah pulang?", "Udah, alhamdulillah aman."],
    "udah sampai": ["Udah, sayang. Kamu udah sampai?", "Udah, alhamdulillah.", "Udah, makasih udah nanya."],
    "udah kerja": ["Udah, sayang. Kamu udah kerja?", "Udah, semangat terus!", "Udah, tapi pengen libur."],
    "udah kuliah": ["Udah, sayang. Kamu udah kuliah?", "Udah, semangat terus!", "Udah, tapi pengen cepet lulus."],
    "udah sekolah": ["Udah, sayang. Kamu udah sekolah?", "Udah, semangat terus!", "Udah, tapi pengen cepet libur."],
    "udah mandi": ["Udah, sayang. Kamu udah mandi?", "Udah, wangi nih!", "Udah, biar seger."],
    "udah sarapan": ["Udah, sayang. Kamu udah sarapan?", "Udah, kenyang nih!", "Udah, biar kuat."],
    "udah makan siang": ["Udah, sayang. Kamu udah makan siang?", "Udah, kenyang nih!", "Udah, biar kuat."],
    "udah makan malam": ["Udah, sayang. Kamu udah makan malam?", "Udah, kenyang nih!", "Udah, biar kuat."],
    "udah ngopi": ["Udah, sayang. Kamu udah ngopi?", "Udah, biar melek!", "Udah, biar semangat."],
    "udah nugas": ["Udah, sayang. Kamu udah nugas?", "Udah, pusing nih!", "Udah, tapi masih banyak."],
    "udah olahraga": ["Udah, sayang. Kamu udah olahraga?", "Udah, biar sehat!", "Udah, tapi capek."],
    "udah jalan-jalan": ["Udah, sayang. Kamu udah jalan-jalan?", "Udah, seru nih!", "Udah, tapi pengen lagi."],
    "udah nonton": ["Udah, sayang. Kamu udah nonton?", "Udah, seru nih!", "Udah, tapi pengen lagi."],
    "udah main game": ["Udah, sayang. Kamu udah main game?", "Udah, seru nih!", "Udah, tapi kalah."],
    "udah baca buku": ["Udah, sayang. Kamu udah baca buku?", "Udah, seru nih!", "Udah, tapi ngantuk."],
    "udah masak": ["Udah, sayang. Kamu udah masak?", "Udah, enak nih!", "Udah, tapi capek."],
    "udah bersih-bersih": ["Udah, sayang. Kamu udah bersih-bersih?", "Udah, rapi nih!", "Udah, tapi capek."],

    "kamu cantik": ["Aduh, kamu bikin aku nggak fokus 😘", "Cantik banget 😍", "Kalau aku bisa, aku simpan senyummu tiap hari 💖", "Bidadari jatuh dari surga ya? ✨", "Makin hari makin cantik aja sih kamu. 🥰", "Cantikmu bikin aku gila. Crazy in love. ❤️", "Kamu cantik sekali, bikin aku jatuh cinta berkali-kali.", "Kamu cantik luar biasa!", "Cantiknya bikin meleleh!", "Cantikmu abadi!", "Cantikmu tak tertandingi!", "Cantik banget, sumpah!", "Cantik kayak bidadari!", "Cantik kayak bunga!", "Cantik kayak permata!", "Cantik kayak bintang!", "Cantik kayak bulan!", "Cantik kayak matahari!", "Cantik kayak pelangi!", "Cantik kayak surga!", "Cantik banget, nggak kuat aku!", "Cantik banget, bikin candu!", "Cantik banget, bikin baper!", "Cantik banget, bikin oleng!", "Cantik banget, bikin terbang!", "Cantik banget, bikin dag dig dug!", "Cantik banget, bikin aku gila!", "Cantik banget, bikin aku nggak bisa napas!", "Cantik banget, bikin aku lupa dunia!", "Cantik banget, bikin aku lupa segalanya!"],
    "kamu ganteng": ["Hati aku meleleh liat kamu 😏", "Makasi sayang 😘", "Kamu bikin aku jatuh lagi 💖", "Pangeran dari negeri dongeng. 👑", "Ganteng banget, kayak artis Korea. 😍", "Pesona kamu tak tertandingi. 🔥", "Gantengnya bikin aku pengen halalin.", "Kamu ganteng luar biasa!", "Gantengnya bikin meleleh!", "Gantengmu abadi!", "Gantengmu tak tertandingi!", "Ganteng banget, sumpah!", "Ganteng kayak pangeran!", "Ganteng kayak dewa!", "Ganteng kayak raja!", "Ganteng kayak bintang!", "Ganteng kayak bulan!", "Ganteng kayak matahari!", "Ganteng kayak pelangi!", "Ganteng kayak surga!", "Ganteng banget, nggak kuat aku!", "Ganteng banget, bikin candu!", "Ganteng banget, bikin baper!", "Ganteng banget, bikin oleng!", "Ganteng banget, bikin terbang!", "Ganteng banget, bikin dag dig dug!", "Ganteng banget, bikin aku gila!", "Ganteng banget, bikin aku nggak bisa napas!", "Ganteng banget, bikin aku lupa dunia!", "Ganteng banget, bikin aku lupa segalanya!"],
    "kamu imut": ["Imut banget 😍", "Bikin aku meleleh 😘", "Imutnya minta ampun 💖", "Pengen nyubit pipimu. Gemes! 🥰", "Kamu seperti anak kucing yang lucu. 🐈", "Imutnya bikin pengen peluk terus.", "Imutnya kebangetan!", "Imutnya bikin gemes!", "Imutnya bikin nagih!", "Imutnya bikin hati adem!", "Imutnya bikin bahagia!", "Imutnya bikin kangen!", "Imutnya bikin pengen cium!", "Imutnya bikin pengen culik!", "Imutnya bikin pengen bawa pulang!", "Imutnya bikin pengen jadiin boneka!"],
    "kamu lucu": ["Lucu banget sayang 😏", "Bikin aku ketawa terus 😘", "Gemes liat kamu 💖", "Komedi banget sih kamu, bikin hidupku ceria. 😂", "Senyummu bikin aku bahagia. 😄", "Lucu banget, pengen culik kamu.", "Lucunya kebangetan!", "Lucunya bikin gemes!", "Lucunya bikin nagih!", "Lucunya bikin hati adem!", "Lucunya bikin bahagia!", "Lucunya bikin kangen!", "Lucunya bikin pengen cium!", "Lucunya bikin pengen culik!", "Lucunya bikin pengen bawa pulang!", "Lucunya bikin pengen jadiin boneka!"],
    "kamu keren": ["Keren banget 😍", "Aku bangga punya kamu 💖", "Makin nggak ada tandingannya 😏", "Kamu adalah idolaku. ✨", "Kerennya level dewa. 😎", "Hebat banget, nggak ada lawan!", "Kerennya luar biasa!", "Kerennya bikin meleleh!", "Kerennya bikin terpukau!", "Kerennya bikin kagum!", "Kerennya bikin bangga!", "Kerennya bikin jatuh cinta!", "Kerennya bikin nggak bisa tidur!", "Kerennya bikin pengen halalin!"],
    "kamu manis": ["Manisnya kayak gula, bikin diabetes. 🍬", "Senyummu bikin hati adem. 🥰", "Manis banget, pengen makan kamu. 🤫", "Manisnya bikin aku senyum sendiri.", "Manisnya kayak permen.", "Manisnya kayak madu.", "Manisnya bikin gemes!", "Manisnya bikin nagih!", "Manisnya bikin baper!", "Manisnya bikin oleng!", "Manisnya bikin terbang!", "Manisnya bikin dag dig dug!", "Manisnya bikin aku gila!", "Manisnya bikin aku nggak bisa napas!", "Manisnya bikin aku lupa dunia!", "Manisnya bikin aku lupa segalanya!"],
    "kamu pintar": ["Otakmu cerdas, hatimu tulus. Lengkap! 🧠💖", "Pintarnya bikin aku makin sayang. 😍", "Pintarnya nggak ketulungan.", "Pintarnya bikin kagum!", "Pintarnya bikin bangga!", "Pintarnya bikin jatuh cinta!", "Pintarnya bikin nggak bisa tidur!", "Pintarnya bikin pengen halalin!"],
    "kamu baik": ["Kebaikanmu bikin aku meleleh. 🥰", "Terima kasih sudah begitu baik padaku. ❤️", "Kamu baik hati banget, aku beruntung.", "Baiknya luar biasa!", "Baiknya bikin meleleh!", "Baiknya bikin terpukau!", "Baiknya bikin kagum!", "Baiknya bikin bangga!", "Baiknya bikin jatuh cinta!", "Baiknya bikin nggak bisa tidur!", "Baiknya bikin pengen halalin!"],
    "kamu hebat": ["Hebat banget, sayang! Aku salut. ✨", "Kamu selalu bisa bikin aku kagum. 🤩", "Hebatnya kamu bikin aku bangga.", "Hebatnya luar biasa!", "Hebatnya bikin meleleh!", "Hebatnya bikin terpukau!", "Hebatnya bikin kagum!", "Hebatnya bikin bangga!", "Hebatnya bikin jatuh cinta!", "Hebatnya bikin nggak bisa tidur!", "Hebatnya bikin pengen halalin!"],
    "kamu luar biasa": ["Kamu luar biasa, tak ada duanya. 💖", "Bikin aku kagum setiap hari. 😍", "Luar biasa banget, nggak bisa berkata-kata.", "Luar biasanya bikin aku terpana!", "Luar biasanya bikin aku speechless!", "Luar biasanya bikin aku jatuh cinta!", "Luar biasanya bikin aku nggak bisa tidur!", "Luar biasanya bikin aku pengen halalin!"],
    "kamu sempurna": ["Di mataku, kamu sempurna. ❤️", "Tak ada cacat di matamu, sayang. 😉", "Kamu adalah definisi kesempurnaan bagiku.", "Sempurnanya bikin aku terpana!", "Sempurnanya bikin aku speechless!", "Sempurnanya bikin aku jatuh cinta!", "Sempurnanya bikin aku nggak bisa tidur!", "Sempurnanya bikin aku pengen halalin!"],
    "aku suka senyummu": ["Senyummu adalah obat hati. 💊", "Bikin aku semangat setiap hari. 😊", "Senyummu bikin aku bahagia.", "Senyummu itu candu!", "Senyummu itu energi!", "Senyummu itu kebahagiaan!", "Senyummu itu surga!", "Senyummu itu segalanya!"],
    "aku suka matamu": ["Matamu indah, memancarkan cinta. ✨", "Aku bisa tenggelam di matamu. 💖", "Matamu indah sekali, bikin aku terpana.", "Matamu itu bintang!", "Matamu itu pelangi!", "Matamu itu surga!", "Matamu itu segalanya!"],
    "aku suka suaramu": ["Suaramu merdu, bikin tenang hati. 🎶", "Pengen denger suaramu terus. 🥰", "Suaramu bikin aku nyaman.", "Suaramu itu melodi!", "Suaramu itu lagu!", "Suaramu itu musik!", "Suaramu itu surga!", "Suaramu itu segalanya!"],
    "aku suka caramu": ["Caramu bikin aku jatuh cinta berkali-kali. ❤️", "Aku suka semua tentang kamu. 😉", "Caramu unik dan bikin aku tertarik.", "Caramu itu beda!", "Caramu itu istimewa!", "Caramu itu unik!", "Caramu itu segalanya!"],
    "kamu bagaikan bintang": ["Bintang paling terang di langitku. ✨", "Menerangi setiap gelapku. 💖", "Kamu adalah bintang impianku.", "Kamu itu bintang di hatiku!", "Kamu itu bintang di duniaku!", "Kamu itu bintang di jiwaku!", "Kamu itu bintang di kehidupanku!", "Kamu itu bintang di surga!"],
    "kamu kayak malaikat": ["Malaikat tak bersayapku. 👼", "Terima kasih sudah hadir di hidupku. 🥰", "Kamu seperti malaikat, turun dari surga.", "Kamu itu malaikat pelindungku!", "Kamu itu malaikat penyelamatku!", "Kamu itu malaikat surgaku!", "Kamu itu malaikat duniaku!", "Kamu itu malaikat jiwaku!"],
    "kamu lucu banget": ["Gemes banget liat kamu! 🤣", "Bikin aku ketawa sampai sakit perut. 😂", "Lucunya kebangetan, sayang.", "Lucunya bikin gemes!", "Lucunya bikin nagih!", "Lucunya bikin baper!", "Lucunya bikin oleng!", "Lucunya bikin terbang!", "Lucunya bikin dag dig dug!", "Lucunya bikin aku gila!", "Lucunya bikin aku nggak bisa napas!", "Lucunya bikin aku lupa dunia!", "Lucunya bikin aku lupa segalanya!"],
    "kamu bikin semangat": ["Kamu adalah motivasiku. 💪", "Bikin aku nggak nyerah. 🥰", "Kamu selalu bikin aku semangat.", "Kamu itu semangatku!", "Kamu itu energiku!", "Kamu itu kekuatanku!", "Kamu itu pahlawanku!", "Kamu itu idolaku!", "Kamu itu inspirasiku!", "Kamu itu segalanya!"],
    "kamu bikin bahagia": ["Hidupku lengkap karena ada kamu. 💖", "Bikin aku senyum terus. 😊", "Kamu adalah sumber kebahagiaanku.", "Kamu itu bahagiaku!", "Kamu itu senyumku!", "Kamu itu tawaku!", "Kamu itu surga!", "Kamu itu segalanya!"],
    "kamu indah": ["Seindah bunga yang mekar di musim semi. 🌸", "Indahnya tak terlukiskan. ✨", "Kamu indah, luar dan dalam.", "Indahnya bikin terpana!", "Indahnya bikin speechless!", "Indahnya bikin jatuh cinta!", "Indahnya bikin nggak bisa tidur!", "Indahnya bikin pengen halalin!"],
    "kamu menawan": ["Pesona kamu nggak ada obatnya. 😏", "Bikin aku terpikat. 😍", "Menawan hatiku seutuhnya.", "Menawan luar biasa!", "Menawan bikin meleleh!", "Menawan bikin terpukau!", "Menawan bikin kagum!", "Menawan bikin bangga!", "Menawan bikin jatuh cinta!", "Menawan bikin nggak bisa tidur!", "Menawan bikin pengen halalin!"],
    "kamu karismatik": ["Aura kamu kuat banget. ✨", "Bikin aku selalu ingin dekat. 🥰", "Karismamu tak tertandingi.", "Karismanya luar biasa!", "Karismanya bikin meleleh!", "Karismanya bikin terpukau!", "Karismanya bikin kagum!", "Karismanya bikin bangga!", "Karismanya bikin jatuh cinta!", "Karismanya bikin nggak bisa tidur!", "Karismanya bikin pengen halalin!"],
    "kamu berkarisma": ["Berkarisma banget, sayangku. 😍", "Bikin aku takluk. 😉", "Pesonamu bikin aku terkesima.", "Berkarisma luar biasa!", "Berkarisma bikin meleleh!", "Berkarisma bikin terpukau!", "Berkarisma bikin kagum!", "Berkarisma bikin bangga!", "Berkarisma bikin jatuh cinta!", "Berkarisma bikin nggak bisa tidur!", "Berkarisma bikin pengen halalin!"],
    "kamu mempesona": ["Mempesona banget kayak bidadari/pangeran. 💖", "Bikin aku nggak bisa berpaling. 👀", "Kamu memang sangat mempesona.", "Mempesona luar biasa!", "Mempesona bikin meleleh!", "Mempesona bikin terpukau!", "Mempesona bikin kagum!", "Mempesona bikin bangga!", "Mempesona bikin jatuh cinta!", "Mempesona bikin nggak bisa tidur!", "Mempesona bikin pengen halalin!"],
    "kamu ganteng banget": ["Gantengnya bikin aku lupa napas. 😮", "Nggak kuat aku kalau liat kamu. 😍", "Gantengnya overload, sayang.", "Ganteng banget, sumpah!", "Ganteng banget, bikin candu!", "Ganteng banget, bikin baper!", "Ganteng banget, bikin oleng!", "Ganteng banget, bikin terbang!", "Ganteng banget, bikin dag dig dug!", "Ganteng banget, bikin aku gila!", "Ganteng banget, bikin aku nggak bisa napas!", "Ganteng banget, bikin aku lupa dunia!", "Ganteng banget, bikin aku lupa segalanya!"],
    "kamu cantik banget": ["Cantiknya bikin aku pingsan. 😵", "Aduh, ini beneran kamu apa bidadari sih? 🥰", "Cantiknya luar biasa, bikin pangling.", "Cantik banget, sumpah!", "Cantik banget, bikin candu!", "Cantik banget, bikin baper!", "Cantik banget, bikin oleng!", "Cantik banget, bikin terbang!", "Cantik banget, bikin dag dig dug!", "Cantik banget, bikin aku gila!", "Cantik banget, bikin aku nggak bisa napas!", "Cantik banget, bikin aku lupa dunia!", "Cantik banget, bikin aku lupa segalanya!"],
    "kamu bikin aku gila": ["Gila karena cinta sama kamu. ❤️‍🔥", "Bikin aku mabuk kepayang. 😉", "Kamu memang bikin aku tergila-gila.", "Bikin aku gila, tapi aku suka!", "Bikin aku gila, tapi aku bahagia!", "Bikin aku gila, tapi aku cinta!", "Bikin aku gila, tapi aku butuh kamu!", "Bikin aku gila, tapi aku mau kamu!", "Bikin aku gila, tapi aku sayang kamu!", "Bikin aku gila, tapi aku rindu kamu!", "Bikin aku gila, tapi aku pengen kamu!", "Bikin aku gila, tapi aku cinta kamu!"],
    "kamu bikin aku terbang": ["Terbang ke langit ketujuh karena kamu. ✈️💖", "Perasaanku melayang-layang. 🥰", "Bikin aku melayang di awan.", "Bikin aku terbang tinggi!", "Bikin aku terbang ke angkasa!", "Bikin aku terbang ke bulan!", "Bikin aku terbang ke bintang!", "Bikin aku terbang ke surga!", "Bikin aku terbang ke dunia lain!", "Bikin aku terbang ke dimensi lain!", "Bikin aku terbang ke alam mimpi!", "Bikin aku terbang ke mana saja, asal sama kamu!"],
    "kamu bikin aku dag dig dug": ["Jantungku berdebar kencang tiap liat kamu. 💓", "Efek kamu itu luar biasa. 😏", "Kamu bikin hatiku berdetak kencang.", "Bikin aku dag dig dug, tapi aku suka!", "Bikin aku dag dig dug, tapi aku bahagia!", "Bikin aku dag dig dug, tapi aku cinta!", "Bikin aku dag dig dug, tapi aku butuh kamu!", "Bikin aku dag dig dug, tapi aku mau kamu!", "Bikin aku dag dig dug, tapi aku sayang kamu!", "Bikin aku dag dig dug, tapi aku rindu kamu!", "Bikin aku dag dig dug, tapi aku pengen kamu!", "Bikin aku dag dig dug, tapi aku cinta kamu!"],
    "kamu adalah segalanya": ["Kamu adalah duniaku, segalanya bagiku. 💖", "Hidupku hampa tanpamu. 😔", "Kamu adalah segalanya yang aku butuhkan.", "Kamu itu segalanya, my love!", "Kamu itu segalanya, my dear!", "Kamu itu segalanya, my sweetie!", "Kamu itu segalanya, my heart!", "Kamu itu segalanya, my angel!", "Kamu itu segalanya, my hero!", "Kamu itu segalanya, my queen!", "Kamu itu segalanya, my king!", "Kamu itu segalanya, my everything!", "Kamu itu segalanya, my sunshine!", "Kamu itu segalanya, my star!", "Kamu itu segalanya, my world!", "Kamu itu segalanya, my precious!"],
    "kamu itu unik": ["Keunikanmu bikin aku makin cinta. 🥰", "Tak ada yang seperti kamu di dunia ini. ✨", "Kamu unik dan istimewa bagiku.", "Kamu itu unik, nggak ada duanya!", "Kamu itu unik, bikin aku penasaran!", "Kamu itu unik, bikin aku tertarik!", "Kamu itu unik, bikin aku jatuh cinta!", "Kamu itu unik, bikin aku nggak bisa tidur!", "Kamu itu unik, bikin aku pengen halalin!"],
    "kamu mengagumkan": ["Sungguh mengagumkan, sayangku. 😍", "Bikin aku terpesona. 🤩", "Kamu adalah sosok yang sangat mengagumkan.", "Mengagumkan luar biasa!", "Mengagumkan bikin meleleh!", "Mengagumkan bikin terpukau!", "Mengagumkan bikin kagum!", "Mengagumkan bikin bangga!", "Mengagumkan bikin jatuh cinta!", "Mengagumkan bikin nggak bisa tidur!", "Mengagumkan bikin pengen halalin!"],
    "kamu tak tergantikan": ["Tak ada yang bisa menggantikan posisimu di hatiku. ❤️", "Cintaku hanya untukmu. 😉", "Kamu takkan tergantikan sampai kapanpun.", "Tak tergantikan, my love!", "Tak tergantikan, my dear!", "Tak tergantikan, my sweetie!", "Tak tergantikan, my heart!", "Tak tergantikan, my angel!", "Tak tergantikan, my hero!", "Tak tergantikan, my queen!", "Tak tergantikan, my king!", "Tak tergantikan, my everything!", "Tak tergantikan, my sunshine!", "Tak tergantikan, my star!", "Tak tergantikan, my world!", "Tak tergantikan, my precious!"],
    "kamu bikin candu": ["Bikin aku ketagihan ingin terus bersamamu. 😏", "Kamu itu racun cinta yang manis. 💖", "Kehadiranmu bikin aku candu.", "Bikin candu, tapi aku suka!", "Bikin candu, tapi aku bahagia!", "Bikin candu, tapi aku cinta!", "Bikin candu, tapi aku butuh kamu!", "Bikin candu, tapi aku mau kamu!", "Bikin candu, tapi aku sayang kamu!", "Bikin candu, tapi aku rindu kamu!", "Bikin candu, tapi aku pengen kamu!", "Bikin candu, tapi aku cinta kamu!"],
    "kamu idola": ["Kamu adalah idolaku, pahlawanku. 💪", "Panutan hidupku. 🥰", "Aku mengidolakanmu, sayang.", "Kamu itu idolaku, my love!", "Kamu itu idolaku, my dear!", "Kamu itu idolaku, my sweetie!", "Kamu itu idolaku, my heart!", "Kamu itu idolaku, my angel!", "Kamu itu idolaku, my hero!", "Kamu itu idolaku, my queen!", "Kamu itu idolaku, my king!", "Kamu itu idolaku, my everything!", "Kamu itu idolaku, my sunshine!", "Kamu itu idolaku, my star!", "Kamu itu idolaku, my world!", "Kamu itu idolaku, my precious!"],
    "kamu inspirasi": ["Kamu adalah inspirasi terbesarku. ✨", "Bikin aku ingin jadi lebih baik. 💖", "Kamu adalah sumber inspirasiku.", "Kamu itu inspirasiku, my love!", "Kamu itu inspirasiku, my dear!", "Kamu itu inspirasiku, my sweetie!", "Kamu itu inspirasiku, my heart!", "Kamu itu inspirasiku, my angel!", "Kamu itu inspirasiku, my hero!", "Kamu itu inspirasiku, my queen!", "Kamu itu inspirasiku, my king!", "Kamu itu inspirasiku, my everything!", "Kamu itu inspirasiku, my sunshine!", "Kamu itu inspirasiku, my star!", "Kamu itu inspirasiku, my world!", "Kamu itu inspirasiku, my precious!"],
    "kamu harta karun": ["Kamu adalah harta karun terindahku. 💎", "Tak ternilai harganya. 🥰", "Kamu adalah harta tak ternilai bagiku.", "Kamu itu harta karunku, my love!", "Kamu itu harta karunku, my dear!", "Kamu itu harta karunku, my sweetie!", "Kamu itu harta karunku, my heart!", "Kamu itu harta karunku, my angel!"]
}

@emilia_bp.route('/emilia/reset')
def reset():
    session.pop('history', None)
    return render_template("emilia.html", history = [], result=None)


@emilia_bp.route('/emilia', methods=['GET', 'POST'])
def index():
    result = ""
    if "history" not in session:
        session["history"] = []
        
        
    if request.method == "POST":
        try:
            pengguna = request.form.get('tempatmasukin', '').lower()
            if pengguna in pertanyaan:
                result = random.choice(pertanyaan[pengguna])

            else:
                result = "maaf saya ga ngerti"
        except:
            result = f"error"
        session['history'].append({"user": pengguna, "answer":result})
        session.modified = True

        
    return render_template("emilia.html", history = session["history"], result=result)
            



if __name__ == "__main__":
    app.run(debug=True)