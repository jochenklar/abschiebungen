from rest_framework import serializers
from data.models import *

class AbschiebungBundeslaenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungBundeslaender

class AbschiebungLandNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLandNationalitaet

class AbschiebungLandZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLandZielgebiet

class AbschiebungLuftwegFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLuftwegFlughafen

class AbschiebungLuftwegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLuftwegNationalitaet

class AbschiebungLuftwegZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungLuftwegZielgebiet

class AbschiebungSeewegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungSeewegNationalitaet

class AbschiebungSeewegZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AbschiebungSeewegZielgebiet

class AirlinesbegleitungSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Airlinesbegleitung

class FrontexabschiebungenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Frontexabschiebungen

class GescheitertFluggesellschaftFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertFluggesellschaftFlughafen

class GescheitertFluggesellschaftNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertFluggesellschaftNationalitaet

class GescheitertMedizinischFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertMedizinischFlughafen

class GescheitertMedizinischNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertMedizinischNationalitaet

class GescheitertWiderstandFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertWiderstandFlughafen

class GescheitertWiderstandNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GescheitertWiderstandNationalitaet

class GruendeZurueckweisungenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GruendeZurueckweisungen

class TabellenbenennungenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tabellenbenennungen

class UeberstellungHerkunftsstaatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UeberstellungHerkunftsstaat

class UeberstellungZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UeberstellungZielgebiet

class ZurueckschiebungBundeslaenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungBundeslaender

class ZurueckschiebungLandwegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungLandwegNationalitaet

class ZurueckschiebungLuftwegFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungLuftwegFlughafen

class ZurueckschiebungLuftwegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungLuftwegNationalitaet

class ZurueckschiebungLuftwegZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckschiebungLuftwegZielgebiet

class ZurueckweisungBundeslaenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungBundeslaender

class ZurueckweisungLuftwegFlughafenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungLuftwegFlughafen

class ZurueckweisungLuftwegGruendeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungLuftwegGruende

class ZurueckweisungLuftwegNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungLuftwegNationalitaet

class ZurueckweisungLuftwegZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungLuftwegZielgebiet

class ZurueckweisungSeewegGruendeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungSeewegGruende

class ZurueckweisungschiebungMinderjaehrigNationalitaetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungschiebungMinderjaehrigNationalitaet

class ZurueckweisungschiebungMinderjaehrigSeewegSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungschiebungMinderjaehrigSeeweg

class ZurueckweisungschiebungMinderjaehrigZielgebietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ZurueckweisungschiebungMinderjaehrigZielgebiet
















