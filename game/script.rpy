# Materi :
    # tipe data
    # variabel
    # jenis operator

init:  # Deklarasi karakter (chara) yang akan masuk ke cerita
    define moderator = Character("Tohka | Moderator")
    # karakter 1 sumi lalu karakter 2 miki nanti diisi pas diperkenalan 
    # dengan $chr_1 Character("sumi") misal
    define chr_1 = Character("????") # sumi
    define chr_2 = Character("????") # miki
    define main = Character("Me")
    # Define <nama_variabel> = Character

    # untuk upload gambar
    # image <nama_var> = "namagambar.ekstensi"
    # image seperti define tetapi ini untuk image bukan karakter
    image moderator = "tohka/1.png"
    image ruangKelas = "background/ruangkelas.jpg"
    image luarKelas = "background/luarkelas.png"
    # Gambar sumi
    image sumi = "Sumi/Smile.png"
    image sumi_sad = "Sumi/Sad.png"
    image sumi_open = "Sumi/Open.png"
    # Gambar miki
    image miki = "Miki/Smile.png"
    image miki_blush = "Miki/blush.png"
    image miki_open = "Miki/Smile_AllOpen.png"
    image miki_close = "Miki/Smile_CloseAll.png"

    # image aiko = "Aiko_Blazer/Aiko_B_Blazer_Closed_Open.png"
    # image aiko_blush = "Aiko_Blazer/Aiko_B_Blazer_Frown_Blush.png"
    # image ruangkelas2 = "tohka/1.png"
    
    # Variabel Image Materi
    
    
