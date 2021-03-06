#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Country(models.Model):
    shortcut_two        = models.CharField(max_length=256, blank=True)
    shortcut_three      = models.CharField(max_length=256, blank=True)
    english_name        = models.CharField(max_length=256, blank=True)
    german_name         = models.CharField(max_length=256, blank=True)
    capital             = models.CharField(max_length=256, blank=True)
    lon                 = models.FloatField(blank=True, null=True)
    lat                 = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.english_name)

class AbschiebungBundeslaender(models.Model):
    bundesland = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class AbschiebungLandNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    staatsangehoerigkeit_country = models.ForeignKey('Country', blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class AbschiebungLandZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class AbschiebungLuftwegFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class AbschiebungLuftwegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    staatsangehoerigkeit_country = models.ForeignKey('Country', blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class AbschiebungLuftwegZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    zielstaat_zielgebiet_country = models.ForeignKey('Country', blank=True, null=True)

class AbschiebungSeewegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class AbschiebungSeewegZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    zielstaat_zielgebiet_country = models.ForeignKey('Country', blank=True, null=True)

class Airlinesbegleitung(models.Model):
    luftfahrtunternehmen = models.CharField(max_length=256, blank=True)
    begleitet = models.IntegerField(blank=True, null=True)

class Frontexabschiebungen(models.Model):
    datum = models.CharField(max_length=256, blank=True)
    zielland = models.CharField(max_length=256, blank=True)
    zielland_country = models.ForeignKey('Country', blank=True, null=True)
    rueckzufuehrende = models.CharField(max_length=256, blank=True)
    bundesbeamte = models.CharField(max_length=256, blank=True)
    beteiligte_bundeslaender = models.CharField(max_length=256, blank=True)
    federfuehrender_staat_durchfuehrende_bundesbehoerde = models.CharField(max_length=256, blank=True)
    fluggesellschaft = models.CharField(max_length=256, blank=True, null=True)
    abflughafen = models.CharField(max_length=256, blank=True, null=True)
    kosten_fluggeraet = models.CharField(max_length=256, blank=True, null=True)

class GescheitertFluggesellschaftFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class GescheitertFluggesellschaftNationalitaet(models.Model):
    luftverkehrsgesellschaft = models.CharField(max_length=256, blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class GescheitertMedizinischFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class GescheitertMedizinischNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True, null=True)
    staatsangehoerigkeit_country = models.ForeignKey('Country', blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class GescheitertWiderstandFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class GescheitertWiderstandNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True, null=True)
    staatsangehoerigkeit_country = models.ForeignKey('Country', blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class GruendeZurueckweisungen(models.Model):
    col_1 = models.CharField(max_length=256, blank=True, null=True)
    col_2 = models.CharField(max_length=256, blank=True, null=True)

class Tabellenbenennungen(models.Model):
    tabellenname = models.CharField(max_length=256, blank=True, null=True)
    tabelleninhalt = models.CharField(max_length=256, blank=True, null=True)
    fragennummer_anfrage = models.IntegerField(blank=True, null=True)

class UeberstellungHerkunftsstaat(models.Model):
    herkunftsstaaten = models.CharField(max_length=256, blank=True, null=True)
    herkunftsstaaten_country = models.ForeignKey('Country', blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)
    davon_minderjaehrige_unter_18 = models.IntegerField(blank=True, null=True)

class UeberstellungZielgebiet(models.Model):
    ueberstellungen_nach_mitgliedstaaten = models.CharField(max_length=256, blank=True)
    ueberstellungen_nach_mitgliedstaaten_country = models.ForeignKey('Country', blank=True, null=True)
    n = models.IntegerField(blank=True, null=True)
    davon_minderjaehrige_unter_18 = models.IntegerField(blank=True, null=True)

class ZurueckschiebungBundeslaender(models.Model):
    bundesland = models.CharField(max_length=256, blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class ZurueckschiebungLandwegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True, null=True)
    staatsangehoerigkeit_country = models.ForeignKey('Country', blank=True, null=True)
    zurueckschiebungen_personen = models.IntegerField(blank=True, null=True)

class ZurueckschiebungLuftwegFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class ZurueckschiebungLuftwegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True, null=True)
    staatsangehoerigkeit_country = models.ForeignKey('Country', blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class ZurueckschiebungLuftwegZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True, null=True)
    zielstaat_zielgebiet_country = models.ForeignKey('Country', blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class ZurueckweisungBundeslaender(models.Model):
    bundesland = models.CharField(max_length=256, blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class ZurueckweisungLuftwegFlughafen(models.Model):
    flughafen = models.CharField(max_length=256, blank=True, null=True)
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class ZurueckweisungLuftwegGruende(models.Model):
    nationalitaet = models.CharField(max_length=256, blank=True, null=True)
    nationalitaet_country = models.ForeignKey('Country', blank=True, null=True)    
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

class ZurueckweisungLuftwegNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True, null=True)
    staatsangehoerigkeit_country = models.ForeignKey('Country', blank=True, null=True) 
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class ZurueckweisungLuftwegZielgebiet(models.Model):
    zielstaat_zielgebiet = models.CharField(max_length=256, blank=True, null=True)
    zielstaat_zielgebiet_country = models.ForeignKey('Country', blank=True, null=True) 
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)

class ZurueckweisungSeewegGruende(models.Model):
    nationalitaet = models.CharField(max_length=256, blank=True, null=True)
    nationalitaet_country = models.ForeignKey('Country', blank=True, null=True) 
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

class ZurueckweisungschiebungMinderjaehrigNationalitaet(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True, null=True)
    staatsangehoerigkeit_country = models.ForeignKey('Country', blank=True, null=True) 
    anzahl = models.IntegerField(blank=True, null=True)
    davonzurueckgewiesen = models.IntegerField(blank=True, null=True)
    davonzurueckgeschoben = models.IntegerField(blank=True, null=True)
    davonuebergabe_an_jugendaemter = models.IntegerField(blank=True, null=True)

class ZurueckweisungschiebungMinderjaehrigSeeweg(models.Model):
    staatsangehoerigkeit = models.CharField(max_length=256, blank=True, null=True)
    staatsangehoerigkeit_country = models.ForeignKey('Country', blank=True, null=True) 
    gesamtzahl_personen = models.IntegerField(blank=True, null=True)
    zurueckweisungen_personen = models.IntegerField(blank=True, null=True)
    zurueckschiebungen_personen = models.IntegerField(blank=True, null=True)

class ZurueckweisungschiebungMinderjaehrigZielgebiet(models.Model):
    grenze = models.CharField(max_length=256, blank=True, null=True)
    anzahl = models.IntegerField(blank=True, null=True)
    zurueckweisungen = models.IntegerField(blank=True, null=True)
    zurueckschiebungen = models.IntegerField(blank=True, null=True)
    uebergabe_an_jugendaaemter = models.IntegerField(blank=True, null=True)
