#!/usr/bin/python3
import time, threading, subprocess, sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
FFMPEGALKU="ffmpeg -y -i"
XTERM="xterm -e" # "xterm -hold -e"
##FORM_BEGIN##
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1018, 699)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 30, 41, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 63, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_avaaTiedostoNimi = QtWidgets.QLineEdit(Form)
        self.lineEdit_avaaTiedostoNimi.setGeometry(QtCore.QRect(140, 30, 471, 25))
        self.lineEdit_avaaTiedostoNimi.setObjectName("lineEdit_avaaTiedostoNimi")
        self.lineEdit_tallennaTiedostoNimi = QtWidgets.QLineEdit(Form)
        self.lineEdit_tallennaTiedostoNimi.setGeometry(QtCore.QRect(140, 60, 471, 25))
        self.lineEdit_tallennaTiedostoNimi.setObjectName("lineEdit_tallennaTiedostoNimi")
        self.pushButton_avaaTiedosto = QtWidgets.QPushButton(Form)
        self.pushButton_avaaTiedosto.setGeometry(QtCore.QRect(620, 30, 21, 24))
        self.pushButton_avaaTiedosto.setObjectName("pushButton_avaaTiedosto")
        self.pushButton_tallennaTiedosto = QtWidgets.QPushButton(Form)
        self.pushButton_tallennaTiedosto.setGeometry(QtCore.QRect(620, 60, 21, 24))
        self.pushButton_tallennaTiedosto.setObjectName("pushButton_tallennaTiedosto")
        self.listWidget_valitseTekstitys = QtWidgets.QListWidget(Form)
        self.listWidget_valitseTekstitys.setGeometry(QtCore.QRect(20, 140, 256, 341))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.listWidget_valitseTekstitys.setFont(font)
        self.listWidget_valitseTekstitys.setObjectName("listWidget_valitseTekstitys")
        self.listWidget_valitseAudio = QtWidgets.QListWidget(Form)
        self.listWidget_valitseAudio.setGeometry(QtCore.QRect(300, 140, 256, 341))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.listWidget_valitseAudio.setFont(font)
        self.listWidget_valitseAudio.setObjectName("listWidget_valitseAudio")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 141, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 120, 131, 17))
        self.label_4.setObjectName("label_4")
        self.listWidget_valitseTekstiTyyppi = QtWidgets.QListWidget(Form)
        self.listWidget_valitseTekstiTyyppi.setGeometry(QtCore.QRect(590, 140, 181, 192))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.listWidget_valitseTekstiTyyppi.setFont(font)
        self.listWidget_valitseTekstiTyyppi.setObjectName("listWidget_valitseTekstiTyyppi")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_valitseTekstiTyyppi.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_valitseTekstiTyyppi.addItem(item)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(600, 120, 131, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(600, 370, 131, 17))
        self.label_7.setObjectName("label_7")
        self.listWidget_tallennusFormaatti = QtWidgets.QListWidget(Form)
        self.listWidget_tallennusFormaatti.setGeometry(QtCore.QRect(590, 390, 181, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.listWidget_tallennusFormaatti.setFont(font)
        self.listWidget_tallennusFormaatti.setObjectName("listWidget_tallennusFormaatti")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_tallennusFormaatti.addItem(item)
        self.pushButton_aloita = QtWidgets.QPushButton(Form)
        self.pushButton_aloita.setGeometry(QtCore.QRect(20, 630, 83, 24))
        self.pushButton_aloita.setObjectName("pushButton_aloita")
        self.pushButton_paivitaEsikatselu = QtWidgets.QPushButton(Form)
        self.pushButton_paivitaEsikatselu.setGeometry(QtCore.QRect(20, 550, 191, 24))
        self.pushButton_paivitaEsikatselu.setObjectName("pushButton_paivitaEsikatselu")
        self.lineEdit_komennonEsikatselu = QtWidgets.QLineEdit(Form)
        self.lineEdit_komennonEsikatselu.setGeometry(QtCore.QRect(10, 590, 1001, 25))
        self.lineEdit_komennonEsikatselu.setObjectName("lineEdit_komennonEsikatselu")
        self.label_status = QtWidgets.QLabel(Form)
        self.label_status.setGeometry(QtCore.QRect(20, 670, 751, 17))
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "tstekstita"))
        self.label.setText(_translate("Form", "Avaa:"))
        self.label_2.setText(_translate("Form", "Tallenna:"))
        self.pushButton_avaaTiedosto.setText(_translate("Form", "..."))
        self.pushButton_tallennaTiedosto.setText(_translate("Form", "..."))
        self.label_3.setText(_translate("Form", "Valitse tekistitysraita:"))
        self.label_4.setText(_translate("Form", "Valitse audioraidat:"))
        __sortingEnabled = self.listWidget_valitseTekstiTyyppi.isSortingEnabled()
        self.listWidget_valitseTekstiTyyppi.setSortingEnabled(False)
        item = self.listWidget_valitseTekstiTyyppi.item(0)
        item.setText(_translate("Form", "Polta kuvaan"))
        item = self.listWidget_valitseTekstiTyyppi.item(1)
        item.setText(_translate("Form", "Sisällytä tekstinä"))
        self.listWidget_valitseTekstiTyyppi.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("Form", "Tekstityksen tyyppi:"))
        self.label_7.setText(_translate("Form", "Tallennusformaatti:"))
        __sortingEnabled = self.listWidget_tallennusFormaatti.isSortingEnabled()
        self.listWidget_tallennusFormaatti.setSortingEnabled(False)
        item = self.listWidget_tallennusFormaatti.item(0)
        item.setText(_translate("Form", "MP4"))
        self.listWidget_tallennusFormaatti.setSortingEnabled(__sortingEnabled)
        self.pushButton_aloita.setText(_translate("Form", "Aloita"))
        self.pushButton_paivitaEsikatselu.setText(_translate("Form", "Päivitä komennon esikatselu:"))
