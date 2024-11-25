from django.shortcuts import render
import random
import joblib
import numpy as np
model = joblib.load('./saveModel/stroke_predict')

def home(request):
    return render(request, 'home.html')


def data(request):
    return render(request, 'data.html')

def predict(request):
    if request.method == 'POST':
        gender = int(request.POST.get('gender'))
        age = int(request.POST.get('age'))
        bmi = int(request.POST.get('bmi'))
        ever_married = int(request.POST.get('ever_married'))
        work_type = int(request.POST.get('work_type'))
        residence_type = int(request.POST.get('residence_type'))
        hypertension = int(request.POST.get('hypertension'))
        heart_disease = int(request.POST.get('heart_disease'))
        avg_glucose_level = int(request.POST.get('avg_glucose_level'))
        smoking_status = int(request.POST.get('smoking_status'))
        advice = [
            "L 'exercice peut aider à réduire les facteurs de risque d'AVC tels que l'hypertension artérielle, le diabète et l'obésité. Essayez d'ajouter de l'exercice à votre routine quotidienne, comme la marche rapide, la natation ou le vélo.",
            "La pression artérielle élevée est un facteur de risque majeur d'AVC. Consultez régulièrement votre médecin pour surveiller votre tension artérielle et prenez des mesures pour la maintenir sous contrôle si elle est élevée.",
            "Le tabagisme est un facteur de risque majeur d'AVC, car il augmente la pression artérielle et réduit le flux sanguin vers le cerveau. Si vous fumez, essayez d'arrêter ou de réduire votre consommation de tabac.",
            "Consultez régulièrement votre médecin pour des examens de santé réguliers et discutez avec lui de vos facteurs de risque d'AVC. Ensemble, vous pouvez élaborer un plan pour réduire votre risque d'AVC.",
            "Maintenir une communication ouverte et honnête avec votre partenaire pour réduire le stress et l'anxiété, qui peuvent être des facteurs de risque d'AVC.",
            "Si vous travaillez dans un bureau, prenez des pauses régulières pour vous lever et marcher pour éviter de rester assis pendant de longues périodes, ce qui peut augmenter le risque d'AVC. Essayez également d'ajuster votre poste de travail pour maintenir une posture correcte.",
            "Si vous avez un BMI élevé, essayez de perdre du poids en adoptant un régime alimentaire sain et en faisant de l'exercice régulièrement. Même une perte de poids modeste peut réduire le risque d'AVC."
        ]
        random_advice = random.choice(advice)
        data_test = np.array([gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]).reshape(1, -1)
        probabilities = model.predict_proba(data_test)
        probabilite_0, probabilite_1 = probabilities[0] 

        return render(request, 'predict.html', {
            'probabilite_1':probabilite_1*100,  
            'probabilite_0':probabilite_0*100,
            'random_advice': random_advice
        })
    return render(request, 'predict.html')