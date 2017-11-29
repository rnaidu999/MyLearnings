#Create a mapping of state to abbreviation
state ={"Oregon" : "OR",
        "Wahsington" : "WA",
        "Texas" : "TX",
        "California" : "CA",
        "Illinois" : "IL",
        "Georgia" : "GA"}

#Define Citis in the states
Citis ={"OR" : "Portland",
        "WA" : "Seattle",
        "CA" : "San Francisco",
        "IL" : "Chicago",
        "GA" : "Atlanta"}

state["New York"] = "NY"
state["Ohio"] ="OH"

Citis["NY"]="Albany"
Citis["OH"]="Columbs"
Citis["TX"]="Dallas"

#print ("\n",state,"\n")
#print (Citis)
#Print Some of states
print ("\n")
print ("*" * 30)
print ("New York ::", state["New York"])
print ("Oregon ::", state["Oregon"])
print ("*" * 30)

#Print soe of Cities
print ("\n")
print ("*" * 40)
print ("City in California ::", Citis["CA"])
print (f"City in Chicago :: {Citis['IL']}")
print ("*" * 40)

#Print every state abbreviation
print ("\n")
print ("*" * 40)
print (f"City in {state['Oregon']} : {Citis[state['Oregon']]}")
print (f"City in {state['New York']} : {Citis[state['New York']]}")
print ("*" * 40)
print ("\n")
print ("*" * 50)
state_abrv=[]

for state, abrv in list(state.items()):
    print (f"{state} State abbreviation \t :: \t {abrv}")
    state_abrv.append(abrv)

print ("*" * 50)
print ("\n")
#print cities in stage
print ("*" * 50)
for cities, abrv in list (Citis.items()):
    print (f"City in {cities} :: {abrv}")
print ("*" * 50)


#Get an item from state dinamics
print ("\n")
print ("*" * 50)
for stateid in state_abrv:
    print (f"City in {stateid} :: {Citis[stateid]}")
print ("*" * 50)
#state1=state.get("Chicago")
#print(state1)
