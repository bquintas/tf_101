import sys
from subprocess import call
from subprocess import check_output



# if len(sys.argv) != 4:
#     print ("Error wrong parameter number")
#     print ("Usage: python aws-cfn-helper-script.py region prefix destroy")
#     print ("Example: python aws-cfn-helper-script.py eu-central-1 myprefix False")
#     sys.exit(1)

# myregion = sys.argv[1]
# prefix = sys.argv[2]
# destroy = sys.argv[3]

mycommands = ["terraform"]

if destroy == "True":
    mycommands.extend(["destroy","--force"])
else:
    mycommands.extend(["apply"])

# mycommands.extend([ "-var", "region="+myregion , "-var", "prefix="+prefix])

print (mycommands)
call(mycommands)
