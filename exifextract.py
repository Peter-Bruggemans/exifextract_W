# dit programma maakt gebruik van ExifTool by Phil Harvey http://www.sno.phy.queensu.ca/~phil/exiftool/
# laad de libraries
import os
from subprocess import check_output
 
# variabelen voor de broninstructieregel
broninstructie = "dir"
bronoptie = "/b/s"
brondrive = "e:/"
bronpad = "Peter Afbeeldingen/Archief/Scan0116"
bronbestand = "*.cr2"
 
# variablelen voor de doelinstructieregel
doelinstructie = "exiftool -T -canon"
doeloptie = ""
doeldrive = "e:/"
doelpad = ""
doelbestand = "test.txt"
 
# bouw de broninstructieregel
bronregel = broninstructie + ' "' + brondrive + bronpad + '/' + bronbestand + '"'
# pas de broninstructieregel aan aan het os(/ wordt \) en voeg de opties toe(/ moet blijven)
osbronregel = (os.path.normpath(bronregel)) + " " + bronoptie
 
# controle
#print (regel)
#print (osregel)
 
# voer de broninstructie uit
result=check_output(osbronregel, shell=True)
# verdeel het resultaat in regels
lines = result.split('\r\n')
# maak de doelinstructieregel aan per broninstructieregel
for line in lines:
    if len(line) > 0:
        # bouw de doelinstructieregel
        doelregel = doelinstructie + ' "' + line + '"' + ' >> ' + ' "' + doeldrive + doelpad + '/' + doelbestand + '"'
        # pas de broninstructieregel aan aan het os(/ wordt \) en voeg de opties toe(/ moet blijven)
        osdoelregel = (os.path.normpath(doelregel)) + " " + doeloptie
        # laat de doelinstructieregel zien
        print (osdoelregel)
        # voer de doelinstructieregel uit
        result2 = check_output(osdoelregel, shell=True)