label start :
    play music "audio/kelas/PeachyPie_DDL.mp3" fadeout 1.0 fadein 1.0
    # bg untuk latar awal # Classroom
    scene ruangKelas with dissolve
    # menambah delay pause
    pause (1.0)
    show moderator with dissolve
    moderator "Selamat Datang Di Game Visual Novel Sederhana...."
    moderator "Sebelum Itu Ayo Isikan Namamu !" with dissolve
    $ player_name = renpy.input("Masukkan NAMA :")
    $ player_name = player_name.strip()
    moderator "Selamat Menikmati Game, [player_name] !" with dissolve
    hide moderator
    with dissolve
    # with dissolve agar tampil smooth
    # timpa sumi sad dulu setelah halo lalu hapus img sumi biasa
    # show sumi_sad
    pause (1.3)
    show sumi
    with dissolve
    chr_1 "Yahalooooooooooo!"
    menu :
        "Kamu siapa ?" :
            $ chr_1 = Character("Sumi")
            chr_1 "Aku Sumi"
    # geser sumi sad
    # show sumi_sad at left
    hide sumi
    # with move
    show sumi_sad at center:  # align horizontal 0.0
        yalign 0.3 # align vertikal 0 (untuk atas).0 (untuk bwh)
        zoom 1.3
    with dissolve
    chr_1 "Kamu Perkenalkan Diri Dong..."

    menu :
        "Apa Harus Banget nih ??" :
            chr_1 "Yaiyalah !"
            menu :
                "Namaku [player_name]" :
                    # play sound "audio/sfx/mixkit-clear-mouse-clicks-2997.wav"
                    hide sumi_sad
                    show sumi_open at center :
                        yalign 0.1
                        zoom 1.2
                    with dissolve
                    chr_1 "Gitu Dongggg"
                    hide sumi_open
                    show sumi at center :
                        yalign 0.1
                        zoom 1.2
                    chr_1 "Halo,[player_name]" with dissolve
             
        "Aku, [player_name]" :
            # play sound "audio/sfx/mixkit-clear-mouse-clicks-2997.wav"
            hide sumi_sad
            show sumi at center :
                yalign 0.1
                zoom 1.2
            with dissolve
            chr_1 "Halo,[player_name]"

    # with dissolve
    show sumi at left :
        yalign 0.1
        zoom 1.2 
        xzoom -1
    with move
    pause (0.7)

    # timpa nanti pada menu hilangkan miki blush
    show miki_open at center:
        yalign -0.3
        zoom 1.18
    show miki_blush at center :
        yalign -0.3
        zoom 1.18
    with dissolve
    
    chr_2 "Anu..."
    with dissolve
                    
    menu :
        "Ya..??":
            chr_2 "........."
            menu :
                "Siapa Nama Kamu..?" : 
                    hide miki_blush
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                    with move
                    with dissolve
                    $ chr_2 = Character("Miki")
                    chr_2 "Aku Miki"
                    menu :
                        "Halo Miki, aku [player_name]" :
                            hide miki_open 
                            show miki_close at right :
                                yalign -0.3
                                zoom 1.18
                            chr_2 "Oke semoga bisa akrab ya [player_name] !"
                            hide sumi
                            show sumi_open at left :
                                yalign 0.1
                                zoom 1.2 
                                xzoom -1
                            with dissolve
                            chr_1 "Miki, Santai Aja [player_name] Ga Gigit Kok "
                            menu :
                                "......" :
                                    hide sumi_open
                                    show sumi at left :
                                        yalign 0.1
                                        zoom 1.2 
                                        xzoom -1
                                    hide miki_close
                                    show miki at right :
                                        yalign -0.3
                                        zoom 1.18
                                    chr_2 "Hahaahaha , bisa aja kamu Sumi teman lamaku..."
                                    hide sumi
                                    show sumi_open at left :
                                        yalign 0.1
                                        zoom 1.2
                                    with dissolve
                                    chr_1 "Emm untuk topik obrolan kita bahas sesuatu yuk..." 
                                    hide sumi_open
                                    show sumi at left :
                                        yalign 0.1
                                        zoom 1.2
                "Biar Kutebak Nama Kamu.... Neko ?" :
                    hide miki_blush
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                    with move
                    with dissolve
                    $ chr_2 = Character("Miki")
                    chr_2 "Bukannn Aku Miki"
                    menu :
                        "Waduh Maaf Salah Tebak" :
                            show miki_open at right :
                                yalign -0.3
                                zoom 1.18
                                xzoom -1
                            with dissolve
                            chr_2 "Heheheh Gapapakok"
                            hide sumi
                            show sumi_open at left :
                                yalign 0.1
                                zoom 1.2
                            with dissolve
                            chr_1 "Emm untuk topik obrolan kita bahas sesuatu yuk..." 
                            hide sumi_open
                            show sumi at left :
                                yalign 0.1
                                zoom 1.2
        "Siapa Ya ..??" :
            $ chr_2 = Character("Miki")
            chr_2 "Aku Miki, kamu ??"
            menu :
                "Aku [player_name]" :
                    hide miki_blush
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                    with move
                    with dissolve
                    chr_2 "Salam Kenal [player_name], Semoga bisa akrab ya !"
                    menu : 
                        "Siappp" :
                            hide sumi
                            show sumi_open at left :
                                yalign 0.1
                                zoom 1.2
                            with dissolve
                            chr_1 "Emm untuk topik obrolan kita bahas sesuatu yuk..." 
                            hide sumi_open
                            show sumi at left :
                                yalign 0.1
                                zoom 1.2

    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1
    with dissolve
    chr_2 "Kita mau bahas apa nih ?"
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18
        xzoom -1
    with dissolve
    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
        xzoom -1
    with dissolve
    chr_1 "Bahas apa ya ... , aku maunya sih tentang teknologi kayak bahasa pemograman gitu terus bahasa yang lagi trend..." 
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve

    menu:
        "Bahasa Pemograman?, Apa itu ?" :
            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
            with dissolve
            chr_1 "Masa Kamu Gatau ?"
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2

            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18
            with dissolve
            chr_2 "Bahasa pemrograman merupakan sebuah alat komunikasi yang digunakan untuk memberikan instruksi kepada komputer agar menjalankan tugas-tugas tertentu, [player_name].
            "
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18
            with dissolve
            menu : 
                "Owh jadi begitu..." :
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                    with dissolve
                    chr_2 "Iyesss!"
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18
                    with dissolve

                    hide sumi
                    show sumi_open at left :
                        yalign 0.1
                        zoom 1.2
                    with dissolve
                    chr_1 "Paham ga ? , pasti gapaham xixixixi"
                    hide sumi_open
                    show sumi at left :
                        yalign 0.1
                        zoom 1.2
                    with dissolve
                    menu :
                        "........" :
                            hide miki
                            show miki_open at right :
                                yalign -0.3
                                zoom 1.18
                            with dissolve
                            chr_2 "Hahaha, bahas bahasa pemograman apa ya?"
                            chr_2 "Emmm... bahasa pemograman yang sekarang populer itu apa ya namanya ...."
                            hide miki_open
                            show miki at right :
                                yalign -0.3
                                zoom 1.18
                            with dissolve

        "Boleh Tuhhh Aku Juga Kepo :D" :
            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
                xzoom -1
            chr_1 "Emang kamu tau Bahasa Pemograman apa?"
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2
            menu : 
                "Tau Kok... kan aku anak IT" :
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                    with dissolve
                    chr_2 "Hahaha, bahas bahasa pemograman apa ya?"
                    chr_2 "Emmm... bahasa pemograman yang sekarang populer itu apa ya namanya...."
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18
                    with dissolve
    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
        xzoom -1
    with dissolve
    chr_1 "Python, Miki!" 
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve

    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18
    with dissolve
    chr_2 "Hebatttt Sumi!, kamu update juga ya tentang bidang pemograman ?"  
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18
    with dissolve
    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
        xzoom -1
    with dissolve
    chr_1 "Enggak terlalu tapi aku sering nonton TikTok Hehehehe"
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve

    menu : 
        "Jadi.. kita bahas bahasa pemograman Python apanya aku awam soalnya ???" :
            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
                xzoom -1
            with dissolve
            chr_1 "Bagaimana Kalau Mulai Dari Pengertian nya ?"
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2
                xzoom -1
            with dissolve
            menu :
                "Lesssgoooo!" :
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                        xzoom -1
                    with dissolve
                    chr_2 "Python adalah bahasa pemrograman tingkat tinggi yang bersifat dinamis, memiliki sintaksis sederhana, dan mudah dipelajari."
                    chr_2 "Bahasa ini bisa dijalankan di hampir semua arsitektur sistem, bisa dipakai untuk aplikasi-aplikasi di berbagai bidang."
                    chr_2 "Lalu... Bahasa pemrograman Python diciptakan oleh Guido van Rossum. " with dissolve
                    chr_2 "Python pertama kali dirilis pada bulan Februari 1991. Guido van Rossum mengembangkan Python sebagai proyek pribadi dan merilis versi pertamanya, Python 0.9.0, ke publik pada tahun 1991. "
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18
                        xzoom -1
                    with dissolve

                    hide sumi
                    show sumi_open at left :
                        yalign 0.1
                        zoom 1.2
                    with dissolve
                    chr_1 "Btw, Game ini dibuat menggunakan bahasa Python Lohh, [player_name]!"
                    hide sumi_open
                    show sumi at left :
                        yalign 0.1
                        zoom 1.2
                        xzoom -1
                    with dissolve

                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                        xzoom -1
                    with dissolve
                    chr_2 "Yapsss !"
                    chr_2 "Kita lanjut ke pembahasan variabel yuk!"
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18
                    with dissolve
                    menu : 
                        "Gas !" :
                            jump variabel_py

