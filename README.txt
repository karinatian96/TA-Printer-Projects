# CS9 TA Office Hours Queue Simulation

This program simulates an office hours queue for CS9 class

*Premise
1. The probability of receiving a new request every minute is 1/150. Since there are 150 probably students in the CS9 class. If there are more students, then for line 78, the range can be changed from 1 to any other numbers. 

2. The time taken to process each request is randomized between 1 to 30 minutes, which means the time interval for each TA and students will be around 1 minimum and 30 minutes maximum. 

3. The TA can only process one request at any given time.

*Equation
1. Average Waiting Time = Total Waiting Time / Number of Requests
2. TA processing time = Processing time of requests * 60 / Processing rate per minute

*Result Visualization

The result will show like the format "Average Wait xxx secs x tasks remaining" for x lines, which x means number of TA

*How to run the whole module

Download the pythonds in the computer. Run the `cs9extracredit.py` file in IDLE. The parameters of the `officeHourSimulation` function can be changed. 'numSeconds' is the number of seconds that need to serve for each students. 'requestPerMinute' is the request that gained for each minute. For the last equation, 'for i in range(x)", x means how many results need to generate, which also means the number of TA. 