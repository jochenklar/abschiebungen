from rest_framework import viewsets
from data.models import *
from data.serializers import *

class AbschiebungBundeslaenderViewSet(viewsets.ModelViewSet):
    queryset = AbschiebungBundeslaender.objects.all()
    serializer_class = AbschiebungBundeslaenderSerializer

class AbschiebungLandNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = AbschiebungLandNationalitaet.objects.all()
    serializer_class = AbschiebungLandNationalitaetSerializer

class AbschiebungLandZielgebietViewSet(viewsets.ModelViewSet):
    queryset = AbschiebungLandZielgebiet.objects.all()
    serializer_class = AbschiebungLandZielgebietSerializer

class AbschiebungLuftwegFlughafenViewSet(viewsets.ModelViewSet):
    queryset = AbschiebungLuftwegFlughafen.objects.all()
    serializer_class = AbschiebungLuftwegFlughafenSerializer

class AbschiebungLuftwegNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = AbschiebungLuftwegNationalitaet.objects.all()
    serializer_class = AbschiebungLuftwegNationalitaetSerializer

class AbschiebungLuftwegZielgebietViewSet(viewsets.ModelViewSet):
    queryset = AbschiebungLuftwegZielgebiet.objects.all()
    serializer_class = AbschiebungLuftwegZielgebietSerializer

class AbschiebungSeewegNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = AbschiebungSeewegNationalitaet.objects.all()
    serializer_class = AbschiebungSeewegNationalitaetSerializer

class AbschiebungSeewegZielgebietViewSet(viewsets.ModelViewSet):
    queryset = AbschiebungSeewegZielgebiet.objects.all()
    serializer_class = AbschiebungSeewegZielgebietSerializer

class AirlinesbegleitungViewSet(viewsets.ModelViewSet):
    queryset = Airlinesbegleitung.objects.all()
    serializer_class = AirlinesbegleitungSerializer

class FrontexabschiebungenViewSet(viewsets.ModelViewSet):
    queryset = Frontexabschiebungen.objects.all()
    serializer_class = FrontexabschiebungenSerializer

class GescheitertFluggesellschaftFlughafenViewSet(viewsets.ModelViewSet):
    queryset = GescheitertFluggesellschaftFlughafen.objects.all()
    serializer_class = GescheitertFluggesellschaftFlughafenSerializer

class GescheitertFluggesellschaftNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = GescheitertFluggesellschaftNationalitaet.objects.all()
    serializer_class = GescheitertFluggesellschaftNationalitaetSerializer

class GescheitertMedizinischFlughafenViewSet(viewsets.ModelViewSet):
    queryset = GescheitertMedizinischFlughafen.objects.all()
    serializer_class = GescheitertMedizinischFlughafenSerializer

class GescheitertMedizinischNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = GescheitertMedizinischNationalitaet.objects.all()
    serializer_class = GescheitertMedizinischNationalitaetSerializer

class GescheitertWiderstandFlughafenViewSet(viewsets.ModelViewSet):
    queryset = GescheitertWiderstandFlughafen.objects.all()
    serializer_class = GescheitertWiderstandFlughafenSerializer

class GescheitertWiderstandNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = GescheitertWiderstandNationalitaet.objects.all()
    serializer_class = GescheitertWiderstandNationalitaetSerializer

class GruendeZurueckweisungenViewSet(viewsets.ModelViewSet):
    queryset = GruendeZurueckweisungen.objects.all()
    serializer_class = GruendeZurueckweisungenSerializer

class TabellenbenennungenViewSet(viewsets.ModelViewSet):
    queryset = Tabellenbenennungen.objects.all()
    serializer_class = TabellenbenennungenSerializer

class UeberstellungHerkunftsstaatViewSet(viewsets.ModelViewSet):
    queryset = UeberstellungHerkunftsstaat.objects.all()
    serializer_class = UeberstellungHerkunftsstaatSerializer

class UeberstellungZielgebietViewSet(viewsets.ModelViewSet):
    queryset = UeberstellungZielgebiet.objects.all()
    serializer_class = UeberstellungZielgebietSerializer

class ZurueckschiebungBundeslaenderViewSet(viewsets.ModelViewSet):
    queryset = ZurueckschiebungBundeslaender.objects.all()
    serializer_class = ZurueckschiebungBundeslaenderSerializer

class ZurueckschiebungLandwegNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = ZurueckschiebungLandwegNationalitaet.objects.all()
    serializer_class = ZurueckschiebungLandwegNationalitaetSerializer

class ZurueckschiebungLuftwegFlughafenViewSet(viewsets.ModelViewSet):
    queryset = ZurueckschiebungLuftwegFlughafen.objects.all()
    serializer_class = ZurueckschiebungLuftwegFlughafenSerializer

class ZurueckschiebungLuftwegNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = ZurueckschiebungLuftwegNationalitaet.objects.all()
    serializer_class = ZurueckschiebungLuftwegNationalitaetSerializer

class ZurueckschiebungLuftwegZielgebietViewSet(viewsets.ModelViewSet):
    queryset = ZurueckschiebungLuftwegZielgebiet.objects.all()
    serializer_class = ZurueckschiebungLuftwegZielgebietSerializer

class ZurueckweisungBundeslaenderViewSet(viewsets.ModelViewSet):
    queryset = ZurueckweisungBundeslaender.objects.all()
    serializer_class = ZurueckweisungBundeslaenderSerializer

class ZurueckweisungLuftwegFlughafenViewSet(viewsets.ModelViewSet):
    queryset = ZurueckweisungLuftwegFlughafen.objects.all()
    serializer_class = ZurueckweisungLuftwegFlughafenSerializer

class ZurueckweisungLuftwegGruendeViewSet(viewsets.ModelViewSet):
    queryset = ZurueckweisungLuftwegGruende.objects.all()
    serializer_class = ZurueckweisungLuftwegGruendeSerializer

class ZurueckweisungLuftwegNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = ZurueckweisungLuftwegNationalitaet.objects.all()
    serializer_class = ZurueckweisungLuftwegNationalitaetSerializer

class ZurueckweisungLuftwegZielgebietViewSet(viewsets.ModelViewSet):
    queryset = ZurueckweisungLuftwegZielgebiet.objects.all()
    serializer_class = ZurueckweisungLuftwegZielgebietSerializer

class ZurueckweisungSeewegGruendeViewSet(viewsets.ModelViewSet):
    queryset = ZurueckweisungSeewegGruende.objects.all()
    serializer_class = ZurueckweisungSeewegGruendeSerializer

class ZurueckweisungschiebungMinderjaehrigNationalitaetViewSet(viewsets.ModelViewSet):
    queryset = ZurueckweisungschiebungMinderjaehrigNationalitaet.objects.all()
    serializer_class = ZurueckweisungschiebungMinderjaehrigNationalitaetSerializer

class ZurueckweisungschiebungMinderjaehrigSeewegViewSet(viewsets.ModelViewSet):
    queryset = ZurueckweisungschiebungMinderjaehrigSeeweg.objects.all()
    serializer_class = ZurueckweisungschiebungMinderjaehrigSeewegSerializer

class ZurueckweisungschiebungMinderjaehrigZielgebietViewSet(viewsets.ModelViewSet):
    queryset = ZurueckweisungschiebungMinderjaehrigZielgebiet.objects.all()
    serializer_class = ZurueckweisungschiebungMinderjaehrigZielgebietSerializer
