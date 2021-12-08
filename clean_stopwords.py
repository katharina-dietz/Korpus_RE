import spacy

# sm Model -> (klein) && Anzahl von Zeilen -> ca 4k
# =>> Laufzeit von ca 30 sek für sw filter.
nlp = spacy.load("de_core_news_sm")

add_stop_words = ['']
rm_stop_words = ['']

#for w in XX_stop_words:            #Add and remove stopword lists if needed
#   nlp.vocab[w].is_stop = True


# string - > string ohne Stopwords
    # in-place (? double-check)
def clean_sw(text):
    doc = nlp(text)
    stri = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return stri
            # token.lemma_ = base string

####-------for Testing
#string1 =[ "Einschneidende Veränderungen zeichnen sich auch in jenen Erzählungen und Romanen ab; die – von den im Schwange befindlichen Feenmärchen unbeeinflußt – auf phantastische Elemente verzichteten und in der Tradition von <e1>Marivaux</e1><rel>und Prévost an dem Anspruch festhielten, unter Verwendung </rel><e2>realistischer Details</e2>  wirkliches Geschehen zu gestalten.",
 #          "So erhalten die Romanfiguren jetzt in zunehmendem Maße ein eigenes moralisches Antlitz, werden sie als Schöpfer einer nicht mehr ständischen Form gesellschaftlichen Zusammenlebens dargestellt.] Bei dieser Neuorientierung können sich die <e1>französischen Erzähler</e1><rel>auf die englischen Romanciers stützen, vor allem auf </rel><e2>Richardson</e2>, dessen Werke seit den vierziger Jahren in französischer Bearbeitung erschienen.",
  #         "Zu den ersten Werken, die in Frankreich diese neue <e2>bewußtseinsbildende Funktion</e2><rel> exemplarisch wahrzunehmen suchten, gehören Marmontels </rel><e1>Contes moraux</e1> (1761: „Moralische Erzählungen“).",
   #        "Wenn <e1>Marmontel</e1><rel> Helden am Ende Liebe und Glück finden, so haben sie es gewöhnlich weniger einem wohlmeinenden Schicksal als ihrem bürgerlichen Fleiß, ihrer Tüchtigkeit und </rel><e2>Tugend</e2> zu danken.",
    #       "In seinem antikisierenden Roman <e1>Bélisaire</e1> <rel> (1767) schließlich, der in den Augen der Zeitgenossen den</rel> <e2>Telemach</e2>  Fénélons übertrifft, wird der Leser aus der Privatsphäre herausgeführt und mit öffentlichen Belangen, mit politischen Fragen konfrontiert. ",
     #      "In seinem antikisierenden Roman <e2>Bélisaire</e2> <rel>(1767) schließlich, der in den Augen der Zeitgenossen den Telemach Fénélons übertrifft, wird</rel>  <e1>der Leser</e1>  aus der Privatsphäre herausgeführt und mit öffentlichen Belangen, mit politischen Fragen konfrontiert.",
      #     "Als <e1>Bélisaire</e1><rel>am Grabe seiner Frau steht, „war der Schmerz des Helden der eines Weisen, er war tief, aber still und erhaben. Auf seinem Gesicht malte sich die Trauer, aber eine schweigsame und würdige Trauer.“] Charakterisierungen wie diese, die von den ganzen Empfindungsreichtum des Menschen, aber gleichzeitig von seiner sittlichen Beherrschung künden, sind für die </rel><e2>moralisierende Literatur</e2>  der Spätaufklärung typisch."
       #    ]

#for sting in string1:
 #   print(clean_sw(sting),"\n")

