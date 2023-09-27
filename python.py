
telugu=int(input("enter telugu subject marks"))
hindi=int(input("enter hindi subject marks"))
english=int(input("enter english subject marks"))
maths=int(input("enter maths subject marks"))
science=int(input("enter science subject marks"))
social=int(input("enter social subject marks"))

print("\n given telugu marks are",telugu)
print("\n given hindi marks are",hindi)
print("\n given english marks are",english)
print("\n given maths marks are",maths)
print("\n given science marks are",science)
print("\n given social marks are",social)


total=telugu+hindi+english+maths+science+social
print("\n the total 6 subject marks are",total)


avg=total/6
print("\n the avg of 6 subjects marks",avg)

if(telugu<35):
    print("telugu subject failed",telugu)
    
if(hindi<35):
    print("hindi subject failed",hindi)
    
if(english<35):
    print("english subject failed",english)
    
if(maths<35):
    print("maths subject failed",maths)
    
if(science<35):
    print("science subject failed",science)
    
if(social<35):
    print("social subject failed",social)
    
if(telugu>hindi and telugu>english and telugu>maths and telugu>science and telugu>social):
    print("\n the telugu subject marks are higher than 5 subjects : ",telugu)

        
    
    
