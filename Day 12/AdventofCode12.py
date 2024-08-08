with open("input12", "r") as gameInfo:
    lines = gameInfo.readlines()
    lineWoutN = []
    for i in lines:
        lineWoutN.append(i.replace("\n", ""))

def validOptions(report, nums):
  result = 0
  if report == "":
    return 1 if nums == () else 0
  if nums == ():
    return 0 if '#' in report else 1

  key = (report, nums)

  if report[0] in ".?":
    result += validOptions(report[1:], nums)
  if report[0] in "#?":
    if nums[0] <= len(report) and "." not in report[:nums[0]] and (nums[0] == len(report) or report[nums[0]] != "#"):
      result += validOptions(report[nums[0] + 1:], nums[1:] )

  return result

task1Total = 0

for line in lineWoutN:
  report, nums = line.split(" ")
  nums = tuple(map(int, nums.split(",")))
  task1Total += validOptions(report, nums)

print(f'Task 1: {task1Total}')
