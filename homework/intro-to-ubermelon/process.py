log_file = open("um-server-01.txt") # open file


def sales_reports(log_file):        # generate report
    for line in log_file:           # for each line of file
        line = line.rstrip()        # remove extra white space right
        day = line[0:3]             # info of day-of-week 3-character
        if day == "Mon":            # change to 'Monday' logs
            print(line)             # print report line


sales_reports(log_file)             #ecall/execute function print report
