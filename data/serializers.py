from rest_framework import serializers
from data.models import *


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country 
        #fields = ('shortcut_two', 'shortcut_three', 'english_name', 'german_name')       

class AbschiebungBundeslaenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungBundeslaender  
        depth = 2      

class AbschiebungLandNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLandNationalitaet
        depth = 2

class AbschiebungLandZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLandZielgebiet
        depth = 2

class AbschiebungLuftwegFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLuftwegFlughafen
        depth = 2

class AbschiebungLuftwegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLuftwegNationalitaet
        depth = 2

class AbschiebungLuftwegZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLuftwegZielgebiet
        depth = 2

class AbschiebungSeewegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungSeewegNationalitaet
        depth = 2

class AbschiebungSeewegZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungSeewegZielgebiet
        depth = 2

class AirlinesbegleitungSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airlinesbegleitung
        depth = 2

class FrontexabschiebungenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Frontexabschiebungen
        depth = 2

class GescheitertFluggesellschaftFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertFluggesellschaftFlughafen
        depth = 2

class GescheitertFluggesellschaftNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertFluggesellschaftNationalitaet
        depth = 2

class GescheitertMedizinischFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertMedizinischFlughafen
        depth = 2

class GescheitertMedizinischNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertMedizinischNationalitaet
        depth = 2

class GescheitertWiderstandFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertWiderstandFlughafen
        depth = 2

class GescheitertWiderstandNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertWiderstandNationalitaet
        depth = 2

class GruendeZurueckweisungenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GruendeZurueckweisungen
        depth = 2

class TabellenbenennungenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tabellenbenennungen
        depth = 2

class UeberstellungHerkunftsstaatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UeberstellungHerkunftsstaat
        depth = 2

class UeberstellungZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UeberstellungZielgebiet
        depth = 2

class ZurueckschiebungBundeslaenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungBundeslaender
        depth = 2

class ZurueckschiebungLandwegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungLandwegNationalitaet
        depth = 2

class ZurueckschiebungLuftwegFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungLuftwegFlughafen
        depth = 2

class ZurueckschiebungLuftwegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungLuftwegNationalitaet
        depth = 2

class ZurueckschiebungLuftwegZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungLuftwegZielgebiet
        depth = 2

class ZurueckweisungBundeslaenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungBundeslaender
        depth = 2

class ZurueckweisungLuftwegFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungLuftwegFlughafen
        depth = 2

class ZurueckweisungLuftwegGruendeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungLuftwegGruende
        depth = 2

class ZurueckweisungLuftwegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungLuftwegNationalitaet
        depth = 2

class ZurueckweisungLuftwegZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungLuftwegZielgebiet

class ZurueckweisungSeewegGruendeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungSeewegGruende
        depth = 2

class ZurueckweisungschiebungMinderjaehrigNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungschiebungMinderjaehrigNationalitaet
        depth = 2

class ZurueckweisungschiebungMinderjaehrigSeewegSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungschiebungMinderjaehrigSeeweg
        depth = 2

class ZurueckweisungschiebungMinderjaehrigZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungschiebungMinderjaehrigZielgebiet
        depth = 2
















