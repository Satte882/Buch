from pathlib import Path
import re

ROOT = Path('.')
F1 = ROOT/'MANUSKRIPT/01_BAUSTEINE_01_02.md'
F2 = ROOT/'MANUSKRIPT/02_BAUSTEINE_03_04.md'
F3 = ROOT/'MANUSKRIPT/03_BAUSTEINE_05_06.md'
F4 = ROOT/'MANUSKRIPT/04_BAUSTEIN_07.md'
F5 = ROOT/'MANUSKRIPT/05_BAUSTEINE_08_09.md'


def replace_exact(path, old, new, n=1):
    text = path.read_text(encoding='utf-8')
    count = text.count(old)
    if count != n:
        raise SystemExit(f'{path}: expected {n} matches, found {count}: {old[:100]!r}')
    path.write_text(text.replace(old, new), encoding='utf-8')

# 1) Prolog: Ambiguität behalten, aber unnötige Relativierung und Dauer-Stakkato reduzieren.
text = F1.read_text(encoding='utf-8')
m = re.search(r'(## Prolog\n\n)(.*?)(\n\n---\n\n## 1\n)', text, re.S)
if not m:
    raise SystemExit('Prolog block not found')
new_prolog = '''Der Regen lief über den Verschluss der Pistole und sammelte sich am Korn.

Eine Hand hielt die Waffe ruhig genug.

Ein paar Meter entfernt stand ein Mann im Regen. Dunkle Kleidung, die Schultern leicht nach vorn gezogen. Hinter ihm verschwamm ein heller Streifen aus Glas und Beton im Wasser auf den Scheiben.

Unter dem Vordach war es kaum trockener. Der Wind drückte den Regen bis an die Wand. Wasser lief über den Boden und zog an den Schuhen des Schützen vorbei ins Dunkel.

Der Mann stand außerhalb des schmalen Schutzes. Seine Jacke war dunkel vor Nässe. Eine Hand hing an seiner Seite, die andere war nicht zu sehen.

Er bewegte sich nur wenig, und die Pistole folgte ihm gerade weit genug, dass der Lauf auf der Mitte seiner Brust blieb.

Dann hielt er wieder still.

Hinter der Glasfront ging irgendwo Licht an und gleich wieder aus. Vom Gelände kam ein dumpfer Schlag, Metall auf Metall, im Regen ohne erkennbare Richtung.

Der Mann hob die rechte Hand. Ob er etwas sagte, ging im Regen unter.

Die Hand war leer.

Die Finger waren gespreizt, nicht hoch genug für eine eindeutige Geste und nicht tief genug, um bedeutungslos zu sein.

Der Schütze machte keinen Schritt. Wasser lief über seine Fingerknöchel und tropfte vom Magazinboden.

Der Mann hatte den Kopf leicht zur Seite gedreht. Dann sah er wieder nach vorn.

Die Entfernung blieb gleich.

Drei Meter. Vielleicht vier.

Nah genug, um loszulaufen. Weit genug, dass der erste Schritt nicht der letzte gewesen wäre.

Dann veränderte sich etwas.

Der rechte Arm des Mannes sank ein Stück. Sein Gewicht verlagerte sich seitlich. Kein Schritt auf den Schützen zu.

Die Pistole musste der Bewegung nicht folgen. Sie war bereits dort.

Der Finger am Abzug spannte sich.

Der Mann griff den Schützen nicht an.

Der Knall war kurz und trocken.

Der Verschluss riss zurück. Wasser spritzte vom Metall, die leere Hülse verschwand im Dunkel.

Für einen Augenblick war der Regen wieder das lauteste Geräusch.

Der Mann zuckte und machte einen Schritt nach hinten, als hätte jemand ihn an der Jacke gerissen. Dann fiel er. Ein Knie schlug zuerst auf den Beton, danach die Schulter. Der Körper drehte sich halb zur Seite und blieb liegen.

Die Waffe blieb oben.

Der Schütze atmete einmal durch den Mund.

Am Boden hob der Mann den Kopf kaum merklich. Eine Hand lag offen auf dem Beton, die andere war unter seinem Körper verschwunden.

Der Schütze setzte den rechten Fuß einen halben Schritt vor und blieb stehen.

Es fiel kein zweiter Schuss.

Erst jetzt trat er aus dem Schatten des Vordachs.

Daniel Reuter sah auf den Mann am Boden. Wasser lief ihm über die Stirn und in den Kragen.

Er senkte die Pistole nicht.'''
text = text[:m.start(2)] + new_prolog + text[m.end(2):]
F1.write_text(text, encoding='utf-8')

