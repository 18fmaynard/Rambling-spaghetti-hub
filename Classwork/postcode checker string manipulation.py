def incorect():
    print("That was not a valid post code!")
post_code = input("Please enter a post code: ")
upper_case = post_code.isupper()
if len(post_code) == 8:
    if upper_case == False:
        incorect()
    else:
        if post_code[0].isalpha() == False:
            incorect()
        else:
            if post_code[1].isalpha() == False:
                incorect()
            else:
                if post_code[2].isdigit() == False:
                    incorect()
                else:
                    if post_code[3].isdigit() == False:
                        incorect()
                    else:
                        if post_code[4].isspace() == False:
                            incorect()
                        else:
                            if post_code[5].isdigit() == False:
                                incorect()
                            else:
                             if post_code[6].isalpha() == False:
                                 incorect()
                             else:
                                   if post_code[7].isalpha() == False:
                                       incorect()
                                   else:
                                       print("Valid post code")
else:
    incorect()