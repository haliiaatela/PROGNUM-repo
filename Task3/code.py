# q 3.1

masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

# Order: ‘Sun’, ‘Jupiter’, ‘Saturn’, ‘Neptune’, ‘Uranus’, ‘Earth’, ‘Venus’, ‘Mars’, ‘Mercury’, ‘Moon’, ‘Pluto’.


moon = masses[-2]
new_list = []

for M in masses:
    if M > moon:
        new_list.append(M)
        
print("New list =", new_list)
        
  
x =  slice(-5, -1)
list2 = masses[x]
print("2nd list =", list2) 

sum_ = sum(list2) / len(list2)
print(sum_)
