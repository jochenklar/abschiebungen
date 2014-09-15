from rest_framework import viewsets
from data.models import *
from data.serializers import *

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class AbschiebungBundeslaenderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AbschiebungBundeslaender.objects.all()
    serializer_class = AbschiebungBundeslaenderSerializer

class AbschiebungLandNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AbschiebungLandNationalitaet.objects.all()
    serializer_class = AbschiebungLandNationalitaetSerializer

class AbschiebungLandZielgebietViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AbschiebungLandZielgebiet.objects.all()
    serializer_class = AbschiebungLandZielgebietSerializer

class AbschiebungLuftwegFlughafenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AbschiebungLuftwegFlughafen.objects.all()
    serializer_class = AbschiebungLuftwegFlughafenSerializer

class AbschiebungLuftwegNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AbschiebungLuftwegNationalitaet.objects.all()
    serializer_class = AbschiebungLuftwegNationalitaetSerializer

class AbschiebungLuftwegZielgebietViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AbschiebungLuftwegZielgebiet.objects.all()
    serializer_class = AbschiebungLuftwegZielgebietSerializer

class AbschiebungSeewegNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AbschiebungSeewegNationalitaet.objects.all()
    serializer_class = AbschiebungSeewegNationalitaetSerializer

class AbschiebungSeewegZielgebietViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AbschiebungSeewegZielgebiet.objects.all()
    serializer_class = AbschiebungSeewegZielgebietSerializer

class AirlinesbegleitungViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Airlinesbegleitung.objects.all()
    serializer_class = AirlinesbegleitungSerializer

class FrontexabschiebungenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Frontexabschiebungen.objects.all()
    serializer_class = FrontexabschiebungenSerializer

class GescheitertFluggesellschaftFlughafenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GescheitertFluggesellschaftFlughafen.objects.all()
    serializer_class = GescheitertFluggesellschaftFlughafenSerializer

class GescheitertFluggesellschaftNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GescheitertFluggesellschaftNationalitaet.objects.all()
    serializer_class = GescheitertFluggesellschaftNationalitaetSerializer

class GescheitertMedizinischFlughafenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GescheitertMedizinischFlughafen.objects.all()
    serializer_class = GescheitertMedizinischFlughafenSerializer

class GescheitertMedizinischNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GescheitertMedizinischNationalitaet.objects.all()
    serializer_class = GescheitertMedizinischNationalitaetSerializer

class GescheitertWiderstandFlughafenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GescheitertWiderstandFlughafen.objects.all()
    serializer_class = GescheitertWiderstandFlughafenSerializer

class GescheitertWiderstandNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GescheitertWiderstandNationalitaet.objects.all()
    serializer_class = GescheitertWiderstandNationalitaetSerializer

class GruendeZurueckweisungenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GruendeZurueckweisungen.objects.all()
    serializer_class = GruendeZurueckweisungenSerializer

class TabellenbenennungenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tabellenbenennungen.objects.all()
    serializer_class = TabellenbenennungenSerializer

class UeberstellungHerkunftsstaatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UeberstellungHerkunftsstaat.objects.all()
    serializer_class = UeberstellungHerkunftsstaatSerializer

class UeberstellungZielgebietViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UeberstellungZielgebiet.objects.all()
    serializer_class = UeberstellungZielgebietSerializer

class ZurueckschiebungBundeslaenderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckschiebungBundeslaender.objects.all()
    serializer_class = ZurueckschiebungBundeslaenderSerializer

class ZurueckschiebungLandwegNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckschiebungLandwegNationalitaet.objects.all()
    serializer_class = ZurueckschiebungLandwegNationalitaetSerializer

class ZurueckschiebungLuftwegFlughafenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckschiebungLuftwegFlughafen.objects.all()
    serializer_class = ZurueckschiebungLuftwegFlughafenSerializer

class ZurueckschiebungLuftwegNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckschiebungLuftwegNationalitaet.objects.all()
    serializer_class = ZurueckschiebungLuftwegNationalitaetSerializer

class ZurueckschiebungLuftwegZielgebietViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckschiebungLuftwegZielgebiet.objects.all()
    serializer_class = ZurueckschiebungLuftwegZielgebietSerializer

class ZurueckweisungBundeslaenderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckweisungBundeslaender.objects.all()
    serializer_class = ZurueckweisungBundeslaenderSerializer

class ZurueckweisungLuftwegFlughafenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckweisungLuftwegFlughafen.objects.all()
    serializer_class = ZurueckweisungLuftwegFlughafenSerializer

class ZurueckweisungLuftwegGruendeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckweisungLuftwegGruende.objects.all()
    serializer_class = ZurueckweisungLuftwegGruendeSerializer

class ZurueckweisungLuftwegNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckweisungLuftwegNationalitaet.objects.all()
    serializer_class = ZurueckweisungLuftwegNationalitaetSerializer

class ZurueckweisungLuftwegZielgebietViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckweisungLuftwegZielgebiet.objects.all()
    serializer_class = ZurueckweisungLuftwegZielgebietSerializer

class ZurueckweisungSeewegGruendeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckweisungSeewegGruende.objects.all()
    serializer_class = ZurueckweisungSeewegGruendeSerializer

class ZurueckweisungschiebungMinderjaehrigNationalitaetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckweisungschiebungMinderjaehrigNationalitaet.objects.all()
    serializer_class = ZurueckweisungschiebungMinderjaehrigNationalitaetSerializer

class ZurueckweisungschiebungMinderjaehrigSeewegViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckweisungschiebungMinderjaehrigSeeweg.objects.all()
    serializer_class = ZurueckweisungschiebungMinderjaehrigSeewegSerializer

class ZurueckweisungschiebungMinderjaehrigZielgebietViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ZurueckweisungschiebungMinderjaehrigZielgebiet.objects.all()
    serializer_class = ZurueckweisungschiebungMinderjaehrigZielgebietSerializer
