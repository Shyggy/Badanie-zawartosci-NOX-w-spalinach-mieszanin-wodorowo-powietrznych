import cantera as ct
import matplotlib.pyplot as plt

n = 25  # number of steps
k = 0.04  # step length
equivalence_ratios = [0.2 + (i * k) for i in range(n)]  # vector containing equivalence ratios
# Approach 1 - representing engines older in technology
A1_no_molar_fraction = []
A1_no2_molar_fraction = []
A1_temp_in = 1500  # initial temperature in Kelvins
A1_pressure_in = 1e6  # initial pressure in Pascals
for equivalence_ratio in equivalence_ratios:
    A1 = ct.Solution('gri30.yaml')
    A1.TPX = A1_temp_in, A1_pressure_in, f'H2:{equivalence_ratio}, O2:0.5, N2:1.88'

    # define simulation duration
    A1_reaction_time = 1  # Reaction extent in seconds

    # perform the combustion simulation in constant pressure for Brayton cycle
    A1_reactor = ct.IdealGasConstPressureReactor(A1)
    A1_sim = ct.ReactorNet([A1_reactor])
    A1_sim.advance(A1_reaction_time)

    # fill vectors containing info about molar fractions of nox
    A1_no_molar_fraction.append(A1.X[35])
    A1_no2_molar_fraction.append(A1.X[36])

A1_nox_molar_fraction = []
for i in range(len(A1_no_molar_fraction)):
    A1_nox_molar_fraction.append(A1_no_molar_fraction[i] + A1_no2_molar_fraction[i])
A1_nox_molar_concentration = []
for i in range(len(A1_no_molar_fraction)):
    A1_nox_molar_concentration.append(A1_nox_molar_fraction[i] * 100)
fig1 = plt.figure(1)
plt.plot(equivalence_ratios, A1_nox_molar_concentration)
plt.xlabel('Equivalence ratio, φ')
plt.ylabel('Molar concentration of NOx, [%]')
plt.title('Relation between molar concentration of NOx and equivalence ratio for Engine 1')
plt.grid(True)

# Approach 2 - representing engines in modern technology
A2_no_molar_fraction = []
A2_no2_molar_fraction = []
A2_temp_in = 1700  # initial temperature in Kelvins
A2_pressure_in = 3.5e6  # initial pressure in Pascals
for equivalence_ratio in equivalence_ratios:
    A2 = ct.Solution('gri30.yaml')
    A2.TPX = A2_temp_in, A2_pressure_in, f'H2:{equivalence_ratio}, O2:0.5, N2:1.88'

    # define simulation duration
    A2_reaction_time = 1  # Reaction duration in seconds

    # perform the combustion simulation in constant pressure
    A2_reactor = ct.IdealGasConstPressureReactor(A2)
    A2_sim = ct.ReactorNet([A2_reactor])
    A2_sim.advance(A2_reaction_time)

    # fill vectors containing info about molar fractions of nox
    A2_no_molar_fraction.append(A2.X[35])
    A2_no2_molar_fraction.append(A2.X[36])

A2_nox_molar_fraction = []
for i in range(len(A2_no_molar_fraction)):
    A2_nox_molar_fraction.append(A2_no_molar_fraction[i] + A2_no2_molar_fraction[i])
A2_nox_molar_concentration = []
for i in range(len(A2_no_molar_fraction)):
    A2_nox_molar_concentration.append(A2_nox_molar_fraction[i] * 100)
fig2 = plt.figure(2)
plt.plot(equivalence_ratios, A2_nox_molar_concentration)
plt.xlabel('Equivalence ratio, φ')
plt.ylabel('Molar concentration of NOx, [%]')
plt.title('Relation between molar concentration of NOx and equivalence ratio for Engine 2')
plt.grid(True)

# Approach 3 - representing engines in possible future technology
A3_no_molar_fraction = []
A3_no2_molar_fraction = []
A3_temp_in = 1900  # initial temperature in Kelvins
A3_pressure_in = 5e6  # initial pressure in Pascals
for equivalence_ratio in equivalence_ratios:
    A3 = ct.Solution('gri30.yaml')
    A3.TPX = A3_temp_in, A3_pressure_in, f'H2:{equivalence_ratio}, O2:0.5, N2:1.88'

    # define simulation time
    A3_reaction_time = 1  # Reaction extent in seconds

    # perform the combustion simulation in constant volume
    A3_reactor = ct.IdealGasConstPressureReactor(A3)
    A3_sim = ct.ReactorNet([A3_reactor])
    A3_sim.advance(A3_reaction_time)

    # fill vectors containing info about molar fractions of nox
    A3_no_molar_fraction.append(A3.X[35])
    A3_no2_molar_fraction.append(A3.X[36])

A3_nox_molar_fraction = []
for i in range(len(A3_no_molar_fraction)):
    A3_nox_molar_fraction.append(A3_no_molar_fraction[i] + A3_no2_molar_fraction[i])
A3_nox_molar_concentration = []
for i in range(len(A3_no_molar_fraction)):
    A3_nox_molar_concentration.append(A3_nox_molar_fraction[i] * 100)
fig3 = plt.figure(3)
plt.plot(equivalence_ratios, A3_nox_molar_concentration)
plt.xlabel('Equivalence ratio, φ')
plt.ylabel('Molar concentration of NOx, [%]')
plt.title('Relation between molar concentration of NOx and equivalence ratio for Engine 3')
plt.grid(True)
plt.show()