label variabel_py :
    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1
    with dissolve
    chr_2 "Dalam Python ada istilah Variabel yang merupakan tempat untuk menyimpan suatu nilai seperti angka, teks, daftar, serta objek loh [player_name] !"
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18
    with dissolve

    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
        xzoom -1
    with dissolve
    chr_1 "Dan juga, Variabel memiliki aturan cara penulisan loh, kalau salah sedikit nantinya program tidak akan bekerja :( "
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve

    menu :
        "Contoh Penulisan Variabel Yang Salah Bagaimana ?" :
            # Variabel salah
            image var_salah = "Content/Variable/variabel_salah.png"
            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18
                xzoom -1
            with dissolve
            chr_2 "Berikut Contohnya, [player_name]"
            show var_salah at center :
                yalign 0.4
                zoom 1.3
            with dissolve
            chr_2 "Apakah terlihat?"
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18
            with dissolve
            hide var_salah

            menu :
                "Iya, Terlihat" :
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                        xzoom -1
                    with dissolve
                    chr_2 "Manteppp"
                    show var_salah at center :
                        yalign 0.4
                        zoom 1.3
                    with dissolve  
                    chr_2 "Dalam penulisan variabel tidak boleh ada spasi, @ serta persen"
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18
                    with dissolve

                    hide var_salah
                    menu :
                        "Kalau Contoh Variabel Yang Benar Bagaimana ?" :
                            hide sumi
                            show sumi_open at left :
                                yalign 0.1
                                zoom 1.2
                                xzoom-1
                            with dissolve

                            show var_benar at center :
                                yalign 0.4
                                zoom 1.3
                            with dissolve

                            chr_1 "Begini yang benar ..."

                            hide sumi_open
                            show sumi at left :
                                yalign 0.1
                                zoom 1.2
                                xzoom-1
                            with dissolve

                            hide var_benar

                            menu :
                                "Lalu... apa lagi selain variabel ?" :
                                    hide miki
                                    show miki_open at right :
                                        yalign -0.3
                                        zoom 1.18
                                    with dissolve
                                    chr_2 "Apa ya..."
                                    hide miki_open
                                    show miki at right :
                                        yalign -0.3
                                        zoom 1.18
                                    with dissolve

                                    jump tipe_data

        "Contoh Penulisan Variabel Yang Benar ?" :
            image var_benar = "Content/Variable/variabel_benar.png"
            show var_benar at center :
                yalign 0.4
                zoom 1.3
            with dissolve

            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
                xzoom-1
            with dissolve
            chr_1 "Begini yang benar"
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2
            with dissolve

            hide var_benar
            menu :
                "Lalu... apa lagi selain variabel ?" :
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                        xzoom -1
                    with dissolve
                    chr_2 "Apa ya..."
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18
                    with dissolve
                    jump tipe_data

