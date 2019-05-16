# more conditional tests

test_sentence = ['elba', 'helena', 'amaranta', 'lindsey', 'martina']

print ("Test for equality and inequality with strings")
print (len(test_sentence) == 5)

print (len(test_sentence) == 4)

test_2_sentence = ['elba', 'helena', 'amaranta', 'lindsey', 'paulien']

print (test_sentence == test_2_sentence)

print("\nTesting using the .lower()")

print (test_sentence[0].lower() == test_2_sentence[0].lower())
print (test_sentence[0].lower() == test_2_sentence[-1].lower())

numero = 5

numeri = 4

print ("\nNumerical tests")
print(numero == numeri)
print (numero > numeri)
print (numero < numeri)
print (numeri != numero)

print ("\nTests using the and keyword and the or keyword")
print (numero and numeri != 7)
print (numero and numeri > 8)

print ("\nTest whether an item is in a list.")
ex = 'paulien'
if ex in test_sentence:
    print ("That lays in the past.")
else:
    print ("That's why it didn't work.")

print ("\nTest whether an item is not in a list.")
love = 'elba'
if love not in test_sentence:
    print ("I think you should talk.")
else:
    print ("She is the one.")