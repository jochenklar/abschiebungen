DROP TABLE IF EXISTS "abschiebung_land_nationalitaet";
CREATE TABLE "abschiebung_land_nationalitaet" ("staatsangehoerigkeit" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "abschiebung_land_zielgebiet";
CREATE TABLE "abschiebung_land_zielgebiet" ("zielstaat_zielgebiet" VARCHAR(256), "gesamtzahl_personen"  INTEGER);

DROP TABLE IF EXISTS "abschiebung_luftweg_flughafen";
CREATE TABLE "abschiebung_luftweg_flughafen" ("flughafen" VARCHAR(256), "gesamtzahl_personen"  INTEGER);

DROP TABLE IF EXISTS "abschiebung_luftweg_nationalitaet";
CREATE TABLE "abschiebung_luftweg_nationalitaet" ("staatsangehoerigkeit" VARCHAR(256), "gesamtzahl_personen"  INTEGER);

DROP TABLE IF EXISTS "abschiebung_luftweg_zielgebiet";
CREATE TABLE "abschiebung_luftweg_zielgebiet" ("zielstaat_zielgebiet" VARCHAR(256), "gesamtzahl_personen"  INTEGER);

DROP TABLE IF EXISTS "abschiebung_seeweg_nationalitaet";
CREATE TABLE "abschiebung_seeweg_nationalitaet" ("staatsangehoerigkeit" VARCHAR(256), "gesamtzahl_personen"  INTEGER);

DROP TABLE IF EXISTS "abschiebung_seeweg_zielgebiet";
CREATE TABLE "abschiebung_seeweg_zielgebiet" ("zielstaat_zielgebiet" VARCHAR(256), "gesamtzahl_personen"  INTEGER);

DROP TABLE IF EXISTS "abschiebung_bundeslaender";
CREATE TABLE "abschiebung_bundeslaender" ("bundesland" VARCHAR(256), "gesamtzahl_personen"  INTEGER);

DROP TABLE IF EXISTS "airlinesbegleitung";
CREATE TABLE "airlinesbegleitung" ("luftfahrtunternehmen" VARCHAR(256), "begleitet" INTEGER);

DROP TABLE IF EXISTS "frontexabschiebungen";
CREATE TABLE "frontexabschiebungen" ("datum" VARCHAR(256), "zielland" VARCHAR(256), "rueckzufuehrende" VARCHAR(256), "bundesbeamte" VARCHAR(256), "beteiligte_bundeslaender" VARCHAR(256), "federfuehrender_staat_durchfuehrende_bundesbehoerde" VARCHAR(256), "fluggesellschaft" VARCHAR(256), "abflughafen" VARCHAR(256), "kosten_fluggeraet" VARCHAR(256));

DROP TABLE IF EXISTS "gescheitert_fluggesellschaft_flughafen";
CREATE TABLE "gescheitert_fluggesellschaft_flughafen" ("flughafen" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "gescheitert_fluggesellschaft_nationalitaet";
CREATE TABLE "gescheitert_fluggesellschaft_nationalitaet" ("luftverkehrsgesellschaft" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "gescheitert_medizinisch_flughafen";
CREATE TABLE "gescheitert_medizinisch_flughafen" ("flughafen" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "gescheitert_medizinisch_nationalitaet";
CREATE TABLE "gescheitert_medizinisch_nationalitaet" ("staatsangehoerigkeit" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "gescheitert_widerstand_flughafen";
CREATE TABLE "gescheitert_widerstand_flughafen" ("flughafen" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "gescheitert_widerstand_nationalitaet";
CREATE TABLE "gescheitert_widerstand_nationalitaet" ("staatsangehoerigkeit" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "gruende_zurueckweisungen";
CREATE TABLE "gruende_zurueckweisungen" ("col_1" VARCHAR(256), "col_2" VARCHAR(256));

DROP TABLE IF EXISTS "tabellenbenennungen";
CREATE TABLE "tabellenbenennungen" ("tabellenname" VARCHAR(256), "tabelleninhalt" VARCHAR(256), "fragennummer_anfrage" INTEGER);

DROP TABLE IF EXISTS "zurueckweisungschiebung_minderjaehrig_nationalitaet";
CREATE TABLE "zurueckweisungschiebung_minderjaehrig_nationalitaet" ("staatsangehoerigkeit" VARCHAR(256), "anzahl" INTEGER, "davonzurueckgewiesen" INTEGER, "davonzurueckgeschoben" INTEGER, "davonuebergabe_an_jugendaemter" INTEGER);

DROP TABLE IF EXISTS "zurueckweisungschiebung_minderjaehrig_zielgebiet";
CREATE TABLE "zurueckweisungschiebung_minderjaehrig_zielgebiet" ("grenze" VARCHAR(256), "anzahl" INTEGER, "zurueckweisungen" INTEGER, "zurueckschiebungen" INTEGER, "uebergabe_an_jugendaaemter" INTEGER);

DROP TABLE IF EXISTS "zurueckweisungschiebung_minderjaehrig_seeweg";
CREATE TABLE "zurueckweisungschiebung_minderjaehrig_seeweg" ("staatsangehoerigkeit" VARCHAR(256), "gesamtzahl_personen" INTEGER, "zurueckweisungen_personen" INTEGER, "zurueckschiebungen_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckschiebung_bundeslaender";
CREATE TABLE "zurueckschiebung_bundeslaender" ("bundesland" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckschiebung_landweg_nationalitaet";
CREATE TABLE "zurueckschiebung_landweg_nationalitaet" ("staatsangehoerigkeit" VARCHAR(256), "zurueckschiebungen_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckschiebung_luftweg_flughafen";
CREATE TABLE "zurueckschiebung_luftweg_flughafen" ("flughafen" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckschiebung_luftweg_nationalitaet";
CREATE TABLE "zurueckschiebung_luftweg_nationalitaet" ("staatsangehoerigkeit" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckschiebung_luftweg_zielgebiet";
CREATE TABLE "zurueckschiebung_luftweg_zielgebiet" ("zielstaat_zielgebiet" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckweisung_bundeslaender";
CREATE TABLE "zurueckweisung_bundeslaender" ("bundesland" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckweisung_luftweg_flughafen";
CREATE TABLE "zurueckweisung_luftweg_flughafen" ("flughafen" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckweisung_luftweg_gruende";
CREATE TABLE "zurueckweisung_luftweg_gruende" ("nationalitaet" VARCHAR(256), "gesamt" INTEGER, "a" INTEGER, "b" INTEGER, "c" INTEGER, "d" INTEGER, "e" INTEGER, "f" INTEGER, "g" INTEGER, "h" INTEGER, "i" INTEGER);

DROP TABLE IF EXISTS "zurueckweisung_luftweg_nationalitaet";
CREATE TABLE "zurueckweisung_luftweg_nationalitaet" ("staatsangehoerigkeit" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckweisung_luftweg_zielgebiet";
CREATE TABLE "zurueckweisung_luftweg_zielgebiet" ("zielstaat_zielgebiet" VARCHAR(256), "gesamtzahl_personen" INTEGER);

DROP TABLE IF EXISTS "zurueckweisung_seeweg_gruende";
CREATE TABLE "zurueckweisung_seeweg_gruende" ("nationalitaet" VARCHAR(256), "gesamt" INTEGER, "a" INTEGER, "b" INTEGER, "c" INTEGER, "d" INTEGER, "e" INTEGER, "f" INTEGER, "g" INTEGER, "h" INTEGER, "i" INTEGER);

DROP TABLE IF EXISTS "ueberstellung_herkunftsstaat";
CREATE TABLE "ueberstellung_herkunftsstaat" ("herkunftsstaaten" VARCHAR(256), "n" INTEGER, "davon_minderjaehrige_unter_18" INTEGER);

DROP TABLE IF EXISTS "ueberstellung_zielgebiet";
CREATE TABLE "ueberstellung_zielgebiet" ("ueberstellungen_nach_mitgliedstaaten" VARCHAR(256), "n" INTEGER, "davon_minderjaehrige_unter_18" INTEGER);