label tipe_data :
    # buat variabel tipe data img
    image tipe_data = "Content/Tipe_data/1.png"
    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
        xzoom-1
    with dissolve
    chr_1 "Bagaimana kalau kita bahas selanjutnya tipe data ?"
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve   

    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1   
    with dissolve                       
    chr_2 "Nah, ide bagus. Maafkan aku tadi zonk soalnya hehehehe"
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18
        xzoom -1   
    with dissolve 
    menu :
        "Tipe data ? apa itu ?..." :
            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18
                xzoom -1   
            with dissolve 
            chr_2 "Tipe data dalam pemrograman adalah cara untuk mengklasifikasikan dan mendefinisikan jenis data yang dapat disimpan dan diolah dalam program komputer."
            chr_2 "Dan juga, Setiap tipe data memiliki karakteristik dan perilaku tertentu yang mempengaruhi bagaimana data tersebut diperlakukan dan dioperasikan."
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18   
            with dissolve
            menu :
                "Untuk contoh kode nya bagaimana ?" :
                    hide sumi
                    show sumi_open at left :
                        yalign 0.1
                        zoom 1.2
                        xzoom-1
                    with dissolve
                    show tipe_data at center  :
                        xalign 0.6
                        yalign 0.4
                        zoom 1.3
                    with dissolve
                    chr_1 "Berikut Kodenya"
                    hide sumi_open
                    show sumi at left :
                        yalign 0.1
                        zoom 1.2
                    with dissolve

                    hide tipe_data
                    menu :
                        "Bisakah kamu menjelaskan tiap jenis nya ?" :
                            hide sumi
                            show sumi_open at left :
                                yalign 0.1
                                zoom 1.2
                                xzoom-1
                            with dissolve
                            chr_1 "Tentu !"
                            show tipe_data at center  :
                                xalign 0.6
                                yalign 0.4
                                zoom 1.3
                            with dissolve
                            chr_1 "Untuk urutan pertama yaitu int..."
                            chr_1 "Digunakan untuk merepresentasikan bilangan bulat, baik positif atau pun negatif"
                            chr_1 "Yang kedua, float..."
                            chr_1 "Digunakan untuk merepresentasikan bilangan desimal (bilangan dengan titik desimal)."
                            chr_1 "Lalu yang ketiga String..."
                            chr_1 "String atau bisa juga di sebut str, digunakan untuk merepresentasikan teks atau karakter."
                            chr_1 "Setelah itu yang keempat dan lima yaitu boolean,"
                            chr_1 "Digunakan untuk merepresentasikan nilai kebenaran, True (benar) atau False(Salah)."
                            hide sumi_open
                            show sumi at left :
                                yalign 0.1
                                zoom 1.2
                                xzoom -1
                            with dissolve
                            hide tipe_data with dissolve

                            hide miki
                            show miki_open at right :
                                yalign -0.3
                                zoom 1.18
                                xzoom -1   
                            with dissolve
                            chr_2 "Oh iya selain tipe data, kita bahas sedikit tentang jenis operator pada Python yuk!"
                            chr_2 "Sebelum menjelaskan kita pindah tempat dulu yuk diluar kelas, udah istirahat ini"
                            hide miki_open
                            show miki at right :
                                yalign -0.3
                                zoom 1.18
                                xzoom -1   
                            with dissolve
                            menu :
                                "Yuk !" :
                                    hide sumi
                                    show sumi_open at left :
                                        yalign 0.1
                                        zoom 1.2
                                        xzoom-1
                                    with dissolve
                                    chr_1 "Yuk !"
                                    hide sumi_open
                                    show sumi at left :
                                        yalign 0.1
                                        zoom 1.2
                                    with dissolve

                                    hide sumi with dissolve
                                    hide miki with dissolve
                                    
                                    jump jenis_operator

                        "Wahhh....." :
                            hide miki
                            show miki_open at right :
                                yalign -0.3
                                zoom 1.18
                                xzoom -1   
                            with dissolve 
                            chr_2 "Oh iya selain tipe data kita, kita bahas sedikit tentang jenis operator pada Python yuk!"
                            chr_2 "Sebelum menjelaskan kita pindah tempat dulu yuk diluar kelas, udah istirahat ini"
                            hide miki_open
                            show miki at right :
                                yalign -0.3
                                zoom 1.18   
                            with dissolve
                            menu :
                                "Yuk !" :
                                    hide sumi
                                    show sumi_open at left :
                                        yalign 0.1
                                        zoom 1.2
                                        xzoom-1
                                    with dissolve
                                    chr_1 "Yuk !"
                                    hide sumi_open
                                    show sumi at left :
                                        yalign 0.1
                                        zoom 1.2
                                    with dissolve
                                    hide sumi with dissolve
                                    hide miki with dissolve
                                    jump jenis_operator

        "Tipe data ? apakah semacam True False begitu ?" :
            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18
                xzoom -1   
            with dissolve
            chr_2 "Yap benar, untuk pengertiannya ...."
            chr_2 "Tipe data dalam pemrograman adalah cara untuk mengklasifikasikan dan mendefinisikan jenis data yang dapat disimpan dan diolah dalam program komputer."
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18   
            with dissolve

            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
                xzoom-1
            with dissolve
            chr_1 "Dan juga, Setiap tipe data memiliki karakteristik dan perilaku tertentu yang mempengaruhi bagaimana data tersebut diperlakukan dan dioperasikan."
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2
                xzoom-1
            with dissolve
            menu :
                "Kalau Tidak Salah Tipe Data Memiliki Banyak Jenis Apa Saja ?" :
                    hide sumi
                    show sumi_open at left :
                        yalign 0.1
                        zoom 1.2
                        xzoom-1
                    with dissolve
                    show tipe_data at center  :
                        xalign 0.6
                        yalign 0.4
                        zoom 1.3
                    with dissolve
                    chr_1 "Berikut tipe-tipenya"
                    hide sumi_open
                    show sumi at left :
                        yalign 0.1
                        zoom 1.2
                        xzoom -1
                    with dissolve
                    hide tipe_data
                    menu :
                        "Bisa kamu jelaskan lebih rincinya ?" :
                            hide sumi
                            show sumi_open at left :
                                yalign 0.1
                                zoom 1.2
                                xzoom-1
                            with dissolve
                            chr_1 "Tentu"
                            hide sumi_open
                            show sumi at left :
                                yalign 0.1
                                zoom 1.2
                                xzoom-1
                            with dissolve
                            show tipe_data at center  :
                                xalign 0.6
                                yalign 0.4
                                zoom 1.3
                            with dissolve

                            hide sumi
                            show sumi_open at left :
                                yalign 0.1
                                zoom 1.2
                                xzoom-1
                            with dissolve
                            chr_1 "Untuk urutan pertama yaitu int..."
                            chr_1 "Digunakan untuk merepresentasikan bilangan bulat, baik positif atau pun negatif"
                            chr_1 "Yang kedua, float..."
                            chr_1 "Digunakan untuk merepresentasikan bilangan desimal (bilangan dengan titik desimal)."
                            chr_1 "Lalu yang ketiga String..."
                            chr_1 "String atau bisa juga di sebut str, digunakan untuk merepresentasikan teks atau karakter."
                            chr_1 "Setelah itu yang keempat dan lima yaitu boolean,"
                            chr_1 "Digunakan untuk merepresentasikan nilai kebenaran, True (benar) atau False(Salah)."
                            hide sumi_open
                            show sumi at left :
                                yalign 0.1
                                zoom 1.2
                            with dissolve
                            hide tipe_data

                            hide miki
                            show miki_open at right :
                                yalign -0.3
                                zoom 1.18
                                xzoom -1   
                            with dissolve
                            chr_2 "Oke apakah kamu paham [player_name] ?"
                            hide miki_open
                            show miki at right :
                                yalign -0.3
                                zoom 1.18   
                            with dissolve
 
                            menu : 
                                "Lumayan" :
                                    hide miki
                                    show miki_open at right :
                                        yalign -0.3
                                        zoom 1.18
                                        xzoom -1   
                                    with dissolve
                                    chr_2 "Kalau sudah mari kita ke penjelasan berikutnya yaitu jenis-jenis operator"
                                    chr_2 "Sebelum menjelaskan kita pindah tempat dulu yuk diluar kelas, udah istirahat ini"
                                    hide miki_open
                                    show miki at right :
                                        yalign -0.3
                                        zoom 1.18   
                                    with dissolve
                                    menu :
                                        "Yuk !" :
                                            hide sumi
                                            show sumi_open at left :
                                                yalign 0.1
                                                zoom 1.2
                                                xzoom-1
                                            with dissolve
                                            chr_1 "Yuk !"
                                            hide sumi_open
                                            show sumi at left :
                                                yalign 0.1
                                                zoom 1.2
                                            with dissolve
                                            hide sumi with dissolve
                                            hide miki with dissolve
                                            jump jenis_operator
                                "Belum.." :
                                    hide miki
                                    show miki_open at right :
                                        yalign -0.3
                                        zoom 1.18
                                        xzoom -1   
                                    with dissolve
                                    chr_2 "Kalau belum paham, kamu bisa menanyakannya kepada CHATGPT atau Google lebih lanjut, [player_name] :)"
                                    chr_2 "Oke sekarang kita masuk ke jenis-jenis operator"
                                    chr_2 "Sebelum menjelaskan kita pindah tempat dulu yuk diluar kelas, udah istirahat ini"
                                    hide miki_open
                                    show miki at right :
                                        yalign -0.3
                                        zoom 1.18   
                                    with dissolve
                                    menu :
                                        "Yuk !" :
                                            hide sumi
                                            show sumi_open at left :
                                                yalign 0.1
                                                zoom 1.2
                                                xzoom-1
                                            with dissolve
                                            chr_1 "Yuk !"
                                            hide sumi_open
                                            show sumi at left :
                                                yalign 0.1
                                                zoom 1.2
                                            with dissolve
                                            hide sumi with dissolve
                                            hide miki with dissolve
                                            jump jenis_operator

