
# CS50 Final Project - Interest Calculator
#### Video Demo:  https://youtu.be/LRTGpONtfiA

The project is a streamlit web app that helps in calculating interest(both compound and simple), present value, future value or its period.
The app is currently deployed in the streamlit free cloud.Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience required

Technologies used:

- Python
- Streamlit frameword

`Streamlit is an open source app framework for Machine learning and Data Science projects.` 

## How the webpage works?
The app is very simple, it requires no signing up. User just need to choose what to calculate first. that is either:

- Future value
- Present Value
- Period
- Interest rate

as shown below:
![](images/2.png)

### Explanation of terms
1. Future Value[^1]
2. Present Value[^2]
3. Interest Rate[^3]
4. Terms(Periods)[^4]

[^1]: Future Value is a value an investor expected given a current value, interest rate and period(in years or month  or both).
[^2]: Present value is a value an investor needed current to acheive a target future value, interest rate and period(in years or month  or both).
This calculation is somethings needed in  discount loans.
[^3]: Interest rate. Here, you have a value and expecting some future value however you don't know an interest appropriate given some period.
[^4]: Finally, you may have the present value and your expected future value with the interest rate but you don't know how long you should allow to yeild that value in future.


### Routing

Its a single route page with no need of authentication.

### Sessions
Information provided is keep in session for each rerun for other computation.

### Database

No database Required

## Possible improvements

As all applications this one can also be improved. Possible improvements:

- Adding Amortization to it to handle loan management

## How to launch application

1. Clone the code: `git clone https://github.com/ankomahtony/asawa_interest_calculator.git`
2. Ensure python3 is install on your machine
3. Create an environment
4. Run command prompt `pip install -r requirements` to install all modules
4. Once installed run command `streamlit run app.py`
5. In your browser go to `localhost:8000`
6. You are ready to go!

or simple use my free cloud hosted
https://share.streamlit.io/ankomahtony/asawa_interest_calculator/app.py

