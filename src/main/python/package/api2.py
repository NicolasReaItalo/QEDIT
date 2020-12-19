import csv
import os

from tinydb import TinyDB


class Clip:
    def __init__(self, name, card, cadence, resolution, codec, duration, iso, shutter, wb, md5, csv):
        self.name = name
        self.card = card
        self.cadence = cadence
        self.resolution = resolution
        self.codec = codec
        self.duration = duration
        self.iso = iso
        self.shutter = shutter
        self.wb = wb
        self.md5 = md5
        self.circled = False
        self.sequence = "Seq"
        self.shot = "Plan"
        self.take = "Prise"
        self.comment = "Pas encore vérifié"
        self.alert_level = 0 # 0: remarque / 1: Avertissement / 2: Alerte
        self.csv = csv
        self.shooting_day = { "shooting_day_number": 0,
                              "shooting_date": "00-00-2000"}



    def circle_change(self):
        self.circled = not self.circled




    def temp_display_clip(self):
        print(self.name)
        print(f'durée: {self.duration} secondes / cadence: {self.cadence } im.s / carte: {self.card}')
        print(f'Sensibilité: {self.iso}  / Balance: {self.wb} / codec: {self.codec}  / Shutter : {self.shutter}' )
        print(f'Sequence: {self.sequence}  / Plan: {self.shot} / Prise: {self.take}')

        if self.circled:
            print('Cette prise est cerclée')
        else:
            print( "Cette prise n'est pas cerclée")

        print(f"commentaire: {self.comment}")
        print("________________________________________________________________________________")

    def clip_to_dict(self):
        dict ={
        "name": self.name,
        "card": self.card,
        "cadence": self.cadence,
        "resolution": self.resolution,
        "codec": self.codec,
        "duration": self.duration,
        "iso": self.iso,
        "shutter": self.shutter,
        "wb": self.wb,
        "md5": self.md5,
        "circled": self.circled,
        "sequence": self.sequence,
        "shot": self.shot,
        "take": self.take,
        "comment": self.comment,
        "csv": self.csv,
        "shooting_day": self.shooting_day

        }
        return dict




