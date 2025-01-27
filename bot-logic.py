import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
    return password

def gen_emodji():
    emodji = ["😄", "😸", "😏", "😊"] 
    return random.choice(emodji)

def gen_coin():
    coin= ["😶", "🪙"] 
    return random.choice(coin)
    
   
def gen_dice():
    dice = [":one:",":two:", ":three:", ":four:", ":five:" , ":six: "]
    return random.choice(dice)

#doble letra
# def double_letter(a):
#     result = ''
#     for letter in str(a):
#         result += letter * 2
#     return result
#funcion secreta
def secret_function(a, b):
    print (a,b)
    return " "

print("hola")
print(secret_function(1, 2))

