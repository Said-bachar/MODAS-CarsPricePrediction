import numpy as np
import pickle
import json

model = None
columns = None
manufacturers = None
car_models = None

def load_artifacts():
    global model
    global columns
    # here we are going to load our artifacts

    with open("./model.pkl", "rb") as f:
        model = pickle.load(f)

    with open("./columns.json", "r") as f:
        columns = json.load(f)["data_columns"]

def predict_price(manufacturer_name, model_name, mechanical,  odometer_value, year_produced, gasoline, engine_capacity, suv, minibus ,new, front, number_of_photos, up_counter):
    try:
        manufacturer_index = -1
        manufacturer = "manufacturer_name_" + manufacturer_name
        #model = "model_name_" + model_name
        if manufacturer_name != "800":
            manufacturer_index = columns.index(manufacturer.lower())

        X_pred = np.zeros(len(columns))

        count = 0
        features = [ mechanical,  odometer_value, year_produced, gasoline, engine_capacity, suv, minibus ,new, front, number_of_photos, up_counter] # it's just for looping purpose

        for f in features:
            X_pred[count] = f
            count += 1

        if manufacturer_index > 0:
            X_pred[manufacturer_index] = 1

        result = model.predict([X_pred])[0]

        return result
    except:
        return 1


def get_manufacturers():
    load_artifacts()
    global manufacturers
    manufacturers = columns[36:90]
    return manufacturers 

def get_models():
    load_artifacts()
    global car_models
    car_models = columns[91:]
    return car_models 

if __name__ == "__main__":
    load_artifacts()
    print(get_models())
    # cars = get_manufacturers()
    # newCars = []
    # for car in cars:
    #      car = car.replace("manufacturer_name_","")
    #      newCars.append(car)
    # print(newCars)
    #print(model)
    #print(predict_price("Chrysler", "Voyager", 0, 297729, 2000, 1, 2.4,0,0,0,1,4,73))