#Write a function that takes camel-cased strings (i.e.
#ThisIsCamelCased), and converts them to snake case (i.e.
#this_is_camel_cased). Modify the function by adding an argument,
#separator, so it will also convert to the kebab case (i.e.this-is-camel-case) as well.

dummy = "ThisIsCamelCased"
print("Original Camel Cased: ", dummy)

#To Snake case

def snake_case(camel_cased):

    #lower = camel_cased.lower()
    lists = [camel_cased[0].lower()]
    for i in range(1, len(camel_cased)):
        if camel_cased[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            lists.append('_')
            lists.append(camel_cased[i].lower())
        else:
            lists.append(camel_cased[i])
    return ''.join(lists)

snake_cased_result = snake_case(dummy)
print("This is snake cased: ", snake_cased_result)



#To Kebab case with separator

def kebab_case(camel_cased, separator):

    lists = [camel_cased[0].lower()]
    for i in range(1, len(camel_cased)):
        if camel_cased[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            lists.append(separator)
            lists.append(camel_cased[i].lower())
        else:
            lists.append(camel_cased[i])
    return ''.join(lists)


kebab_cased_result = kebab_case(dummy, '-')
print("This is kebab cased: ", kebab_cased_result)




