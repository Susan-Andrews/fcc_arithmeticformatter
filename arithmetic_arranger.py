import re
def arithmetic_arranger(problems,solve=False):

  if(len(problems) > 5 ):
    return  "Error: Too many problems."
  first=""
  second=""
  lines=""
  sumx=""
  string=""
  for problem in problems:
    if (re.search("[^\s0-9.+-]",problem)):
      if(re.search("[/]",problem) or re.search("[*]",problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."
    firstnumber=problem.split(" ")[0]
    operator=problem.split(" ")[1]
    secondnumber=problem.split(" ")[2]
    if(len(firstnumber)>=5 or len(secondnumber)>=5):
      return "Error: Numbers cannot be more than four digits."
      
    sum=""
    if (operator=="+"):
      sum=str(int(firstnumber) + int(secondnumber))
    elif  (operator=="-"):
      sum=str(int(firstnumber) - int(secondnumber))
    
    length=max(len(firstnumber),len(secondnumber)) + 2
    top=str(firstnumber).rjust(length)
    bottom=operator + str(secondnumber).rjust(length - 1)
    line = ""
    
    res=str(sum).rjust(length)
    for s in range(length):
      line += "-"
    if problem != problems[-1]:
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else :
      first += top 
      second += bottom 
      lines += line 
      sumx += res 
  if solve:
    string=first + "\n" + second + "\n" + lines + "\n" +sumx 
  else :
    string=first + "\n" + second + "\n" + lines
  return string  

    
    