# Scene luar kelas !
label jenis_operator :
    scene luarKelas
    show miki at right :
        yalign -0.3
        zoom 1.18
    with dissolve
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve
    play music "audio/luar-kelas/MySongYourNote_DDL.mp3" fadeout 1.0 fadein 1.0
    pause (0.5)

    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
    with dissolve
    chr_1 "[player_name],sebelum membahas apakah kamu tau operator pada python itu apa ??"
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve
    menu :
        "Tidak... aku pemula sama sekali belum tau...." :
            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
            with dissolve
            chr_1 "Oke, Miki apakah kamu bisa menjelaskannya ?"
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2
            with dissolve

            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18  
            with dissolve
            chr_2 "Okiii !"
            chr_2 "Operator dalam Python adalah simbol atau tanda yang digunakan untuk melakukan operasi pada nilai atau variabel. Operator digunakan untuk melakukan operasi matematika, perbandingan, logika, dan lainnya."
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18   
            with dissolve
            menu :
                "Lalu bagaimana dengan jenis jenis nya ?" :
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18   
                    with dissolve
                    chr_2 "Aku akan menjelaskannya sambil memberikan gambarnya ya!"
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18   
                    with dissolve

                    jump op_aritmatika

        "Aku cuman tau mengenai pengertiannya, Operator dalam Python adalah simbol atau tanda yang digunakan untuk melakukan operasi pada nilai atau variabel. Operator digunakan untuk melakukan operasi matematika, perbandingan, logika, dan lainnya." :
            chr_2 "Betul !"
            menu :
                "Lalu bagaimana dengan jenis-jenisnya ?" :
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18  
                    with dissolve
                    chr_2 "Aku akan menjelaskannya sambil memberikan gambarnya ya!"
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18   
                    with dissolve
                    jump op_aritmatika
