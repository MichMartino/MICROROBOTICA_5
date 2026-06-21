from flask import Flask, render_template, request
#cartella per modello e labelEncoder
from joblib import load
#App semplice per utilizzare la regressione lineare

#Creo l'app
app = Flask(__name__)

#Prendo il regressore e gli encoder e li carico
regressor = load("./webapp500usate/regressor.joblib")
labelEncoder_model = load("./webapp500usate/labelEncoder_model.joblib")
labelEncoder_transmission = load("./webapp500usate/labelEncoder_transmission.joblib")

@app.route("/", methods=["GET", "POST"])
def prevedi_prezzo():
    if request.method == "POST":
        #Mi prendo tutti i dati dal form
        engine_power = int(request.form["engine_power"])
        age_in_days = int(request.form["age_in_days"])
        km = int(request.form["km"])
        previous_owners = int(request.form["previous_owners"])
        lat = float(request.form["lat"])
        lon = float(request.form["lon"])
        model = request.form["model"]
        transmission = request.form["transmission"]

        #Trasformo i campi testuali in numeri con i labelEncoder
        model_n = labelEncoder_model.transform([model])[0]
        transmission_n = labelEncoder_transmission.transform([transmission])[0]

        #Ora preparo la 500 di test
        fiat500 = [engine_power,
            age_in_days,
            km,
            previous_owners,
            lat,
            lon,
            model_n,
            transmission_n]
        
        prezzo_risultato = regressor.predict([fiat500])[0]

        return render_template("index.html", prezzo = prezzo_risultato)
    
    return render_template("index.html")

if __name__=="__main__":
    #Avvio l'app
    app.run(host = "0.0.0.0", port= 5000, debug = True)

