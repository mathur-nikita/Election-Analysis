

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine majority vote count, majority percentage, and candidate.
        # Capturing this information for reporting.
        if (votes > majority_count) and (vote_percentage > majority_percentage):
            majority_count = votes
            majority_candidate = candidate_name
            majority_percentage = vote_percentage

    winning_candidate_summary = ""

    # If the candidiate with highest percentage of votes has 50% or more of the total votes for the city, they win.
    # Else, there is no winner in this election and another round of voting will need to take place in the future.
    if(majority_percentage >= 50.0):
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {majority_candidate}\n"
            f"Winning Vote Count: {majority_count:,}\n"
            f"Winning Percentage: {majority_percentage:.1f}%\n"
            f"-------------------------\n")
    else:
        winning_candidate_summary = (
            f"-------------------------\n"
            f"No winner - no candidate won 50% or more of the votes so a second round of voting will need to take place for this election.\n"
            f"Informational: the candidate with the votes is {majority_candidate} with {majority_percentage:.1f}% of the votes ({majority_count:,} votes)\n"
            f"-------------------------\n"            
        )

    # Print the winning candidate (to terminal)
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
