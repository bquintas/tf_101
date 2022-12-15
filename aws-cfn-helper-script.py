import sys
from subprocess import call
from subprocess import check_output



if len(sys.argv) != 2:
    print ("Error wrong parameter number")
    print ("Usage: python aws-cfn-helper-script.py $destroy")
    print ("Example: python aws-cfn-helper-script.py False")
    sys.exit(1)

destroy = sys.argv[1]

mycommands = ["terraform"]

if destroy == "True":
    mycommands.extend(["destroy","--force"])
else:
    mycommands.extend(["apply","yes"])

print (mycommands)
call(mycommands)
