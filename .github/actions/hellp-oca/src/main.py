import sys
import os

getEnvLeader = os.environ.get("INPUT_LEADER")
getEnvMember = os.environ.get("INPUT_MEMBER")

print("Hello " + getEnvLeader)
print("Hello " + getEnvMember)