# kesini
label op_aritmatika :
    image aritmatika = "Content/Jenis_Operator/aritmatika.png"
    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18  
    with dissolve
    chr_2 "Pertama tama Operator Aritmatika, adalah simbol atau tanda yang digunakan untuk melakukan operasi matematika pada operand (nilai atau variabel). "
    show aritmatika at center:
        yalign 0.1
        zoom 0.85 
    with moveinbottom
    hide miki_open
    show miki_open at right :
        yalign -0.3
        zoom 1.18  
    with dissolve
    chr_2 "Seperti inilah gambarnya, [player_name]"
    chr_2 "Pada penjumlahan a + b akan menghasilkan 15. Lalu pada pengurangan akan menjadi 5. Dan pada perkalian akan menjadi 50."
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18   
    with dissolve
    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
    with dissolve
    chr_1 "Selanjutnya pada pembagian akan menghasilkan 2 , dan pada Modulus akan mencari sisa bagi disini sisa bagi 0 karena 10 dibagi 5 menyisakan 0. dan pangkat akan menghasilkan 100.000."
    chr_1 "Selanjutnya pembagian bulat, Operator // mengembalikan hasil pembagian bulat dari a oleh b, yaitu berapa kali b dapat memasukkan a tanpa menghasilkan pecahan."
    chr_1 "Dalam hal ini, 5 dapat memasukkan 10 dua kali tanpa pecahan, sehingga hasilnya adalah 2. "
    chr_1 "Operator aritmatika digunakan untuk melakukan berbagai operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, pembagian, dan lainnya. "
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve

    hide aritmatika
    menu :
        "Wah ....." :
            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
                xzoom-1
            with dissolve
            chr_1 "Oke selanjutnya ada operator perbandingan !"
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2
            with dissolve
            menu :
                "Perbandingan ? semacam membandingkan begitu ?" :
                    hide sumi
                    show sumi_open at left :
                        yalign 0.1
                        zoom 1.2
                        xzoom-1
                    with dissolve
                    chr_1 "Yap betul !"
                    chr_1 "Yuk langsung kita bahas"
                    hide sumi_open
                    show sumi at left :
                        yalign 0.1
                        zoom 1.2
                    with dissolve
                    jump op_perbandingan
                "Apa itu ? bisa kamu jelaskan ?" :
                    hide sumi
                    show sumi_open at left :
                        yalign 0.1
                        zoom 1.2
                        xzoom-1
                    with dissolve
                    chr_1 "Ayo kita bahas lebih lanjut... sebelum itu apakah kamu sudah paham aritmatika tadi ?"
                    hide sumi_open
                    show sumi at left :
                        yalign 0.1
                        zoom 1.2
                    with dissolve
                    menu :
                        "Paham !" :
                            jump op_perbandingan
label op_perbandingan :
    image perbandingan = "Content/Jenis_Operator/perbandingan.png"
    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
    with dissolve
    chr_1 "Sebelum membahas contoh kode nya aku akan memberitahumu pengertiannya dulu.."
    chr_1 "Operator perbandingan dalam pemrograman adalah simbol atau tanda yang digunakan untuk membandingkan dua nilai atau ekspresi."
    chr_1 "Operator ini menghasilkan hasil berupa nilai kebenaran (True atau False) yang menunjukkan apakah perbandingan yang dilakukan adalah benar atau salah. "
    chr_1 "Operator perbandingan berguna untuk menguji hubungan antara dua nilai atau ekspresi dalam kondisi logika."
    chr_1 "Oke aku akan menunjukkan gambarnya ..."
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve

    show perbandingan at center :
        yalign 0.2
        zoom 0.8
    with moveinbottom

    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
        xzoom-1
        xalign -0.1
    with dissolve
    
    
    chr_1 "Ini gambarnya, [player_name]. Di gambar sudah beserta penjelasan jika kode di jalankan akan pasti menghasilkan antara True atau False tidak ada yang lain...."
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
        xzoom-1
        xalign -0.1
    with dissolve
    hide perbandingan
    menu :
        "Begitu ya... jadi ini untuk membandingkan apakah suatu variabel dinyatakan ada yang memenuhi ketentuan atau tidak ya ?..." :
            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
            with dissolve
            chr_1 "Yap betul ! untuk selanjut nya miki, jelaskan"
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2
            with dissolve
            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18   
            with dissolve
            chr_2 "Selanjutnya kita bahas operator logika"
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18  
            with dissolve
            pause (0.5)
            jump op_logika
        "Woww paham paham" :
            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
                xzoom -1
            with dissolve
            chr_1 "Sudah paham kan ?"
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2
            with dissolve
            menu :
                "Yap !" :
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18
                        xzoom -1   
                    with dissolve
                    chr_2 "Oke selanjutnya kita ke operator logika yuk !..."
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18
                        xzoom -1   
                    with dissolve
                    menu :
                        "Lesgo !" :
                            jump op_logika

