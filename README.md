### text_cleaner

clean a text to perform ml algo.

Can perform :

- remove dash for linebreak
- remove extra whitespace
- normalization to lower case (or upper)
- remove accents
- remove punctuation (preceded or folowed by a space)
- normalize inclusive writting
- split punctuation (inbetween two caracter like the apostrophe)
- remove digits
- remove short words (you set the limit size)
- remove stopwords
- transform plural to singular
- transform feminine to masculine
- stemming

example :

Before :
```
Édition du groupe « Ebooks libres et gratuits »




                                                              Jules Verne


                                                  VINGT MILLE LIEUES
                                                      SOUS LES MERS
                                                                 (1870)
                             Table des matières


PREMIÈRE PARTIE.................................................................4
  I UN ÉCUEIL FUYANT ............................................................... 5
  II LE POUR ET LE CONTRE .................................................... 12
  III COMME IL PLAIRA À MONSIEUR .................................... 19
  IV NED LAND............................................................................26
  V À L'AVENTURE ! ...................................................................35
  VI À TOUTE VAPEUR ...............................................................43
  VII UNE BALEINE D'ESPÈCE INCONNUE ............................ 55
  VIII MOBILIS IN MOBILE .......................................................65
  IX LES COLÈRES DE NED LAND............................................ 75
  X L'HOMME DES EAUX...........................................................84


                                         -3-
PREMIÈRE PARTIE



      -4-
                            I
                    UN ÉCUEIL FUYANT
    L’année 1866 fut marquée par un événement bizarre, un
phénomène inexpliqué et inexplicable que personne n’a sans
doute oublié. Sans parler des rumeurs qui agitaient les
populations des ports et surexcitaient l’esprit public à l’intérieur
des continents les gens de mer furent particulièrement émus.
Les négociants, armateurs, capitaines de navires, skippers et
masters de l’Europe et de l’Amérique, officiers des marines
militaires de tous pays, et, après eux, les gouvernements des
divers États des deux continents, se préoccupèrent de ce fait au
plus haut point.

    En effet, depuis quelque temps, plusieurs navires s’étaient
rencontrés sur mer avec « une chose énorme » un objet long,
fusiforme, parfois phosphorescent, infiniment plus vaste et plus
rapide qu’une baleine.
```

After :
```
edition groupe ebooks libre gratuit jules verne lieue mer table matiere partie ecueil fuyant iii plaira monsieur ned land aventure vapeur vii baleine espece inconnue viii mobilis mobile colere ned land homme eau partie ecueil fuyant anne marque evenement bizarre phenomene inexplique inexplicable doute oublie parler rumeur agitaient population port surexcitaient esprit public interieur continent gens mer particulierement emu negociant armateur capitaine navire skippers master europe amerique officier marine militaire pays gouvernement etat continent preoccuperent haut point effet temps plusieurs navire rencontre mer enorme objet long fusiforme parfois phosphorescent infiniment vaste rapide baleine
'edition groupe ebooks libre gratuit jules verne lieue mer table matiere partie ecueil fuyant iii plaira monsieur ned land aventure vapeur vii baleine espece inconnue viii mobilis mobile colere ned land homme eau partie ecueil fuyant anne marque evenement bizarre phenomene inexplique inexplicable doute oublie parler rumeur agitaient population port surexcitaient esprit public interieur continent gens mer particulierement emu negociant armateur capitaine navire skippers master europe amerique officier marine militaire pays gouvernement etat continent preoccuperent haut point effet temps plusieurs navire rencontre mer enorme objet long fusiforme parfois phosphorescent infiniment vaste rapide baleine'
```
