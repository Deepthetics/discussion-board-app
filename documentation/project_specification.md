## Sovelluksen tarkoitus

Sovelluksen on tarkoitus toimia keskustelualustana, missä käyttäjät voivat käydä keskustelua eri aiheista. Aiheet muodostavat omat keskustelualueensa, jotka sisältävät aiheeseen liittyviä käyttäjien luomia viestiketjuja. Viestiketjut sisältävät käyttäjien kirjoittamia viestejä.

## Käyttäjät

Sovelluksella on kahdenlaisia käyttäjiä:
- peruskäyttäjä
- ylläpitäjä

## Sovelluksen keskeiset toiminnot

- käyttäjä voi luoda uuden tunnuksen #DONE
- käyttäjä voi kirjautua sisään olemassaolevalla tunnuksella #DONE
- käyttäjä voi kirjautua ulos #DONE
- käyttäjä näkee sovelluksen etusivulla olemassaolevat keskustelualueet #DONE
- käyttäjä näkee keskustelualueiden sisältämien viestiketjujen lukumäärät #DONE
- käyttäjä näkee keskustelualueen sivulla keskustelualueen viestiketjut #DONE
- käyttäjä näkee viestiketjujen sisältämien viestien lukumäärät #DONE
- käyttäjä näkee viestiketjun sivulla siihen kirjoitetut viestit #DONE
- käyttäjä näkee viestien yhteydessä niihin liittyvät tiedot (kirjoittaja/ajankohta/tykkäykset) #DONE
- käyttäjä voi luoda uuden viestiketjun antamalla sille otsikon ja kirjoittamalla viestiketjun aloitusviestin #DONE
- käyttäjä voi kirjoittaa viestejä jo olemassaoleviin viestiketjuihin #DONE
- käyttäjä voi muokata luomansa viestiketjun otsikkoa #DONE
- käyttäjä voi muokata kirjoittamansa viestin sisältöä #DONE
- käyttäjä voi poistaa luomansa viestiketjun #DONE
- käyttäjä voi poistaa kirjoittamansa viestin #DONE
- ylläpitäjä voi luoda keskustelualueita #DONE
- ylläpitäjä voi poistaa keskustelualueita #DONE
- ylläpitäjä voi poistaa viestiketjuja #DONE
- ylläpitäjä voi poistaa viestejä #DONE

## Sovelluksen jatkokehitysideat

- käyttäjä näkee keskustelualueen yhteydessä viimeksi aktiivisen viestiketjun sekä sinne viimeksi kirjoitetun viestin kirjoittajan/ajankohdan
- käyttäjä näkee viestiketjun yhteydessä sinne viimeksi kirjoitetun viestin kirjoittajan/ajankohdan
- käyttäjä voi tykätä muiden käyttäjien viesteistä
- käyttäjä voi lähettää yksityisviestejä muille käyttäjille
- ylläpitäjä voi poistaa käyttäjiä

## Tiedostetut bugit/puutteet/kehityskohdat
- viestiketju ei poistu automaattisesti, jos siitä poistetaan kaikki viestit
- käyttäjälle ei tulosteta ilmoituksia onnistuneista operaatioista
- käyttäjältä/ylläpitäjältä ei varmisteta poisto-operaatioiden yhteydessä, että haluavatko he todella toteuttaa poiston
- ilmoitukset epäonnistuneista operaatioista voitaisiin tulostaa samalle sivulle ilman uudelleenohjausta
- uuden viestiketjun luonnin jälkeen ohjataan keskustelualueen sivulle, vaikka loogisempaa voisi olla ohjata uuden viestiketjun sivulle
- ulkoasu