# 2) Einstieg: unnötige Weichmacher reduzieren, reale Prozessreibung ergänzen.
replace_exact(F1,
    'Jonas schien von der Zustimmung kurz aus dem Takt gebracht.',
    'Die Zustimmung brachte Jonas kurz aus dem Takt.')
replace_exact(F1,
    '„Vielleicht. Vielleicht fragt jemand nach dem Grund. Vielleicht wird aus einer Kontrolle eine zweite, weil ein Kollege den Vermerk sieht. Vielleicht passiert gar nichts.“',
    '„Vielleicht fragt jemand nach dem Grund. Vielleicht wird aus einer Kontrolle eine zweite, weil ein Kollege den Vermerk sieht. Oder es passiert gar nichts.“')
replace_exact(F1,
    'Die erste Entlastung kam um 14.37 Uhr.\n\nDaniel war gerade auf dem Weg zu einem anderen Termin, als Jonas ihn im Flur abfing.',
    'Die erste Entlastung kam um 14.37 Uhr. Zwei Rückrufe beim Sicherheitsdienst waren bis dahin ins Leere gegangen; die Fahrzeugdisposition stand noch aus.\n\nDaniel war gerade auf dem Weg zu einem anderen Termin, als Jonas ihn im Flur abfing.')
replace_exact(F1,
    'Arbeitsauftrag. Datum. Ansprechpartner. Leistungsbeschreibung. Nichts daran wirkte nachträglich zusammengebaut. Trotzdem las Daniel die Seite zweimal.',
    'Arbeitsauftrag. Datum. Ansprechpartner. Leistungsbeschreibung. Nichts daran deutete auf eine nachträgliche Konstruktion. Trotzdem las Daniel die Seite zweimal.')
replace_exact(F1,
    'Daniel legte das Tablet flach auf den Tisch.\n\nMit jedem Dokument wurde die Sache langweiliger.\n\nDaniel mochte langweilige Erklärungen.',
    'Daniel legte das Tablet flach auf den Tisch. Mit jedem Dokument wurde die Sache langweiliger, und Daniel mochte langweilige Erklärungen.')
replace_exact(F1,
    'Daniel rief selbst bei dem Ansprechpartner des Gebäudes an. Zwei Minuten später hatte er die letzte Bestätigung: Ahrens sollte am kommenden Montag die Zufahrt mit einem größeren Fahrzeug testen.',
    'Daniel rief selbst bei dem Ansprechpartner des Gebäudes an. Beim ersten Versuch ging niemand ran. Zehn Minuten später rief der Mann zurück. Ahrens sollte am kommenden Montag die Zufahrt mit einem größeren Fahrzeug testen.')
replace_exact(F1,
    'Er ergänzte keine vierte Zeile.\n\nEr setzte unter jede die bestätigte Erklärung.\n\nArbeitsauftrag.\n\nAnlieferfenster.\n\nAnderer Aufbau in derselben Gegend.\n\nJonas sah zu.',
    'Er ergänzte keine vierte Zeile. Unter jede setzte er die bestätigte Erklärung: Arbeitsauftrag, Anlieferfenster, anderer Aufbau in derselben Gegend.\n\nJonas sah zu.')
replace_exact(F1,
    'Die Wohnung roch noch immer nach seiner Mutter, obwohl fast alles, was diesen Geruch hätte erklären können, längst in Kisten steckte. Vielleicht bildete er es sich ein. Jana behauptete, es sei das Holz der alten Schränke.',
    'Für Daniel roch die Wohnung noch immer nach seiner Mutter, obwohl fast alles, was diesen Geruch hätte erklären können, längst in Kisten steckte. Jana behauptete, es sei das Holz der alten Schränke.')