class Rapport:
    def __init__(self):
        self.report_name = ""
        self.report_number = 1
        self.director = ""
        self.cinematographer = ""
        self.film_title = ""
        self.production = ""
        self.framerate_list = []
        self.shooting_days = []
        self.clip_list = []
        self.all_card_list = []
        self.csv_list = []
        self.codec_list = []
        self.qc_date = {"day":1,"month":1,"year":1999}

    def csv_importer(self, csv_path):

        file = open(csv_path, newline='')
        reader = csv.reader(file)
        rows = [r for r in reader]
        # Recupération des index de chaque champ
        indexName = 0
        indexCadence = 0
        indexCarte = 0
        indexCodec = 0
        indexResolution = 0
        indexIso = 0
        indexWb = 0
        indexMD5 = 0
        indexDuration = 0
        indexShutter = 0

        i = 0
        while i < len(rows[0]):

            if rows[0][i] == "Name":
                indexName = i
            elif rows[0][i] == "Fps":
                indexCadence = i
            elif rows[0][i] == "Reel/Tape":
                indexCarte = i
            elif rows[0][i] == "Codec":
                indexCodec = i
            elif rows[0][i] == "Resolution":
                indexResolution = i
            elif rows[0][i] == "ASA":
                indexIso = i
            elif rows[0][i] == "Whitepoint":
                indexWb = i
            elif rows[0][i] == "Duration":
                indexDuration = i
            elif rows[0][i] == "Shutter":
                indexShutter = i
            elif rows[0][i] == "MD5":
                indexMD5 = i
            i += 1

        # On ajoute un objet clip dans clip_list par clip
        for row in rows:
            self.clip_list.append(
                Clip(row[indexName], row[indexCarte], row[indexCadence], row[indexResolution], row[indexCodec],
                     row[indexDuration], row[indexIso], row[indexShutter], row[indexWb], row[indexMD5],
                     os.path.basename(csv_path)))
        # on supprime le premier rang avec les place holders
        del self.clip_list[0]
       # On met à jour les listes de cartes/codec et csv importés
        self.refresh_all_card_list()
        self.refresh_csv_list()
        self.refresh_codec_list()


    def affichage_clips(self):
        for clip in self.clip_list:
            print(f"Clip n° {self.clip_list.index(clip) + 1}")
            clip.temp_display_clip()

    def refresh_all_card_list(self):
        for clip in self.clip_list:
            if clip.card not in self.all_card_list:
                self.all_card_list.append(clip.card)

    def refresh_csv_list(self):
        for clip in self.clip_list:
            if clip.csv not in self.csv_list:
                self.csv_list.append(clip.csv)

    def refresh_codec_list(self):
        for clip in self.clip_list:
            if clip.codec not in self.codec_list:
                self.codec_list.append(clip.codec)

    def refresh_framerate_list(self):
        for clip in self.clip_list:
            if clip.cadence not in self.framerate_list:
                self.framerate_list.append(clip.cadence)

    def save_report(self, path):
        db = TinyDB(path)
        db.drop_tables()
        header = db.table("header")
        header.insert({"film_title": self.film_title})
        header.insert({"director": self.director})
        header.insert({"cinematographer": self.cinematographer})
        header.insert({"production": self.production})
        header.insert({"report_number": self.report_number})
        header.insert({"qc_date": self.qc_date})
        header.insert({"shooting_days": self.shooting_days})
        header.insert({"csv_list": self.csv_list})
        header.insert({"card_list": self.all_card_list})
        clip_list = db.table("clip_list")
        for clip in self.clip_list:
            clip_list.insert(clip.clip_to_dict())

    def load_report(self, path):
        if not os.path.exists(path):
            return False
        db = TinyDB(path)
        header = db.table("header")
        self.film_title = header.get(doc_id=1)["film_title"]
        self.director = header.get(doc_id=2)["director"]
        self.cinematographer = header.get(doc_id=3)["cinematographer"]
        self.production = header.get(doc_id=4)["production"]
        self.report_number = header.get(doc_id=5)["report_number"]
        self.qc_date = header.get(doc_id=6)["qc_date"]
        self.shooting_days = header.get(doc_id=7)["shooting_days"]
        self.csv_list = header.get(doc_id=8)["csv_list"]
        self.all_card_list = header.get(doc_id=9)["card_list"]

        saved_clip_list = db.table("clip_list")
        self.clip_list.clear()
        for i in range(saved_clip_list.__len__()):
            clip = Clip("a", "b", "c", "d", "e",
                        "f", "g", "h", "i", "j",
                        "k")
            clip.name = saved_clip_list.get(doc_id=i + 1)["name"]
            clip.card = saved_clip_list.get(doc_id=i + 1)["card"]
            clip.cadence = saved_clip_list.get(doc_id=i + 1)["cadence"]
            clip.resolution = saved_clip_list.get(doc_id=i + 1)["resolution"]
            clip.codec = saved_clip_list.get(doc_id=i + 1)["codec"]
            clip.duration = saved_clip_list.get(doc_id=i + 1)["duration"]
            clip.iso = saved_clip_list.get(doc_id=i + 1)["iso"]
            clip.shutter = saved_clip_list.get(doc_id=i + 1)["shutter"]
            clip.wb = saved_clip_list.get(doc_id=i + 1)["wb"]
            clip.md5 = saved_clip_list.get(doc_id=i + 1)["md5"]
            clip.circled = saved_clip_list.get(doc_id=i + 1)["circled"]
            clip.sequence = saved_clip_list.get(doc_id=i + 1)["sequence"]
            clip.shot = saved_clip_list.get(doc_id=i + 1)["shot"]
            clip.take = saved_clip_list.get(doc_id=i + 1)["take"]
            clip.comment = saved_clip_list.get(doc_id=i + 1)["comment"]
            clip.csv = saved_clip_list.get(doc_id=i + 1)["csv"]
            clip.shooting_day = saved_clip_list.get(doc_id=i + 1)["shooting_day"]

            self.clip_list.append(clip)


    def show_report(self):
        print(self.film_title)
        print(self.director)
        print(self.cinematographer)
        print(self.production )
        print(self.framerate_list)
        print(self.report_number)
        print(self.shooting_days)
        print(self.csv_list)
        print(self.all_card_list )

    ## shooting days operations

    def create_shooting_day(self,number,day,month,year):
       # on verifie que ce numéro n'existe pas déjà
        for d in self.shooting_days:
            if d.get("number") == number:
                return False

        day = {"number":number,"day":day,"month":month,"year":year, "cards":[], "comment":""}
        self.shooting_days.append(day)
        return True

    def delete_shooting_day(self, number):
        i = 0
        while i < self.shooting_days.__len__():
            if self.shooting_days[i]["number"] == number:
                del self.shooting_days[i]
            i += 1

    def get_shooting_day(self,number):   # return the corresponding shooting day dict to the number
        for d in self.shooting_days:
            if d.get("number") == number:
                return d

    def get_shooting_date_from_number(self,number):  # return the corresponding shooting date as a list [d,m,y]
        for d in self.shooting_days:
            if d.get("number") == number:
                return [d.get("day"),d.get("month"),d.get("year")]

    def get_shooting_date_string_from_number(self,number):  # return the corresponding shooting date as a string [d,m,y]
        for d in self.shooting_days:
            if d.get("number") == number:
                j = d.get("day")
                m = d.get("month")
                y = d.get("year")
                return f"{j}/{m}/{y}"

    def set_shooting_day_comment(self,day_number,comment):

        for d in self.shooting_days:
            if d.get("number") == day_number:
                d["comment"] = comment









if __name__ == '__main__':
    test = Rapport()
    test.cinematographer = "Brissou"
    test.film_title = "Yo!"
    test.production = "Produit hi hi hi"
    test.csv_importer("/Users/user/Desktop/QCEdit/CSV/TEST.csv")



    test.create_shooting_day(0,19,10,1999)
    test.create_shooting_day(1,19,10,1999)
    test.create_shooting_day(2,19,10,1999)
    test.create_shooting_day(3,19,10,1999)


    for card in test.all_card_list:
       test.get_shooting_day(3).get("cards").append(card)
    test.save_report("/Users/user/Desktop/rapport_ok_02.json")

    print(test.get_shooting_date_from_number(2))

    #test.show_report()
