import pickle as p
def Write():
    f=open('ElevenNov.dat','ab')
    data=input("Enter the data to be inserted into the file: ")
    p.dump(data,f) #pickle.dump(input data, file object)
    f.close()

def Read():
    f=open('ElevenNov.dat','rb')
    q=p.load(f)
    print(q)
    f.close()   
Write()
Read()