label op_logika :
    image logika = "Content/Jenis_Operator/logika.png"
    show logika at center :
        yalign 0.4
        zoom 1.2
        xalign 0.4
    with dissolve
    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xalign 1.1   
    with dissolve
    chr_2 "Operator logika pada Python adalah operator yang digunakan untuk melakukan operasi logika pada nilai-nilai boolean (True atau False)."
    chr_2 "Operator logika ini digunakan untuk menggabungkan, membandingkan, atau memeriksa kebenaran dari ekspresi boolean."
    chr_2 "Berikut contoh gambar operator logika disertai dengan percabangan if else"
    hide logika
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18   
    with dissolve
    menu :
        "Jadi... jika salah satu variabel bernilai false maka akan menghasilkan false ya?" :
            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18
                xzoom -1   
            with dissolve   
            chr_2 "Yap, jadi apakah kamu sudah paham ??"
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18   
            with dissolve
            menu :
                "Sudah !" :
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18   
                    with dissolve 
                    chr_2 "Mari kita ke topik selanjutnya Yuk !"
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18   
                    with dissolve
                    jump op_penugasan
        "Jadi... kalau variabel keduanya benar atau true maka hasilnya true ya?" :
            hide sumi
            show sumi_open at left :
                yalign 0.1
                zoom 1.2
            with dissolve
            chr_1 "Paham ga nie?, [player_name]"
            hide sumi_open
            show sumi at left :
                yalign 0.1
                zoom 1.2
            with dissolve
            menu :
                "Sudah-Sudah miki..." :
                    hide miki
                    show miki_open at right :
                        yalign -0.3
                        zoom 1.18 
                    with dissolve
                    chr_2 "Oke, kita ke pembahasan selanjutnya Yuk !"
                    hide miki_open
                    show miki at right :
                        yalign -0.3
                        zoom 1.18   
                    with dissolve
                    jump op_penugasan

        "If Else ? apa itu ?" :
            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18  
            with dissolve
            chr_2 "Kamu belum tau tentang if else ya ?"
            chr_2 "Oke aku beritau deh..."
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18   
            with dissolve
            menu :
                "Iyanih heheeh, bolehhh...." :
                    jump if_else

label if_else :
    image img_if = "Content/Percabangan/if.png"
    image img_else = "Content/Percabangan/ifelse.png"
    image img_elif = "Content/Percabangan/elif.png"
    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18 
    with dissolve
    chr_2 "Percabangan adalah salah satu konsep fundamental dalam pemrograman yang memungkinkan kamu membuat keputusan berdasarkan kondisi yang diberikan."
    chr_2 "Ini memungkinkan program kamu untuk menjalankan blok kode tertentu jika suatu kondisi benar (true), dan blok kode lain jika kondisi salah (false)."
    chr_2 "Di python kita dapat menggunakan beberapa pernyataan untuk melakukan suatu percabangan, contohnya"
    show img_if at center :
        yalign 0.4
        zoom 1.2
        xalign 0.4
    with dissolve
    hide miki_open
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1
        xalign 1.05 
    with dissolve
    chr_2 "Pernyataan If saja, pernyataan yang memeriksa suatu kondisi dan menjalankan blok kode jika kondisi itu benar."
    hide img_if
    show img_else at center :
        yalign 0.4
        zoom 1.2
        xalign 0.4
    with dissolve
    hide miki_open
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1
        xalign 1.05 
    with dissolve
    chr_2 "Lalu dengan Else, jika kondisi dalam if tidak benar, blok kode dalam else akan dijalankan."
    hide img_else
    show img_elif at center :
        yalign 0.2
        zoom 1.2
    with dissolve
    hide miki_open
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1
        xalign 1.05 
    with dissolve
    chr_2 "Penggunaan if, elif, dan else bersamaan memungkinkan kamu untuk mengambil keputusan berdasarkan kondisi yang berbeda dalam program kamu."
    chr_2 "Ini adalah bagian penting dari logika kontrol dalam pemrograman yang memungkinkan kamu untuk menjalankan kode yang sesuai dengan situasi atau kondisi tertentu."
    
    hide img_elif with dissolve

    chr_2 "Oke selanjutnya kita ke operator Penugasan !"
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18   
    with dissolve
    menu :
        "Gass !" :
            jump op_penugasan


label op_penugasan :
    image penugasan = "Content/Jenis_Operator/penugasan.png"
    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18   
    with dissolve
    chr_2 "Oke untuk pembahasan jenis operator terakhir yaitu Operator Penugasan"
    chr_2 "Sumi apakah kamu bisa menjelaskannya ?"
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18   
    with dissolve

    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
    with dissolve
    chr_1 "Oke !!!"
    chr_1 "Operator penugasan (assignment operator) dalam pemrograman adalah operator yang digunakan untuk menginisialisasi atau mengganti nilai dari sebuah variabel. "
    chr_1 "Operator ini menghubungkan nilai di sebelah kanan operator dengan variabel di sebelah kiri operator."
    chr_1 "Tujuan dari operator penugasan adalah untuk memberikan nilai ke variabel agar dapat digunakan dalam operasi selanjutnya."
    hide sumi_open
    show sumi at left :
        yalign 0.1
        zoom 1.2
    with dissolve

    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1 
        xalign 1.1  
    with dissolve
    show penugasan at center :
        yalign 0.4
        zoom 1.2
        xalign 0.4
    with dissolve
    chr_2 "Berikut contoh kodenya,"
    chr_2 "Count yang tadinya 5 jika += akan menjadi 7. Dan juga saldo yang tadinya 1.000 di -= akan menjadi 800"
    hide penugasan
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18
        xzoom -1   
    with dissolve
    menu :
        "Begitu ya..." :
            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18   
            with dissolve
            chr_2 "Yappsss"
            chr_2 "Apakah kamu sudah paham ?"
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18   
            with dissolve
            menu : 
                "Paham-paham" :
                    hide sumi
                    show sumi_open at left :
                        yalign 0.1
                        zoom 1.2
                    with dissolve
                    chr_1 "Oke selanjutnya kita ke looping yuk"
                    hide sumi_open
                    show sumi at left :
                        yalign 0.1
                        zoom 1.2
                    with dissolve
                    menu :
                        "Yuk !" :
                            jump looping
            
        "Emmm..." :
            hide miki
            show miki_open at right :
                yalign -0.3
                zoom 1.18
                xzoom -1   
            with dissolve
            chr_2 "Yap.. selanjutnya kita ke looping, [player_name]"
            hide miki_open
            show miki at right :
                yalign -0.3
                zoom 1.18   
            with dissolve
            jump looping

    
