import matplotlib.pyplot as plt
import numpy as np

# Parameter-Initialisierung
initial_dose = 10  # in mg
diazepam_plateau = 700 * initial_dose / 10  # in ng/ml
diazepam_half_life = 30 / 24  # in Tagen
n_desmethyldiazepam_half_life = 4  # in Tagen
n_desmethyldiazepam_conversion_ratio = 1  # 1:1 Umwandlung von Diazepam zu N-Desmethyldiazepam

diazepam_duration = 1  # Diazepam Einnahme Dauer in Tagen - Anpassen wie gewünscht
total_duration = 30  # Länge der x-Achse in Tagen - Anpassen wie gewünscht

diazepam_equivalent_ng_per_ml = 177  # 177 ng/ml entsprechen 10 mg Diazepam
diazepam_equivalent_ratio = 10 / diazepam_equivalent_ng_per_ml

# Arrays erstellen
days = np.arange(0, total_duration, 0.1)
diazepam_conc = np.zeros(len(days))
n_desmethyldiazepam_conc = np.zeros(len(days))

# Modellierung der Konzentrationssteigerung und des Plateaus
steady_state_reached_day = None
five_mg_reached_day = None
for i, day in enumerate(days):
    if day <= diazepam_duration:
        diazepam_conc[i] = diazepam_plateau / (1 + np.exp(-0.5 * (day - 5)))
    else:
        diazepam_conc[i] = diazepam_conc[i - 1] * (2 ** (-0.1 / diazepam_half_life))

    n_desmethyldiazepam_conc[i] = n_desmethyldiazepam_conc[i - 1] + 0.05 * diazepam_conc[i] * n_desmethyldiazepam_conversion_ratio
    n_desmethyldiazepam_conc[i] *= (2 ** (-0.1 / n_desmethyldiazepam_half_life))

    # Ermitteln Sie den Zeitpunkt, an dem der Steady-State erreicht wird
    if steady_state_reached_day is None and day > 0 and np.abs(diazepam_conc[i] - diazepam_conc[i - 1]) < 0.01:
        steady_state_reached_day = day

    # Ermitteln Sie den Zeitpunkt, an dem nur noch 5 mg Diazepam-Äquivalent im Körper sind
    if (five_mg_reached_day is None) and (day > diazepam_duration) and ((diazepam_conc[i] + n_desmethyldiazepam_conc[i]) * diazepam_equivalent_ratio <= 5):
        five_mg_reached_day = day

peak_diazepam_conc = max(diazepam_conc)
peak_n_desmethyldiazepam_conc = max(n_desmethyldiazepam_conc)
peak_conc_ng_per_ml = peak_diazepam_conc + peak_n_desmethyldiazepam_conc
peak_conc_mg = peak_conc_ng_per_ml * diazepam_equivalent_ratio  # Spitzenkonzentration in mg Diazepam-Äquivalent

if steady_state_reached_day is not None:
    print(f"Das Plateau (Steady State) wird erreicht an Tag: {steady_state_reached_day:.1f}")

if five_mg_reached_day is not None:
    print(f"Nach Tag {five_mg_reached_day:.1f} beträgt die Diazepam-Äquivalenz nur noch 5 mg")

# Vergleichsstoffe und ihre Äquivalenzen zu 10 mg Diazepam
benzos = {
    "Alprazolam": 0.5,
    "Bromazepam": 5,
    "Chlordiazepoxide": 25,
    "Clobazam": 20,
    "Clonazepam": 0.5,
    "Clorazepate": 15,
    "Diazepam": 10,
    "Estazolam": 1.5,
    "Flunitrazepam": 1,
    "Halazepam": 20,
    "Ketazolam": 22.5,
    "Loprazolam": 1.5,
    "Lorazepam": 1,
    "Lormetazepam": 1.5,
    "Medazepam": 10,
    "Midazolam": 7.5,
    "Nitrazepam": 10,
    "Nordazepam": 10,
    "Oxazepam": 20,
    "Prazepam": 15,
    "Quazepam": 20,
    "Temazepam": 20,
    "Zaleplon": 20,
    "Zolpidem": 20,
    "Zopiclone": 15
}

# Äquivalente Dosen zu anderen Benzodiazepinen berechnen und anzeigen
for benzo, equivalent in benzos.items():
    equivalent_dose = peak_conc_mg * equivalent / 10
    print(f"{benzo}: {equivalent_dose:.2f} mg")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(days, diazepam_conc, label='Diazepam')
plt.plot(days, n_desmethyldiazepam_conc, label='N-Desmethyldiazepam')
plt.xlabel("Time (days)")
plt.ylabel("Concentration (ng/ml)")
plt.title(f"Diazepam and N-Desmethyldiazepam Concentrations Over Time")
plt.legend()
plt.grid(True)
plt.show()