replace_exact(F1,
    'Das war vermutlich der erste Satz an diesem Abend, gegen den er nichts prüfen konnte.',
    'Das war der erste Satz an diesem Abend, gegen den er nichts prüfen konnte.')

# 3) Auslöser/Moralischer Druck: symmetrische Relativierung und Rhetorik-Ticks glätten.
replace_exact(F2,
    'Wenn er jetzt fragte, ob sie jemandem von seinem Besuch erzählt hatte, erzeugte er aus einem ungeklärten Satz sofort eine private Lage. Vielleicht zu Recht. Vielleicht wegen einer Nachricht, deren Absender genau diese Reaktion wollte.',
    'Wenn er jetzt fragte, ob sie jemandem von seinem Besuch erzählt hatte, erzeugte er aus einem ungeklärten Satz sofort eine private Lage. Sie konnte real sein. Oder genau die Reaktion, die der Absender provozieren wollte.')
replace_exact(F2,
    'Jana. Mara. Der Makler möglicherweise. Jeder, der ihm gefolgt war.',
    'Jana. Mara. Der Makler. Jeder, der ihm gefolgt war.')
replace_exact(F2,
    'Vielleicht kam um 19.40 Uhr die reguläre Bestätigung.\n\nVielleicht um 20.05 Uhr.\n\nVielleicht morgen.\n\nVielleicht war das Kennzeichen nichts.',
    'Die reguläre Bestätigung konnte um 19.40 Uhr kommen, um 20.05 Uhr oder erst morgen. Das Kennzeichen konnte sich am Ende als nichts erweisen.')
replace_exact(F2,
    'Er hätte sich eine Begründung bauen können.\n\nAkute Lage.\n\nGefahr für eine Großveranstaltung.\n\nZweimal präzise Quelleninformation.\n\nVerletzter Sicherheitsmann.\n\nAlles wahr.',
    'Er hätte sich aus lauter wahren Punkten eine Begründung bauen können: akute Lage, Gefahr für eine Großveranstaltung, zweimal präzise Quelleninformation, ein verletzter Sicherheitsmann.')
replace_exact(F2,
    'Kein unsichtbarer Schritt.\n\nKein Hack.\n\nKein Zugang, den jemand anderer für ihn geöffnet hatte.\n\nSein Name. Seine Kennung. Seine Uhrzeit.\n\nDas war fast beruhigend.\n\nFast.',
    'Es war kein unsichtbarer Schritt und kein Hack. Der Zugriff lief unter seinem Namen, seiner Kennung, seiner Uhrzeit. Gerade diese Sichtbarkeit hatte etwas beinahe Beruhigendes.')
replace_exact(F2,
    'Er klickte zurück in die Suchmaske.\n\nPerson blieb leer.\n\nAnschrift blieb leer.\n\nTelefon blieb leer.',
    'Er klickte zurück in die Suchmaske. Die Felder für Person, Anschrift und Telefon blieben leer.')
replace_exact(F2,
    'Keine Fahrer.\n\nKeine Kontakte.\n\nKeine Haushalte.\n\nKeine Bewegungsübersicht.\n\nKeine Suche nach Janas Namen, obwohl der Gedanke für einen kurzen Moment da war.',
    'Er zog weder Fahrer noch Kontakte, Haushalte oder Bewegungsübersichten hinzu. Nach Janas Namen suchte er ebenfalls nicht, obwohl ihm der Gedanke kurz kam.')
replace_exact(F2,
    'Das Feld wäre da gewesen.\n\nEr ließ es zu.\n\nDaniel öffnete den dritten Treffer.\n\nZwei Tage später.\n\nAndere Straße.\n\nWieder beide Fahrzeuge innerhalb desselben Zeitfensters.\n\nDiesmal neun Minuten auseinander.',
    'Das Feld wäre da gewesen; er ließ es zu. Daniel öffnete den dritten Treffer. Zwei Tage später, andere Straße: wieder beide Fahrzeuge innerhalb desselben Zeitfensters, diesmal neun Minuten auseinander.')
