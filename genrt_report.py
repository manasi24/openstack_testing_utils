#Author: Ahmad Faheem
#Author gmail: afaheem88@gmail.com
#Tempest prior to versions 15.0.0, creates a file under tempest/.testrepository with numbers as their filenames.
#This script helps create the list of Passed, Failed and Skipped test cases
#It also includes the check for designate and murano plugins.

#Usage: python genrt_report.py tempest/.testrepository/filename 
#Sample Usage: python genrt_report.py tempest/.testrepository/1 

import sys

def get_test_name(line):
    try:
        if 'setUpClass' in line or 'tearDownClass' in line:
            return line[line.index('(')+1:line.index(')')]
        else:
            return line[6:]
    except Exception:
        print line
        raise

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
            if "test: " in lines[count]:
                if "failure: " in lines[count+2]:
                    failed.append(get_test_name(lines[count]))
                elif "successful: tempest" in lines[count+2]:
                    passed.append(get_test_name(lines[count]))
                elif "successful: designate_tempest_plugin" in lines[count+2]:
                    passed.append(get_test_name(lines[count]))
                elif "successful: murano_tempest_tests" in lines[count+2]:
                    passed.append(get_test_name(lines[count]))
                elif "skip: " in lines[count+2]:
                    skipped.append(get_test_name(lines[count]))
                count += 2
            else:
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
