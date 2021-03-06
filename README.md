# The Python Challenge
There were two components for this challenge: (1) analysing the financial records of a company; and (2) modernising the vote-counting process in a small, rural town. In both cases, data analyses were sped up using Python.

## Analysing Financial Records
The records consisted of profits and losses over the span of 86 months. This [script](
      python-challenge/PyBank/main.py
    )
     was used to summarise the data. Results indicated that the company obtained a net profit of $38,382,578 over the period included in the analysis. Though posting a positive net profit, the month-by-month change was, on average, -$2315.12. The greatest increase in profit was recorded in February 2012 ($1,926,159) and was lower than the absolute value of the greatest decrease in profit; this was recorded in September 2013 (-$2,196,167). These indicators seem to suggest that the company is facing a loss trend rather than a profit trend. 

## Counting Votes
This [script](
      python-challenge/PyPoll/main.py
    ) 
    was used to hasten the counting of the votes. There were four candidates running for office in the small rural town. Of the 3,521,001 voters, 63% voted for Khan, making him the winner by popular vote (Table 1). 

Table 1. Results of the election

Candidate | No. of votes | Percentage (%)
----------|--------------|---------------
Khan|2218231|63.0
Correy|704200|20.0
Li|492940|14.0
O'Tooley|105630| 3.0