replace_exact(F2,
    'Er hätte jetzt erweitern können.\n\nFahrer.\n\nKontakte.\n\nWeitere Fahrzeuge der Kurierfirma.\n\nPersonen aus dem alten Verfahren.',
    'Er hätte jetzt auf Fahrer, Kontakte, weitere Fahrzeuge der Kurierfirma und Personen aus dem alten Verfahren erweitern können.')
replace_exact(F2,
    'Drei Treffer.\n\nEiner wertlos.\n\nZwei möglicherweise relevant.',
    'Drei Treffer: einer wertlos, zwei offen.')
replace_exact(F2,
    'Nicht *Sie hatten recht*.\n\nNicht *Sie haben Menschen gerettet*.\n\nNicht einmal *der Zugriff hat funktioniert*.',
    'Die Nachricht sagte weder *Sie hatten recht* noch *Sie haben Menschen gerettet*. Nicht einmal *der Zugriff hat funktioniert*.')
replace_exact(F2,
    'Vielleicht hatte sie nur darauf gesetzt, dass er es wahrscheinlich tat.',
    'Vielleicht hatte sie nur darauf gesetzt, dass er es tat.')

# 4) Mittelteil: Erklär-/Wiederholungsechos entfernen, nicht die Methode selbst.
replace_exact(F3,
    'Nicht gebrochen.\n\nNicht geläutert.\n\nNur ein Mann, der offenbar erst jetzt begriff, dass sein normaler Montag vielleicht nicht mehr stattfand.',
    'Nicht gebrochen oder geläutert. Nur ein Mann, dem gerade klar wurde, dass sein normaler Montag nicht mehr stattfand.')
replace_exact(F3,
    'Keine Versöhnung.\n\nKeine Entlastung.\n\nNur eine Korrektur, die langsamer wirkte als der Verdacht.\n\nNach dem Telefonat öffnete Daniel die Weitergabekette der Korrektur.',
    'Nach dem Telefonat öffnete Daniel die Weitergabekette der Korrektur.')
replace_exact(F3,
    'Sie hasste den Satz vermutlich.\n\n„Wahrscheinlich nicht rechtzeitig“, sagte sie schließlich.',
    '„Wahrscheinlich nicht rechtzeitig“, sagte sie schließlich.')
replace_exact(F3,
    'Daniel hörte zu.\n\nNicht alles daran betraf ihn.\n\nDas war vermutlich der Punkt.\n\nDaniel fragte Mara nicht nach Quadratmetern oder Mietdauer.',
    'Daniel hörte zu. Nicht alles daran betraf ihn.\n\nEr fragte Mara nicht nach Quadratmetern oder Mietdauer.')
replace_exact(F3,
    'Das hatte sie ihm schon beim ersten Gespräch gesagt.\n\nVielleicht nicht in denselben Worten.\n\nEr hatte damals nach Homeoffice gefragt.',
    'Das hatte sie ihm schon beim ersten Gespräch gesagt, nur anders. Damals hatte er nach Homeoffice gefragt.')
replace_exact(F3,
    'Jetzt saß er hier.\n\nNicht später genug offenbar.\n\n„Ich baue die breiten Möglichkeiten jetzt nicht vollständig zurück“, sagte er.',
    'Jetzt saß er hier.\n\n„Ich baue die breiten Möglichkeiten jetzt nicht vollständig zurück“, sagte er.')

# 5) Reversal: echte Unsicherheit schützen, nur sichtbare Formelschablonen glätten.
replace_exact(F4,
    'Mit nur der Kennung wirkte die Lage enger.\n\nMit beiden Zeilen wirkte sie prüfbedürftig.\n\nNicht harmlos.\n\nNur anders.',
    'Mit nur der Kennung wurde die Lage enger; mit beiden blieb sie prüfbedürftig. Nicht harmlos, aber anders.')
