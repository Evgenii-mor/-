

calls = 0
def count_calls():
    global calls
    calls +=1
def string_info(string):
    stroka = (str(string))
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result
def is_contains(string, list_to_searh):
    string = (str(string).lower())
    list_to_searh = list(list_to_searh)
    count_calls()
    for i in range(len(list_to_searh)):
        if str(list_to_searh[i]).lower() == string:
            result = True
            break
        else:
            result = False
        continue
    return result


print(string_info('Kalinka'))
print(string_info('Cavaleria'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))

print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)