##FORM_END##
        
class txt2srt():
    def createSrt(temppiHakemisto):
        '''convert png images to text files and then text files to srt-file-'''
        import datetime, time, sys, os
        from pathlib import Path
        maxNayttoaika=10.0 # Tekstityksen maksimi näyttöaika sekunteina
        aikaOffset=0.0 # korjataan tekstityksen ajoitusta sekuntia
        def etsiValista( s, eka, vika ): #merkkijono josta etsitään sananA ja sananB välistä
            try:
                alku = s.index(eka) + len(eka)
                loppu = s.index( vika, alku )
                return s[alku:loppu]
            except ValueError:
                return ""
        
        if os.path.isfile(temppiHakemisto+"/subs.xml"): #************************ xml created by ccextactor ****
            kirjoitaSrt=open(temppiHakemisto+"/subs.srt", "w")
            with open(temppiHakemisto+"/subs.xml", "r") as fp:
                kierros=1 #Tämä on srt-tiedostoon tulostettava indeksi
                for rivi in fp:
                    if(len(rivi))>1:
                        rivi=rivi.rstrip()
                        if rivi.startswith("<spu"): #tällä rivillä tarvittavat tiedot
                            rivi=rivi.replace(",",".")
                            alku=aikaOffset+float(etsiValista(rivi,'start="','" end'))
                            #print(alku)
                            if alku<0: #jos aikaOffset vääntää pakkaselle
                                alku=0
                            loppu=aikaOffset+float(etsiValista(rivi,'end="','" image'))
                            if loppu<0: #jos aikaOffset vääntää pakkaselle
                                loppu=0
                            kesto=(loppu-alku)
                            if (kesto<0) or (kesto>maxNayttoaika): # jos näyttöaika liian lyhyt tai liian pitkä. liian lyhyt se voi olla kesken pätkäistyssä transport streamissa
                                loppu=alku+maxNayttoaika
                            falku=datetime.timedelta(seconds=float(alku))
                            salku="0"+str(falku)
                            if not "." in salku: #jos aika on tasasekunti ilman desimaalinollia, niin lisätään ne
                                salku+=".000000"
                            salku=salku[:-3].replace(".",",")
        
                            floppu=datetime.timedelta(seconds=float(loppu))
                            sloppu="0"+str(floppu)
                            if not "." in sloppu: #jos aika on tasasekunti ilman desimaalinollia, niin lisätään ne
                                sloppu+=".000000"
                            sloppu=sloppu[:-3].replace(".",",") #poistetaan lopusta kolme nollaa ja muutetaan piste pilkuksi
        
                            kuva=etsiValista(rivi,'image="','" xoffset')
                            numero=kuva[-8:-4]
                            steksti =  Path(temppiHakemisto+'/'+"subs.d"+"/sub"+numero+".png.txt").read_text() #luetaan kyseinen tekstitystiedosto
                            steksti=steksti.rstrip()
                            kirjoitaSrt.write(str(kierros)+"\n")
                            kirjoitaSrt.write(salku+" --> " +sloppu+"\n")
                            kirjoitaSrt.write(steksti+"\n\n")
                            kierros+=1
            kirjoitaSrt.close()
        
        
        elif os.path.isfile(temppiHakemisto+"/png/subs.xml"): #************************ xml created by subp2png ****
            kirjoitaSrt=open(temppiHakemisto+"/tekstit.srt", "w")
            with open(temppiHakemisto+"/png/subs.xml", "r") as fp:
                kierros=1 #Tämä on srt-tiedostoon tulostettava indeksi
                for rivi in fp:
                    if(len(rivi))>1:
                        rivi=rivi.rstrip()
                        if rivi.startswith("  <subtitle i"): #tällä rivillä tarvittavat tiedot
                            alku=etsiValista(rivi,'start="','" stop')
                            #sekAlku=aikaOffset+float(alku[6:])
                            #if sekAlku<0: #jos aikaOffset vääntää pakkaselle
                            #    sekAlku=0
                            loppu=etsiValista(rivi,'stop="','">')
                            #print(">"+loppu+"<")
                            #sekLoppu=aikaOffset+float(loppu[6:])
                            #if sekLoppu<0: #jos aikaOffset vääntää pakkaselle
                            #    sekLoppu=0         
                            alkuDateTime = datetime.datetime.strptime(alku, '%H:%M:%S.%f')+datetime.timedelta(seconds=aikaOffset)
                            loppuDateTime = datetime.datetime.strptime(loppu, '%H:%M:%S.%f')+datetime.timedelta(seconds=aikaOffset)
                            #tähän tsekkaa jos pakkaselle offsetin takia
                            salku=str(alkuDateTime)[11:-3]
                            sloppu=str(loppuDateTime)[11:-3]
                            diff=loppuDateTime-alkuDateTime
                            if diff.seconds>maxNayttoaika:
                                ssLoppu=str(alkuDateTime+datetime.timedelta(seconds=maxNayttoaika))[11:-3]
                            kuva=etsiValista(rivi,'id="','" start')
                            numero=("0000"+kuva)[-4:]
                            steksti =  Path(temppiHakemisto+'/'+"png"+"/subs"+numero+".png.txt").read_text() #luetaan kyseinen tekstitystiedosto
                            steksti=steksti.rstrip()
                            kirjoitaSrt.write(str(kierros)+"\n")
                            kirjoitaSrt.write(salku+" --> " +sloppu+"\n")
                            kirjoitaSrt.write(steksti+"\n\n")
                            kierros+=1
            kirjoitaSrt.close()         


