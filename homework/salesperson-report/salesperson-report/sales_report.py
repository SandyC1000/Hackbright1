"""Generate sales report showing total melons each salesperson sold."""

# Initialize lists of salespeople and melons_sold 
salespeople = []
melons_sold = []
# open file for sales_report
f = open('sales-report.txt')
for line in f:
    line = line.rstrip() # strip right blank space
    entries = line.split('|') # separated by |

    salesperson = entries[0]  # name of salesperson
    melons = int(entries[2])  # number of melons sold

    if salesperson in salespeople:  # add melons sold to corresponding salesperson
        position = salespeople.index(salesperson)

        melons_sold[position] += melons  # add melons to eachn salesperson
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# print report of salesperson/melons sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
