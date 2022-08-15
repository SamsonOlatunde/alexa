from django.shortcuts import render, redirect
from .models import sentimentAnalysis
import joblib
import pickle


# Create your views here.


def index(request):
    model = joblib.load('model_svc.pkl')

    #title = sentimentAnalysis.objects.all()

    if request.method == 'POST':
        message = request.POST['title']
        prediction = model.predict([message])

        def predict(item):
            if item == 1:
                return 'Positive Review'
            else:
                return 'Negative Review'

        predict_result = predict(prediction)

        return render(request, 'index.html', {'predict': predict_result})
    return render(request, 'index.html')