class lomake():  
    def __init__(self):
        self.tempDir="/tmp/pyqttekstita"
        self.seis=False
        self.app = QtWidgets.QApplication(sys.argv)
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.Form)
        self.l = threading.Thread(name="looppi", target=self.looppi)
        self.l.start()        
        self.Form.show()
        self.ui.pushButton_avaaTiedosto.clicked.connect(self.avaaTiedosto)
        self.ui.pushButton_tallennaTiedosto.clicked.connect(self.tallennaTiedosto)
        self.ui.pushButton_paivitaEsikatselu.clicked.connect(self.paivitaEsikatselu)
        self.ui.pushButton_aloita.clicked.connect(self.aloitaMuunnos)
        self.app.aboutToQuit.connect(self.lopeta)
        self.ui.lineEdit_tallennaTiedostoNimi.setText("out.mp4")
        self.ui.listWidget_valitseTekstiTyyppi.setCurrentRow(0)
        self.ui.listWidget_tallennusFormaatti.setCurrentRow(0)
        self.makeTemp()
        sys.exit(self.app.exec_()) 
        
    def makeTemp(self): # /tmp/pyqttekstita/{0001 .... 9999}
        if not os.path.exists(self.tempDir):
            os.makedirs(self.tempDir)   
        listDir = os.listdir(self.tempDir)
        listDir.sort(reverse=True)
        if len(listDir)>0:
            lastDir=int(listDir[0])
        else:
            lastDir=0
        createDir=str(lastDir+1).zfill(4)
        self.tempDir=self.tempDir+"/"+createDir
        os.makedirs(self.tempDir) 
        
    def paivitaEsikatselu(self):
        global FFMPEGALKU
        audioMap=""
        videoMap=""
        vsubInput=""
        vsubMap=""
        if self.ui.listWidget_tallennusFormaatti.currentRow()==0: #MP4
            #print("tallentaa mp4")
            onkoRaspi = subprocess.check_output("cat /proc/cpuinfo |tail -n 1", shell=True).decode()
            if "Raspberry" in onkoRaspi:
                videoMap="-map 0:v -c:v h264_omx"
            else:
                videoMap="-map 0:v -c:v libx264"         
        
        valittuTekstiIndex=self.ui.listWidget_valitseTekstitys.currentRow()
        if self.subTracks[valittuTekstiIndex][3]=="DVB Subtitle": #Lähde on DVB-teksti
            #print("DVB subtitle valittu")
            if self.ui.listWidget_valitseTekstiTyyppi.currentRow()==0: #Polta kuvaan
                print("Polta kuvaan")
                vsubInput="-filter_complex '[0:v][i:"+self.subTracks[valittuTekstiIndex][2]+"]overlay'"
            elif self.ui.listWidget_valitseTekstiTyyppi.currentRow()==1: # Embedded teksti
                print("embedded teksti")
                vsubInput="-i "+self.tempDir+"/subs.srt"
                vsubMap="-map 1:s -c:s mov_text"
        elif self.subTracks[valittuTekstiIndex][3]=="Teletext Subtitle": #Lähde on teleteksti
            #print("teleteksti valittu")
            if self.ui.listWidget_valitseTekstiTyyppi.currentRow()==0: #Polta kuvaan
                #print("Polta kuvaan")
                vsubInput="-vf subtitles="+self.tempDir+"/subs.srt"
            elif self.ui.listWidget_valitseTekstiTyyppi.currentRow()==1: # Embedded teksti
                #print("embedded teksti")
                vsubInput="-i "+self.tempDir+"/subs.srt"
                vsubMap="-map 1:s -c:s mov_text"                
        for a in range(0,self.ui.listWidget_valitseAudio.model().rowCount()):
            tila=self.ui.listWidget_valitseAudio.item(a).checkState()
            if tila==QtCore.Qt.Checked:
                audioMap+="-map i:"+self.audioTracks[a][2]+" -c:a copy "

        komento=FFMPEGALKU+" '"+self.ui.lineEdit_avaaTiedostoNimi.text()+"' "+vsubInput+" "+videoMap+" "+audioMap+" "+vsubMap+" "+self.ui.lineEdit_tallennaTiedostoNimi.text()
        self.ui.lineEdit_komennonEsikatselu.setText(komento)
        self.app.processEvents()
        
        
        
    def aloitaMuunnos(self):
        global XTERM
        self.paivitaEsikatselu()
        valittuTekstiIndex=self.ui.listWidget_valitseTekstitys.currentRow()
        if self.ui.listWidget_valitseTekstiTyyppi.currentRow()==1: #graaafinen teksti ensin srt
            self.graafinen2srt()
            
        if self.subTracks[valittuTekstiIndex][3]=="Teletext Subtitle":
            ccCommand=XTERM+" "+"ccextractor -tpage "+self.subTracks[valittuTekstiIndex][2]+" -o "+self.tempDir+"/subs.srt '"+self.ui.lineEdit_avaaTiedostoNimi.text()+"'"
            self.ui.label_status.setText("ccextractor")
            self.app.processEvents()
            os.system(ccCommand)
            
        #print("muunnetaan")
        ffCommand=XTERM+" "+self.ui.lineEdit_komennonEsikatselu.text()
        self.ui.label_status.setText("ffmpeg")
        self.app.processEvents()       
        os.system(ffCommand)
        self.valmis()          
        
        
    def graafinen2srt(self): #Graafiset tekstit sisällytetyksi txt
        #print("graafinen2srt")
        valittuTekstiIndex=self.ui.listWidget_valitseTekstitys.currentRow()
        longSubLang="fin"
        if self.subTracks[valittuTekstiIndex][4]=="nl": longSubLang="nld"
        if self.subTracks[valittuTekstiIndex][4]=="da": longSubLang="dan"
        if self.subTracks[valittuTekstiIndex][4]=="sv": longSubLang="swe"
        if self.subTracks[valittuTekstiIndex][4]=="no": longSubLang="nor"
        ccCommand=XTERM+" "+"ccextractor -dvblang "+longSubLang+" -out=spupng -o "+self.tempDir+"/subs.xml -noteletext '"+self.ui.lineEdit_avaaTiedostoNimi.text()+"'"
        os.system(ccCommand)
        for file in os.listdir(self.tempDir+"/subs.d"):
            self.ui.label_status.setText("Käsitellään: "+str(file))
            self.app.processEvents()
            #print("FILE:",file)  
            convertParams="-trim -bordercolor black -border 50x5 -resize 300% -negate -alpha remove -background black"
            convCommand="convert "+self.tempDir+"/subs.d/"+file+" "+convertParams+" "+self.tempDir+"/subs.d/"+file+" >/dev/null 2>/dev/null" 
            #print(convCommand)
            os.system(convCommand)
            tesseCommand="tesseract -l "+longSubLang+" "+self.tempDir+"/subs.d/"+file+" "+self.tempDir+"/subs.d/"+file+" >/dev/null 2>/dev/null"
            os.system(tesseCommand)
        txt2srt.createSrt(self.tempDir)
  
            
    def avaaTiedosto(self):
        fname = QFileDialog.getOpenFileName()[0]
        self.ui.lineEdit_avaaTiedostoNimi.setText(fname)  
        self.ui.listWidget_valitseAudio.clear()
        self.ui.listWidget_valitseTekstitys.clear()
        self.subTracks=[] #[tulostettavanimi, type, pid, formaatti, kieli]
        self.audioTracks=[] #[tulostettavanimi, type, pid, formaatti, kieli]        
        #haetaan mediainfolla raidat:
        mkomento="mediainfo --output=JSON \""+fname+"\" |jq -r '.media.track[] | \"\(.\"@type\");\(.ID);\(.Format);\(.Language)\"'|head -n -1 "
        minfo=subprocess.check_output(mkomento, shell=True).decode()
        mitems=minfo.splitlines()
        for i in range(0, len(mitems)):
            #print(i, mitems[i])
            tyyppi, pid, formaatti, kieli = mitems[i].split(";")
            if tyyppi == "Text":
                if formaatti == "DVB Subtitle": #DVB subtitle pid int -> hex
                    pid=hex(int(pid))
                if formaatti =="Teletext Subtitle": #5000-699 -> 699
                    pid=pid.split("-")[1]
                tulostettava=kieli.upper()+" "+formaatti+" "+pid
                self.subTracks.append([tulostettava,tyyppi,pid,formaatti,kieli])
                self.ui.listWidget_valitseTekstitys.addItem(tulostettava)                
            if tyyppi == "Audio": # Audio pid int -> hex
                pid=hex(int(pid))
                tulostettava=kieli.upper()+" "+formaatti+" "+pid
                self.audioTracks.append([tulostettava,tyyppi,pid,formaatti,kieli])
                item = QtWidgets.QListWidgetItem()
                item.setCheckState(QtCore.Qt.Checked)
                item.setText(tulostettava)
                self.ui.listWidget_valitseAudio.addItem(item)                
            #print(tyyppi,pid,formaatti,kieli)
        self.ui.listWidget_valitseTekstitys.setCurrentRow(self.ui.listWidget_valitseTekstitys.model().rowCount()-1)
        #print(self.subTracks)
        #print(self.audioTracks)
    def tallennaTiedosto(self):
        fname = QFileDialog.getSaveFileName()[0]
        self.ui.lineEdit_tallennaTiedostoNimi.setText(fname)
         


        
    def lopeta(self):
        #print("quit")
        self.seis=True
        quit()
        
    def valmis(self):
        self.ui.label_status.setText("Valmis!")
        self.app.processEvents()
        
    def looppi(self):
        a=0
        
        while not self.seis: #mainloop
            #print("seis:",self.seis)
            time.sleep(5) 
            a+=1

if __name__ == "__main__":
    lo=lomake()
 
