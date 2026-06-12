dict = { 
  "table" :{
       "a": "a piece of furniture",
       # "b": "list of factual figures",
    },
   "cat" : "a small animal " ,
}
print(dict["table"])

set = { "python", "java", "c++", "c#", "python","javasript","java","c++","c"}
print(len(set))

dict ={}

a = int(input("marks of pys:"))
b = int(input("marks of java:"))
c = int(input("marks of c++:"))

marlist = [a,b,c]
dict["marks"] = marlist
print(dict)