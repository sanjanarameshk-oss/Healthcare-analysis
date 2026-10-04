# Healthcare Text Analysis

print("====================================")
print("       HEALTHCARE TEXT ANALYSIS")
print("====================================")

text = input("Enter patient symptoms: ").lower()

symptoms = {
    "Fever": ["fever", "temperature", "hot"],
    "Cough": ["cough", "coughing"],
    "Cold": ["cold", "sneezing", "runny nose"],
    "Headache": ["headache", "head pain"],
    "Stomach Pain": ["stomach pain", "abdominal pain"],
    "Sore Throat": ["sore throat", "throat pain"],
    "Fatigue": ["tired", "fatigue", "weakness"],
    "Vomiting": ["vomiting", "vomit"]
}

found_symptoms = []

for symptom, keywords in symptoms.items():
    for keyword in keywords:
        if keyword in text:
            found_symptoms.append(symptom)
            break

print("\n========== ANALYSIS RESULT ==========")
print("Patient Input:", text)

if found_symptoms:
    print("Detected Symptoms:")
    for symptom in found_symptoms:
        print("-", symptom)
else:
    print("No common symptoms detected.")

print("\nNote: This program is for educational purposes only.")
print("Please consult a qualified healthcare professional for medical advice.")