#!/usr/bin/env python3

'''
Assertions

-> Technically another control flow mechanism
-> It evaluates a boolean expression, if it's false, it raies an AssertionError
-> It can be used as a primitive version of testing and validation
-> Combined with decorators, you could build your small testing framework

Decorators

-> A very powerful functional programming technique
-> Add behavior to other functions on the fly
-> They are referenced with the @ symbol
-> They are technically a wrapper function, which within will execute the decorated function
-> You don't necessarily need assertions to use decorators, this is just an example

*** You can use this simple primitive testing technique in your projects
if you don't want to deep-dive into a testing framework ***
'''

TESTS_EXECUTED = 0
TESTS_PASSED = 0

def main():
    test_string = 'testme123'
    try:
        is_alpha_numeric_test(test_string)
        is_alpha_test(test_string) #This one raises an error
    except AssertionError as e:
        print(e)
    finally:
        print('{} tests passed out of {} executed.'.format(str(TESTS_PASSED), str(TESTS_EXECUTED)))

#Our Test decorator
def Test(to_decorate_function):
    '''
    -> This wrapper functions, all it does is to increase the counts before/after
    executing the actual logic
    -> We are "decorating" the function, which means we are adding additional behavior
    '''
    def test_function(test_value):
        global TESTS_EXECUTED, TESTS_PASSED
        TESTS_EXECUTED += 1
        to_decorate_function(test_value)
        TESTS_PASSED += 1
    return test_function

@Test
def is_alpha_numeric_test(string):
    assert string.isalnum(), 'Input String is not alphanumeric'

@Test
def is_alpha_test(string):
    assert string.isalpha(), 'Input String is not alphabetic only'

if __name__ == '__main__':
    main()