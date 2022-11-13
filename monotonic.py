def monotonic_equations(t, T):
    S0_new = S0*(0.75 + 0.25*(t/(4000*31557600))) #31557600 is the number of seconds per year
    dT1_dt = (1/(rho[0]*c[0]*Zed[0]))*((gamma_1*(1-ALPHA_SKY)*(1-alpha[0]))*S0_new - TAU*SIGMA_B*(T[0]**4)) + (((L12*k12)*(T[1] - T[0])) / (A1*rho[0]*c[0]*Zed[0]))
    dT2_dt = (1/(rho[1]*c[1]*Zed[1]))*((gamma_2*(1-ALPHA_SKY)*(1-alpha[1]))*S0_new - TAU*SIGMA_B*(T[1]**4)) + (((L23*k23*(T[2] - T[1]))-(L12*k12*(T[1] - T[0])))/(A2*rho[1]*c[1]*Zed[1]))
    dT3_dt = (1/(rho[2]*c[2]*Zed[2]))*((gamma_3*(1-ALPHA_SKY)*(1-alpha[2]))*S0_new - TAU*SIGMA_B*(T[2]**4)) + (((L34*k34*(T[3] - T[2]))-(L23*k23*(T[2] - T[1])))/(A3*rho[2]*c[2]*Zed[2]))
    dT4_dt = (1/(rho[3]*c[3]*Zed[3]))*((gamma_4*(1-ALPHA_SKY)*(1-alpha[3]))*S0_new - TAU*SIGMA_B*(T[3]**4)) + (((L45*k45*(T[4] - T[3]))-(L34*k34*(T[3] - T[2])))/(A4*rho[3]*c[3]*Zed[3]))
    dT5_dt = (1/(rho[4]*c[4]*Zed[4]))*((gamma_5*(1-ALPHA_SKY)*(1-alpha[4]))*S0_new - TAU*SIGMA_B*(T[4]**4)) + (((L56*k56*(T[5] - T[4]))-(L45*k45*(T[4] - T[3])))/(A5*rho[4]*c[4]*Zed[4]))
    dT6_dt = (1/(rho[5]*c[5]*Zed[5]))*((gamma_6*(1-ALPHA_SKY)*(1-alpha[5]))*S0_new - TAU*SIGMA_B*(T[5]**4)) - (((L56*k56)*(T[5] - T[4])) / (A6*rho[5]*c[5]*Zed[5]))
    return np.array([dT1_dt, dT2_dt, dT3_dt, dT4_dt, dT5_dt, dT6_dt])

init_temps = np.zeros(6)
init_temps[0] = 244.31043415
init_temps[1] = 256.9900539
init_temps[2] = 264.49181217
init_temps[3] = 262.18171593
init_temps[4] = 259.17096089
init_temps[5] = 247.23991597

this_method = 'DOP853'

# Define maximum allowable time step for solve_ivp.
max_dt = 276*24*3600

# Assign the results of solve_ivp to the variable 'sol'
sol = solve_ivp(monotonic_equations, [0,4000*31557600], init_temps, method=this_method, max_step=max_dt)

# Plot
plt.figure(figsize=(10,8))
plt.plot(sol.t/31557600, sol.y[5], label = 'Zone 6', color='lightblue')
plt.plot(sol.t/31557600, sol.y[4], label = 'Zone 5', color='lightgreen')
plt.plot(sol.t/31557600, sol.y[3], label = 'Zone 4', color='orange')
plt.plot(sol.t/31557600, sol.y[2], label = 'Zone 3', color='red', linestyle='dashed')
plt.plot(sol.t/31557600, sol.y[1], label = 'Zone 2', color='green', linestyle='dashed')
plt.plot(sol.t/31557600, sol.y[0], label = 'Zone 1', color='blue', linestyle='dashed')
plt.xlabel('time (years)')
plt.ylabel('Temperature (K)')
plt.title(f'Temperature Model (monotonic increase of solar constant) using solve_ivp: {this_method}') # (max. dt = {max_dt} s)')
plt.legend()
#plt.xlim(10000,10001)
plt.show()