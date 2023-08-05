# Benzodiazepine Plasma Concentration Model
Warning: I'm currently in the process of comparing the data with the literature, hence the script is not providing reliable data at the moment. For the short-term simulation, the currently used data are calculated. However, for the long-term simulation, they are currently deviating significantly from reality.
## Overview

This Python script models the plasma concentrations of Diazepam and its metabolites over a 30-day span. The main objective is to compare the peak concentration of Diazepam, achieved post a single dosage, with the peak concentration of another Benzodiazepine. The Diazepam equivalent is calculated by summing the Diazepam concentration and the equivalent metabolite concentration.

## Context

Benzodiazepines are a class of psychoactive drugs commonly prescribed to treat conditions like anxiety and insomnia. They function by enhancing the effects of the gamma-aminobutyric acid (GABA) neurotransmitter in the brain, thereby inducing calming and sedative effects. Diazepam is among the most frequently prescribed Benzodiazepines.

The data used to construct the pharmacokinetic model in this script is derived from a study by J. A. S. Gamble, J. W. Dundee, and R. C. Gray titled "Plasma Diazepam Concentrations Following Prolonged Administration" published in the British Journal of Anaesthesia in 1976. Therefore, the modeled values for Diazepam and its metabolite concentrations should be reasonably accurate.

## Requirements

This script relies on the following Python libraries:

- matplotlib
- numpy

You can install these dependencies using the following command:

```
pip install matplotlib numpy
```

## Functionality

In the future, I aim to enable a more precise long-term simulation, with factors such as age, gender, and other medications taken into account. Given the complexity of this topic, it will take some time to implement these features.

The script calculates the Diazepam and metabolite concentrations in plasma over the specified duration using a pharmacokinetic model that considers the half-life of Diazepam and its metabolite. It then determines the time to reach the steady state, where the drug's input and elimination rates are balanced, leading to a stable concentration in the body.

The script also performs a comparison of the peak concentration of Diazepam with that of other Benzodiazepines. The user can set the equivalent dose of the other Benzodiazepine, and the script will calculate and display the equivalent Diazepam dose required to achieve the same peak concentration.

## Usage

1. Adjust the parameters in the script to establish desired values for initial dose, half-lives, conversion ratios, and more.

2. Execute the script by running the Python file:

```
python benzodiazepine_concentration.py
```

3. The console will display results, including the time when Diazepam reaches a steady state and when the Diazepam equivalent reduces to 5 mg. Additionally, the script will display the equivalent Diazepam dose required to achieve the peak concentration of the chosen Benzodiazepine.

4. The script also generates a plot of Diazepam and its metabolite concentrations over time, facilitating visual analysis of the drug's plasma profile.

## Disclaimer

This script serves primarily illustrative and comparative purposes, and it should not be used as a substitute for professional medical advice.

## License

This script is licensed under the MIT License. For more details, refer to the LICENSE file in this repository.
