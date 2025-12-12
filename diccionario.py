meme_dict = {
  "CRINGE": "Algo que causa mucha pena",
  "LOL": "Una respuesta comun a algo gracioso",
  "Rolf":"Se utiliza como reaccion a algo gracioso,similar a LOL"
  "Aguacero" : "Lluvia muy fuerte y repentina",
  "Dar papaya": "Dejarse robar, descuidarse o colocarse en riesgo innecesario",
  "Desparchado": "Estar sin nada que hacer o sin planes."

word = input("Escribe una palabra moderna que no entiendas (!Utiliza mayusculas): ")
if word in meme_dict.keys():
  print(meme_dict[word]
else:
  print("Todavia no tenemos esa palabra... Pero estamos trabajando en ella.") 
