Retirement Portfolio Monte Carlo Simulation
Introduction
This project aims to provide a dynamic and probabilistic visualization of an investor's retirement portfolio throughout their lifespan. It is designed for investors who wish to stress-test their retirement strategies and quantify the likelihood of not running out of money during retirement.

Unlike traditional portfolio calculators that use fixed return rates, this project leverages Monte Carlo simulations to generate random return rates that mimic the actual behavior of the market, which historically follows a normal distribution. The model is highly customizable, allowing users to adjust various parameters to reflect their financial situation and retirement goals.

Key Features:
Dynamic Simulation: Utilizes Monte Carlo methods to simulate numerous potential outcomes, providing a probabilistic view of portfolio performance.
Market Realism: Uses normally distributed random returns to reflect the actual volatility and unpredictability of the market.
Customizable Parameters: Users can modify inputs like tax rates, income, savings rate, return rates, inflation, and more to tailor the model to their specific needs.
Visual Insights: Generates visualizations to help users understand the potential growth and risks associated with their retirement portfolio.
Use Cases:
Retirement Planning: Helps investors visualize how their portfolio might evolve and what they can expect in different market conditions.
Risk Assessment: Allows users to evaluate the probability of their portfolio sustaining them through retirement, based on different risk scenarios.
Strategic Adjustments: Investors can experiment with different retirement ages, savings rates, and other factors to see how these changes affect their retirement success.
Diversified Investing Strategy
This project was inspired by the need for a more effective investment strategy after experiencing the drawbacks of active trading. Active investing often leads to inefficiency, higher taxes, and suboptimal returns. Research supports that a diversified, passive investment strategy, such as investing in index funds, is generally more effective.

Modern Portfolio Theory:
The foundation of this project is the concept of diversification. According to Markowitz's model, the most efficient portfolios are those that offer the highest returns with the lowest risk. Diversification reduces isolated risks and optimizes returns, which is the basis of the 'efficient frontier' in modern portfolio theory.

Assumptions
To ensure the model remains straightforward and focused, the following assumptions are made:

Index Fund Investment: The investor commits 100% of savings to a diversified index fund, with no withdrawals until retirement.
Non-Tax-Advantaged Account: The retirement account is a standard brokerage account, with withdrawals taxed as capital gains.
Steady Income Growth: The investor receives a constant annual pay raise throughout their working years.
Stable Expense Ratio: The chosen index fund maintains a consistent expense ratio over time.
Inflation: Long-term inflation is assumed to match the Federal Reserve's target, currently set at 2.5% (adjustable).
Savings Allocation: All income saved during working years is invested into the retirement portfolio.
Constant Real Withdrawals: Post-retirement, the investor withdraws a fixed amount adjusted for inflation to maintain their standard of living.
No Additional Savings Post-Retirement: Once retired, no further contributions are made to the retirement account.
Getting Started
Prerequisites
Python 3.x
Libraries: numpy, matplotlib
Installation
Clone the repository: git clone https://github.com/your-repo-name.git
Install the required libraries: pip install -r requirements.txt
Running the Simulation
Open the project directory.
Run the main script: python main.py
Adjust parameters as needed directly in the script or via a configuration file (if implemented).
Example Usage
After running the simulation, the program will output:

A plot of a single portfolio simulation showing the growth and decline over time.
Percentile-based visualizations that illustrate the range of potential portfolio values.
The probability of retirement success based on the simulation outcomes.
An analysis of how changing the retirement age affects the probability of success.
Contributing
Contributions to the project are welcome. Please submit a pull request or open an issue if you have any suggestions or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Markowitz, H.M.: For the foundational work in Modern Portfolio Theory.
