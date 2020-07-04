'''Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid'''

class OrderOfParentheses:

    @staticmethod

    def check_valid(brackets):
        listing, parentheses_dict = [], {"(": ")", "{": "}", "[": "]"}
        for p in brackets:
            if p in parentheses_dict:
                listing.append(p)
            elif len(listing) == 0 or parentheses_dict[listing.pop()] is not p:
                return False
        return len(listing) == 0


print(OrderOfParentheses().check_valid("(){}[]"))
print(OrderOfParentheses().check_valid("{[}]}"))
print(OrderOfParentheses().check_valid("{{{"))
print(OrderOfParentheses().check_valid("{{{}}}[]()"))