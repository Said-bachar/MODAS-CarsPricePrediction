from flask import Flask, render_template, request
import util

app = Flask(__name__)

@app.route("/")
def index():
    manufacturer = util.get_manufacturers()
    vehicle = []
    for car in manufacturer:
         car = car.replace("manufacturer_name_","")
         vehicle.append(car)
    car_models = util.get_models()
    models = []
    for model in car_models:
         model = model.replace("model_name_","")
         models.append(model)
    return render_template("index.html", vehicle = vehicle, models = models)


@app.route("/predictedPrice", methods = ["POST"])
def predictedPrice():
    try:
        year = int(request.form["year"])
        kms = int(request.form["kilometers"])
        vehicle = request.form["vehicle"]
        model = request.form["model"]
        fuel = request.form["fuel"]
        state = request.form["state"]
        transmission = request.form["transmission"]
        bodyType = request.form["bodytype"]
        engineCapacity =  float(request.form["engineCapacity"])
        numberOfPhotos =  int(request.form["numberOfPhotos"])
        upCounter = int(request.form["upCounter"])
        driveTrain = request.form["drivetrain"]

        gasoline = 0
        new = 0
        mechanical = 0
        suv = 0
        minibus = 0
        front = 0


        if fuel == "gasoline":
            gasoline = 1

        if state == "new":
            individual = 1

        if transmission == "mechanical":
            mechanical = 1

        if bodyType == 'suv':
            suv = 1
        elif bodyType == 'minibus':
            minibus = 1

        if driveTrain == "front":
            front = 1

        result = util.predict_price(vehicle, model, mechanical, kms , year, gasoline, engineCapacity, suv, minibus ,new, front, numberOfPhotos, upCounter)

        if result == 1:
            return "Something is wrong please fill proper input!!"
        else:
            return str(round(float(result), 2)) + " $ (USD)"
    except:
        return "Exception !!"

if __name__ == "__main__":
    app.run(debug = True)         