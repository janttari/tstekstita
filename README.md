# tstekstita
![](https://github.com/janttari/tstekstita/raw/master/tstekstita.png)

Työkalu transport stream-tiedostojen tekstityksen käsittelyyn.
Transport streamissa oleva tekstitys voi olla joko DVB-teksti tai teksti-tv-tekstitys.
Tekstitys voidaan polttaa kiinni kuvaan, tai siitä voidaan luoda MP4-tiedostoon sisällytetty tekstitys, jonka saa halutessaan
päälle ja pois. Luotu tiedosto toimii ainakin VLC-soittimella ja Enigma2-digiboksilla.

Ohjelman tarvitsemat riippuvuudet pitäisi asentua suorittamalla skripti "asenna-riippuvuudet"
Sen jälkeen ohjelma "tstekstita.py" avaa käyttöliittymän, jossa valitaan tiedosto ja tekstitys- ja audioraidat.
Painikkeella "Aloita" muunnostyö aloitetaan.


-----
paaikkuna.ui on Qt Designerillä tehty käyttöliittymä
paivita-ui on skripti joka injektoi käyttöliittymän varsinaiseen ohjelmaan, mikäli käyttöliittymää haluaa muuttaa.
Näitä tiedostoja et tarvitse, ellet halua ohjelmaan tehdä muutoksia.
