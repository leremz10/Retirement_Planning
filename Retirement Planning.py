import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)

# Define Parameters and Initial Conditions
def get_parameters():
    return {
        'current_age': 25,
        'tax_rate': 0.2,
        'starting_savings': 25000,
        'current_gross_income': 70000,
        'raise_pct': 0.03,
        'income_saved': 0.15,
        'expense_ratio': 0.0018,
        'return_rate': 0.0682,
        'stdev': 0.152,
        'retirement_age': 67,
        'ret_income': 30000,
        'max_age': 95,
        'inf_rate': 0.025,
        'num_sims': 1000
    }

# Validate Parameters
def validate_parameters(params):
    if not (0 <= params['tax_rate'] <= 1):
        raise ValueError("Tax rate must be between 0 and 1.")
    if not (0 <= params['income_saved'] <= 1):
        raise ValueError("Income saved must be between 0 and 1.")
    if not (0 <= params['return_rate'] <= 1):
        raise ValueError("Return rate must be between 0 and 1.")
    if params['retirement_age'] <= params['current_age']:
        raise ValueError("Retirement age must be greater than current age.")

# Simulation Logic
def simulation_round(params, sim_idx, returns):
    years = params['max_age'] - params['current_age'] + 1
    working_years = params['retirement_age'] - params['current_age']

    # Pre-allocate arrays
    working_gross_income = np.zeros(years)
    taxes = np.zeros(years)
    working_income_saved = np.zeros(years)
    portfolio_value = np.zeros(years)
    mf_expense = np.zeros(years)
    real_net_income = np.zeros(years)
    annual_ret_reduction = np.zeros(years)

    # Initialize first year values
    working_gross_income[0] = params['current_gross_income']
    portfolio_value[0] = params['starting_savings']
    mf_expense[0] = portfolio_value[0] * params['expense_ratio']

    # Simulate working years
    for j in range(1, working_years):
        working_gross_income[j] = params['current_gross_income'] * (1 + params['raise_pct']) ** j
        taxes[j] = working_gross_income[j] * params['tax_rate']
        working_income_saved[j] = working_gross_income[j] * (1 - params['tax_rate']) * params['income_saved']
        portfolio_value[j] = (portfolio_value[j-1] + working_income_saved[j-1] - mf_expense[j-1]) * (1 + returns[sim_idx, j])

    # Simulate retirement years
    for j in range(working_years, years):
        real_net_income[j] = params['ret_income']
        net_income = real_net_income[j] * (1 + params['inf_rate']) ** j
        taxes[j] = net_income * params['tax_rate'] / (1 - params['tax_rate'])
        annual_ret_reduction[j] = net_income + taxes[j]
        portfolio_value[j] = (portfolio_value[j-1] - mf_expense[j-1] - annual_ret_reduction[j]) * (1 + returns[sim_idx, j])

    return portfolio_value

def run_simulation(params):
    logging.info("Starting simulations")

    years = params['max_age'] - params['current_age'] + 1
    returns = np.random.normal(params['return_rate'], params['stdev'], (params['num_sims'], years))

    # Parallel execution of simulations
    with mp.Pool(mp.cpu_count()) as pool:
        results = pool.starmap(simulation_round, [(params, i, returns) for i in range(params['num_sims'])])

    portfolio_values = np.array(results)

    logging.info("Simulations completed")
    return portfolio_values

# Calculate Probability of Success
def prob_success(portfolio_values, num_sims):
    successes = np.sum(portfolio_values[:, -1] > 0)
    return (successes / num_sims) * 100

# Plot Results
def plot_single_simulation(portfolio_values, params):
    years_plot = np.arange(params['max_age'] - params['current_age'] + 1)
    plt.figure()
    plt.plot(years_plot + params['current_age'], portfolio_values[0, :], color='g')
    plt.xlabel('Age')
    plt.ylabel('Portfolio Value')
    plt.title('Single Simulation of Portfolio Value')
    plt.grid()
    plt.show()

def plot_percentiles(portfolio_values, params):
    years_plot = np.arange(params['max_age'] - params['current_age'] + 1)
    fifteenth = np.percentile(portfolio_values, 15, axis=0)
    thirty = np.percentile(portfolio_values, 30, axis=0)
    median = np.median(portfolio_values, axis=0)
    seventy = np.percentile(portfolio_values, 70, axis=0)
    eighty_five = np.percentile(portfolio_values, 85, axis=0)

    plt.figure()
    plt.plot(years_plot + params['current_age'], fifteenth, 'r--', label='15th Percentile')
    plt.plot(years_plot + params['current_age'], thirty, 'y--', label='30th Percentile')
    plt.plot(years_plot + params['current_age'], median, 'k-', label='Median')
    plt.plot(years_plot + params['current_age'], seventy, 'b--', label='70th Percentile')
    plt.plot(years_plot + params['current_age'], eighty_five, 'g--', label='85th Percentile')
    plt.xlabel('Age')
    plt.ylabel('Portfolio Value (USD)')
    plt.title('Expected Portfolio Value by Percentile')
    plt.legend()
    plt.grid()
    plt.show()

# Main Execution
if __name__ == "__main__":
    params = get_parameters()
    validate_parameters(params)
    portfolio_values = run_simulation(params)
    plot_single_simulation(portfolio_values, params)
    plot_percentiles(portfolio_values, params)
    success_rate = prob_success(portfolio_values, params['num_sims'])
    print(f"Your retirement account's probability of success is: {success_rate:.2f}%")
