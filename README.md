# Election Analysis

## Overview of Election Audit Project

For this project we have been asked by Tom, a Colorado Board of Elections employee, to help with an audit of the election results of a U.S. Congressional Precinct in Colorado.  In order to complete this audit the following tasks must be completed:

1) Reporting the total number of votes cast
2) Collecting the complete list of candidates who received votes
3) Reporting the number of votes cast for each candidate
4) Reporting the percentage of votes each candidate received 
5) Reporting the winner of the election based on popular vote

This work is usually completed in Excel but we have been asked if the entire process can be automated using Python.  If the audit runs successfully then the same process can be reused to audit other elections (ex. congressional districts, senatorial districts, local elections).

## Resources 

 - Data Source: election_results.csv
 - Software: Python 3.6.1, Visual Studio Code 1.62.0

## Election Audit Results

The results of the election audit were posted to an output file using our Python script, as shown below:

![election_analysis_summary.PNG](https://github.com/mathur-nikita/Election_Analysis/blob/main/Resources/election_analysis_summary.PNG)

### Breakdown of Audit Results for Candidates:

1) The total number of votes that were cast in this election were 369,711 votes. 

2) The following candidates received votes during this election:
- Charles Casper Stockham
- Diana DeGette
- Raymon Anthony Doane
3) The number of votes cast for each candidate were as follows:
- Charles Casper Stockham received 85,213 votes.
- Diana DeGette received 272,892 votes.
- Raymon Anthony Doane received 11,606 votes.
4) The percentage of votes received per candidate is as follows:
- Charles Casper Stockham received 23.0% of the votes.
- Diana DeGette received 73.8% of the votes.
- Raymon Anthony Doane received 3.1% of the votes. 
5) The winner of this election was candidate Diana DeGette, who won the popular vote with 272,892 votes (73.8% of all votes).

### Breakdown of Audit Results for Counties:

1) Three counties were reported to have voters participating in this election:
- Jefferson County
- Denver County
- Arapahoe County
2) The number of votes cast per county were as follows:
- Jefferson County cast 38,855 votes.
- Denver County cast 306,055 votes.
- Arapahoe County cast 24,801 votes.
3) The percentage of votes cast per county is as follows:
- Jefferson County cast 10.5% of the votes.
- Denver County cast 82.8% of the votes.
- Arapahoe County cast 6.7% of the votes.
4) The county with the largest voter turnout was Denver County, with a voter turnout of 306,055 voters (82.8% of all voters participating in this election).

## Election Audit Summary

The Python script has been proven to successfully generate results for a congressional election and has the flexbility to be used for additional election audits.  

#### Mayoral Elections

The script can be adjusted to handle local mayoral elections.  Currently there are a few sections of code that are specific to tabulating data for counties, but those won't apply to city elections so they would need to be removed:

![code_segments_for_county_info.PNG](https://github.com/mathur-nikita/Election_Analysis/blob/main/Resources/code_segments_for_county_info.png)

Mayoral elections can have multiple rounds if none of the candidates receive 50% or more of the vote, so an additional result would need to be handled for this situation.  Currently the code is only accounting for majority wins:

![winning_candidate_congressional.png](https://github.com/mathur-nikita/Election_Analysis/blob/main/Resources/winning_candidate_congressional.PNG)

The updated code would look something like this, but probably with the addition of a few variable name changes for ease of reading (example all "winner_" variables would be renamed to "majority_" prefixes:

![mayoral_elections_code.PNG](https://github.com/mathur-nikita/Election_Analysis/blob/main/Resources/mayoral_elections_code.PNG)
