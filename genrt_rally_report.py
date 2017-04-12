#Author: Ahmad Faheem, Manasi Shah
#Author gmail: afaheem88@gmail.com, manasishah24@gmail.com
<<<<<<< HEAD
#This script helps create the list of Passed, Failed and Skipped test cases from rally verify result, with rally version 9.0.0
=======
#This script helps create the list of Passed, Failed and Skipped test cases from rally verify result, with rally version 9.0.0
>>>>>>> 49108e456a0166f3946e39fe6eaf70ee4c4b53e0

#Usage: python genrt_rally_report.py rally_report_filename 
#Sample Usage: rally verify show --uuid $uuid > rally_report.txt; python genrt_rally_report.py rally_report.txt

import sys

def get_test_name(line):
    split_line = line.split('|')
    return split_line[1].strip()

def main():
    filename = sys.argv[1]
    failed = []
    passed = []
    skipped = []
    with open(filename, 'r') as fd:
        lines = [line.strip() for line in fd.readlines()]
        length = len(lines)
        count = 0
        while count < length:
            if "| success |" in lines[count]:
                passed.append(get_test_name(lines[count]))
            elif "| skip    |" in lines[count]:
                skipped.append(get_test_name(lines[count]))
            elif "| fail    |" in lines[count]:
                failed.append(get_test_name(lines[count]))
            count += 1
    print "*********************************************Passed test cases*******************************************************"
    for test in passed:
        print test
    print "*********************************************Failed test cases*******************************************************"
    for test in failed:
        print test
    print "*********************************************Skipped test cases*******************************************************"
    for test in skipped:
        print test

if __name__ == '__main__':
    main()