replace_exact(F4,
    'Diesmal wirkte die Lücke nicht leer.\n\nDiesmal konnte man sie prüfen.',
    'Diesmal war die Lücke prüfbar.')

# 6) Finale/Nachhall: bewusste Echos behalten, redundante Wiederholungen entfernen.
replace_exact(F5,
    'Drei Meter auf nassem Beton.\n\nVielleicht weniger.\n\nEin Schritt unter das Vordach, zwei hinaus.',
    'Drei Meter auf nassem Beton.\n\nEin Schritt unter das Vordach, zwei hinaus.')
replace_exact(F5,
    'Die Entfernung war nach dem Schuss nicht größer geworden.\n\nSie wirkte nur plötzlich messbar.',
    'Die Entfernung war nach dem Schuss nicht größer geworden. Sie war nur plötzlich messbar.')
replace_exact(F5,
    'Nicht jede Person war geklärt.\n\nNicht jede Verbindung erklärt.\n\nNicht jeder Teil von Hellers Warnung bestätigt.',
    'Personen blieben ungeklärt, Verbindungen offen, Teile von Hellers Warnung unbestätigt.')
replace_exact(F5,
    'Daniel merkte erst da, dass seine linke Hand zitterte.\n\nNicht stark.\n\nGenug.',
    'Daniel merkte erst da, dass seine linke Hand leicht zitterte.')
replace_exact(F5,
    'Keine letzte Aussage.\n\nKeine saubere Motivformel.\n\nKeine Möglichkeit, Heller im Nachhinein alles zuzuschreiben, was Daniel selbst entschieden hatte.',
    'Es gab keine letzte Aussage, keine saubere Motivformel und keine Möglichkeit, Heller im Nachhinein alles zuzuschreiben, was Daniel selbst entschieden hatte.')
replace_exact(F5,
    'Wieder dieser Satz.\n\nGetrennt.\n\nHellers Manipulation.\n\nDaniels Schuss.\n\nOperativer Nutzen.\n\nKeines hob das andere auf.',
    'Wieder dieselbe Trennung: Hellers Manipulation, Daniels Schuss, operativer Nutzen. Keines hob das andere auf.')
replace_exact(F5,
    'Früher hätte er geantwortet, weil es zwei Minuten dauerte.\n\nVielleicht auch heute.\n\nMara stellte ihm den Kaffee hin.',
    'Früher hätte er geantwortet, weil es zwei Minuten dauerte.\n\nMara stellte ihm den Kaffee hin.')
replace_exact(F5,
    'Mara ging zwei Schritte zur Seite und sprach fünf Minuten über eine Präsentation, einen verschobenen Termin und jemanden, der offenbar seit dem Morgen auf eine Entscheidung wartete.',
    'Mara ging zwei Schritte zur Seite und sprach fünf Minuten über eine Präsentation, einen verschobenen Termin und jemanden, der seit dem Morgen auf eine Entscheidung wartete.')
replace_exact(F5,
    'Das Gespräch dauerte vielleicht zwanzig Sekunden.',
    'Das Gespräch dauerte kaum zwanzig Sekunden.')
replace_exact(F5,
    'Jonas zog die Markierung zurück.\n\nNiemand wirkte enttäuscht.\n\nDas gefiel Daniel.',
    'Jonas zog die Markierung zurück. Niemand protestierte.\n\nDas gefiel Daniel.')
replace_exact(F5,
    'Sie hatte den Fall nicht automatisch größer gemacht.\n\nZumindest diesmal nicht.',
    'Sie hatte den Fall nicht automatisch größer gemacht. Diesmal nicht.')
replace_exact(F5,
    'Daniel bemerkte, dass niemand enttäuscht wirkte.\n\nDas Instrument musste nicht jedes Mal etwas finden, um als normal zu gelten.\n\nVielleicht war genau das die stärkste Form von Normalisierung.',
    'Das Instrument musste nicht jedes Mal etwas finden, um als normal zu gelten.')

