#python-challenge PyBank script

#Import modules
import os
import csv

file_path = os.path.join(".", "budget_data.csv")


with open (file_path, "r") as fin_data:
    
    reader = csv.reader(fin_data, delimiter=",")
    print(reader)
    
    #Init. variables
    month_count = 0
    total_rev = 0
    rev_change = 0
    curr_month_rev = 0
    prev_month_rev = 0
    months = []
    rev_changes = []
    
    #Check for header row
    csv_header = next(reader)
    print(f"Column headers: {csv_header}" + "\n")
    
    
    for row in reader:
        month_count = (month_count + 1)
        months.append(row[0])
        curr_month_rev = int(row[1])
        total_rev = total_rev + curr_month_rev
        
        if month_count > 1:
            rev_change = curr_month_rev - prev_month_rev
            rev_changes.append(rev_change)
            
            prev_month_rev = curr_month_rev
            
       
       #Month by month results
            if month_count >1:
            
                rev_change = sum(rev_changes)
                avg_rev_change = round((rev_change/(month_count - 1)), 2)
                    
                max_change = max(rev_changes)
                min_change = min(rev_changes)
                
                max_month_index = rev_changes.index(max_change)
                min_month_index = rev_changes.index(min_change)
                
                max_month = months[max_month_index]
                min_month = months[min_month_index]
        
print("PyBank Financial Analysis")
print(f"Total months: {month_count}")
print(f"Total revenue (profits/losses): ${total_rev}")
print(f"Average revenue change: ${avg_rev_change}")
print(f"Greatest increase in revenue: {max_month} (${max_change})")
print(f"Greatest decrease in revenue: {min_month} (${min_change})")

 

#Write summary to new file
with open("PyBank_output_file.txt", "w") as text:
    text.write("PyBank Financial Analysis" + "\n")
    text.write(f"Total months: {month_count}" + "\n")
    text.write(f"Total revenue (profits/losses): ${total_rev}" + "\n") 
    text.write(f"Average revenue change: ${avg_rev_change}" + "\n")
    text.write(f"Greatest increase in revenue: {max_month} (${max_change})" + "\n")
    text.write(f"Greatest decrease in revenue: {min_month} (${min_change})" + "\n")