label looping :
    image loop_for = "Content/Looping/loop_for.png"
    image loop_while = "Content/Looping/loop_while.png"
    image loop_enumerate = "Content/Looping/loop_enumerate.png"
    hide sumi
    show sumi_open at left :
        yalign 0.1
        zoom 1.2
        xzoom -1
    with dissolve
    chr_1 "Oke materi teraktir kita akan membahas macam macam looping..."
    chr_1 "Dalam konteks pemrograman Python, istilah `Looping` mengacu pada penggunaan struktur pengulangan (atau loop) untuk menjalankan serangkaian pernyataan atau tindakan berulang-ulang."
    chr_1 "Pengulangan memungkinkan Kamu menjalankan kode beberapa kali sesuai dengan kondisi atau iterasi yang ditentukan. Ada dua jenis loop yang umum digunakan di Python ."
    chr_1 "Ada Macam Macam Loop loh. Miki bisakah kamu menyebutkannya satu persatu?"
    # show sumi at left :
    #     yalign 0.1
    #     zoom 1.2
    #     xzoom -1
    # with dissolve

    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1   
    with dissolve
    chr_2 "Tentu Sumi !"
    hide sumi_open
    hide sumi
    chr_2 "Yang pertama ..."
    chr_2 "Loop For"
    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1   
    with dissolve
    show loop_for at center :
        yalign 0.4
        zoom 1.4
        xalign 0.4
    with dissolve 
    chr_2 "Kode di atas akan menghasilkan output 1,2,3,4,5"
    chr_2 "Python tidak memiliki loop foreach yang terpisah seperti bahasa lainnya sebaliknya, for digunakan untuk tugas tersebut."
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18
        xalign 1.05
        xzoom -1  
    with dissolve
    hide loop_for with dissolve
    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xalign 1.05
        xzoom -1
    chr_2 "Kedua..., Loop While"
    show loop_while at center :
        yalign 0.4
        zoom 1.2
        xalign 0.35
    with dissolve
    chr_2 "loop while yang akan berjalan selama variabel iterasi kurang dari 10"
    chr_2 "Outputnya adalah Iterasi ke-1 lalu Iterasi ke-2 dan seterusnya"
    chr_2 "Python tidak memiliki loop do-while bawaan seperti beberapa bahasa pemrograman lainnya."
    chr_2 "Namun, kamu dapat mensimulasikannya dengan menggabungkan loop while dengan penggunaan break untuk menghasilkan hasil yang serupa."

    hide loop_while with dissolve

    hide miki_open
    show miki_open at right :
        yalign -0.3
        zoom 1.18
        xzoom -1
        xalign 1.05 
    with dissolve
    chr_2 "Ketiga, Loop Menggunakan Enumerate"
    show loop_enumerate at center :
        yalign 0.4
        zoom 1.2
        xalign 0.21
    with dissolve
    chr_2 "Loop Enumerate digunakan untuk mengulang elemen-elemen dari sebuah iterable sambil melacak indeks atau nomor iterasi saat ini."
    chr_2 "Output kode diatas Buah ke-1: apel Buah ke-2: pisang Buah ke-3: ceri Buah ke-4: durian"
    chr_2 "Kamu dapat menggunakan fungsi enumerate bersama dengan loop for untuk mengakses indeks dan nilai dari elemen-elemen dalam sebuah urutan."
    hide loop_enumerate with dissolve
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18   
    with dissolve
    

    pause (0.4)
    show sumi at left :
        yalign 0.1
        zoom 1.2
        xzoom -1
    with dissolve
    hide miki
    show miki_open at right :
        yalign -0.3
        zoom 1.18  
    with dissolve 
    chr_2 "Apakah kamu sudah paham semua yang kami jelaskan, [player_name] ?"
    hide miki_open
    show miki at right :
        yalign -0.3
        zoom 1.18   
    with dissolve
    menu :
        "Yap" :
            hide miki
            hide sumi

            show miki_open at center :
                yalign -0.3
                zoom 1.18   
            with dissolve 
            chr_2 "Oke terimakasih materi kita sampai disini dulu ya"
            hide miki_open

            show sumi_open at center :
                yalign 0.1
                zoom 1.2
            with dissolve
            chr_1 "Terimakasih telah memainkan cerita kita !"
            hide sumi_open
            jump end

label end :
    show moderator at center
    with dissolve
    moderator "TAMAT.....!"
    moderator "Terimakasih telah Memainkan Game Sederhana ini.."
    pause