# 7) Umfangssteuerung: historische Ziele bleiben sichtbar, sind ab jetzt aber kein Qualitäts-/Abnahmekriterium.
U = ROOT/'UMFANG_UND_AUSBAUSTEUERUNG.md'
ut = U.read_text(encoding='utf-8')
anchor = '## Überziel\n'
status = '''## Aktuelle Steuerungsregel ab #39 – Qualität vor Wortziel\n\nDie nachfolgenden Wortziele dokumentieren die **historische Ausbauplanung**. Für die abgenommene Vollfassung und alle weiteren Lektorats-/Testleser-Pässe sind sie **kein Abnahmekriterium mehr**.\n\n- **Umfang folgt Funktion.**\n- Wortzahl wird weiter automatisch gemessen, aber nicht mechanisch optimiert.\n- Es wird weder aufgefüllt noch gekürzt, nur um einen Korridor zu treffen.\n- Eine Kürzung ist richtig, wenn sie Leserwirkung verbessert; eine Erweiterung ist richtig, wenn eine vorhandene Szene dadurch glaubwürdiger, konkreter oder emotional vollständiger wird.\n- Plot-, Figuren- und Romanfunktion haben Vorrang vor Soll/Ist-Werten.\n\nDiese Regel überschreibt für die aktuelle Manuskriptphase alle später in dieser Datei genannten Formulierungen, nach denen 75.000–80.000 Wörter oder 77.000 Wörter zwingend erreicht werden müssten. Die Werte bleiben ausschließlich als historische Planungs- und Vergleichsdaten erhalten.\n\n'''
if status not in ut:
    if anchor not in ut: raise SystemExit('UMFANG anchor missing')
    ut = ut.replace(anchor, status + anchor, 1)
    U.write_text(ut, encoding='utf-8')

# 8) Konsolidierte Finaldatei ausschließlich aus Prolog + K1–47 neu bauen; technische Baustein-Header nicht übernehmen.
files=[F1,F2,F3,F4,F5]
chapters={}
heading=re.compile(r'^##\s+(Prolog|\d+)\s*$')
for path in files:
    cur=None; buf=[]
    for line in path.read_text(encoding='utf-8').splitlines():
        m=heading.match(line.strip())
        if m:
            if cur is not None: chapters[cur]='\n'.join(buf).strip('\n')
            cur=m.group(1); buf=[]
        elif cur is not None:
            if line.strip()=='---': continue
            buf.append(line)
    if cur is not None: chapters[cur]='\n'.join(buf).strip('\n')
order=['Prolog']+[str(i) for i in range(1,48)]
missing=[c for c in order if c not in chapters]
if missing: raise SystemExit(f'missing chapters: {missing}')
parts=['# Ausnahmezustand']
for c in order:
    parts.append(f'## {c}\n\n{chapters[c].strip()}')
final='\n\n---\n\n'.join(parts).rstrip()+'\n'
if final.count('\n## ' ) != 48: raise SystemExit('chapter count invariant failed')
if 'Die Hand war leer.' not in chapters['Prolog']: raise SystemExit('cold-open empty-hand invariant failed')
if 'Nicht gesendet.' not in chapters['40']: raise SystemExit('K40 not-sent invariant failed')
if 'Terminal in der linken Hand' not in chapters['40']: raise SystemExit('K40 left-hand terminal invariant failed')
if not final.rstrip().endswith('„Wie belastbar ist deine Gegenhypothese?“'): raise SystemExit('final line invariant failed')
(ROOT/'AUSNAHMEZUSTAND_FINAL.md').write_text(final, encoding='utf-8')

# 9) Diagnose nach Patch aktualisieren (temporär; wird nach Abnahme wieder gelöscht).
exec((ROOT/'scripts/anti_tick_scan.py').read_text(encoding='utf-8'), {'__name__':'__main__'})
exec((ROOT/'scripts/anti_tick_detail_scan.py').read_text(encoding='utf-8'), {'__name__':'__main__'})
print('anti-tick pass applied and final rebuilt')
