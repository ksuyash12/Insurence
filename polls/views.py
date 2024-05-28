from django.shortcuts import render, redirect
import pandas as pd
import pickle


def index_func(request):
    res = 0
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['sex']  # select
        bmi = request.POST['bmi']
        child = request.POST['child']
        smoker = request.POST['smoker']  # select
        region = request.POST['region']  # select

        if all([name, age, gender, bmi, child, smoker, region]):
            # Convert POST data to appropriate types and create a dictionary
            data = {
                'age': float(age),
                'sex': int(gender),
                'bmi': float(bmi),
                'children': int(child),
                'smoker': int(smoker),
                'region': int(region)
            }

            # Create a DataFrame with the specified columns
            df = pd.DataFrame([data])

            # load the model from disk
            model = 'polls/Medical.pickle'
            loaded_model = pickle.load(open(model, 'rb'))
            res = loaded_model.predict(df)
            print(res)

        else:
            return redirect('homepage')
    else:
        pass

    return render(request, "index.html", {'response': res})
