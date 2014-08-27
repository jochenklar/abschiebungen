from django.db import models

class AbschiebungBundeslaender(models.Model):
    bundesland = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abschiebung_bundeslaender'

class AbschiebungLandNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abschiebung_land_nationalitaet'

class AbschiebungLandZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abschiebung_land_zielgebiet'

class AbschiebungLuftwegFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abschiebung_luftweg_flughafen'

class AbschiebungLuftwegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abschiebung_luftweg_nationalitaet'

class AbschiebungLuftwegZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abschiebung_luftweg_zielgebiet'

class AbschiebungSeewegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abschiebung_seeweg_nationalitaet'

class AbschiebungSeewegZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'abschiebung_seeweg_zielgebiet'

class Airlinesbegleitung(models.Model):
    luftfahrtunternehmen = models.CharField(max_length=256, blank=True)
    begleitet = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'airlinesbegleitung'

class Frontexabschiebungen(models.Model):
    datum = models.CharField(max_length=256, blank=True)
    zielland = models.CharField(max_length=256, blank=True)
    rueckzufuehrende = models.CharField(max_length=256, blank=True)
    bundesbeamte = models.CharField(max_length=256, blank=True)
    beteiligte_bundeslaender = models.CharField(max_length=256, blank=True)
    federfuehrender_staat_durchfuehrende_bundesbehoerde = models.CharField(max_length=256, blank=True)
    fluggesellschaft = models.CharField(max_length=256, blank=True)
    abflughafen = models.CharField(max_length=256, blank=True)
    kosten_fluggeraet = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'frontexabschiebungen'

class GescheitertFluggesellschaftFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'gescheitert_fluggesellschaft_flughafen'

class GescheitertFluggesellschaftNationalitaet(models.Model):
    luftverkehrsgesellschaft = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'gescheitert_fluggesellschaft_nationalitaet'

class GescheitertMedizinischFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'gescheitert_medizinisch_flughafen'

class GescheitertMedizinischNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'gescheitert_medizinisch_nationalitaet'

class GescheitertWiderstandFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'gescheitert_widerstand_flughafen'

class GescheitertWiderstandNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'gescheitert_widerstand_nationalitaet'

class GruendeZurueckweisungen(models.Model):
    col_1 = models.CharField(max_length=256, blank=True)
    col_2 = models.CharField(max_length=256, blank=True)
    class Meta:
        managed = False
        db_table = 'gruende_zurueckweisungen'

class Tabellenbenennungen(models.Model):
    tabellenname = models.CharField(max_length=256, blank=True)
    tabelleninhalt = models.CharField(max_length=256, blank=True)
    fragennummer_anfrage = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tabellenbenennungen'

class UeberstellungHerkunftsstaat(models.Model):
    herkunftsstaaten = models.CharField(max_length=256, blank=True)
    n = models.IntegerField(blank=True, null=True)
    davon_minderjaehrige_unter_18 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ueberstellung_herkunftsstaat'

class UeberstellungZielgebiet(models.Model):
    ueberstellungen_nach_mitgliedstaaten = models.CharField(max_length=256, blank=True)
    n = models.IntegerField(blank=True, null=True)
    davon_minderjaehrige_unter_18 = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ueberstellung_zielgebiet'

class ZurueckschiebungBundeslaender(models.Model):
    bundesland = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckschiebung_bundeslaender'

class ZurueckschiebungLandwegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    zurueckschiebungen_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckschiebung_landweg_nationalitaet'

class ZurueckschiebungLuftwegFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckschiebung_luftweg_flughafen'

class ZurueckschiebungLuftwegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckschiebung_luftweg_nationalitaet'

class ZurueckschiebungLuftwegZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckschiebung_luftweg_zielgebiet'

class ZurueckweisungBundeslaender(models.Model):
    bundesland = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckweisung_bundeslaender'

class ZurueckweisungLuftwegFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckweisung_luftweg_flughafen'

class ZurueckweisungLuftwegGruende(models.Model):
    nationalitaet = models.CharField(max_length=256, blank=True)
    gesamt = models.IntegerField(blank=True, null=True)
    a = models.IntegerField(blank=True, null=True)
    b = models.IntegerField(blank=True, null=True)
    c = models.IntegerField(blank=True, null=True)
    d = models.IntegerField(blank=True, null=True)
    e = models.IntegerField(blank=True, null=True)
    f = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)
    i = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckweisung_luftweg_gruende'

class ZurueckweisungLuftwegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckweisung_luftweg_nationalitaet'

class ZurueckweisungLuftwegZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckweisung_luftweg_zielgebiet'

class ZurueckweisungSeewegGruende(models.Model):
    nationalitaet = models.CharField(max_length=256, blank=True)
    gesamt = models.IntegerField(blank=True, null=True)
    a = models.IntegerField(blank=True, null=True)
    b = models.IntegerField(blank=True, null=True)
    c = models.IntegerField(blank=True, null=True)
    d = models.IntegerField(blank=True, null=True)
    e = models.IntegerField(blank=True, null=True)
    f = models.IntegerField(blank=True, null=True)
    g = models.IntegerField(blank=True, null=True)
    h = models.IntegerField(blank=True, null=True)
    i = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckweisung_seeweg_gruende'

class ZurueckweisungschiebungMinderjaehrigNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    anzahl = models.IntegerField(blank=True, null=True)
    davonzurueckgewiesen = models.IntegerField(blank=True, null=True)
    davonzurueckgeschoben = models.IntegerField(blank=True, null=True)
    davonuebergabe_an_jugendaemter = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckweisungschiebung_minderjaehrig_nationalitaet'

class ZurueckweisungschiebungMinderjaehrigSeeweg(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    zurueckweisungen_personen = models.IntegerField(blank=True, null=True)
    zurueckschiebungen_personen = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckweisungschiebung_minderjaehrig_seeweg'

class ZurueckweisungschiebungMinderjaehrigZielgebiet(models.Model):
    grenze = models.CharField(max_length=256, blank=True)
    anzahl = models.IntegerField(blank=True, null=True)
    zurueckweisungen = models.IntegerField(blank=True, null=True)
    zurueckschiebungen = models.IntegerField(blank=True, null=True)
    uebergabe_an_jugendaaemter = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zurueckweisungschiebung_minderjaehrig_zielgebiet'
