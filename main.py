import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.escape_characters as escape_characters
import basics.output.ascii_art as ascii_art

import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.review as review
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input

import basics.decisions.simple_decision.counter as counter
import basics.decisions.simple_decision.decision_if as decision_if
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.modulo_operator as modulo_operator
import basics.decisions.simple_decision.and_operator as and_operator
import basics.decisions.simple_decision.or_operator as or_operator
import basics.decisions.simple_decision.review as decision_review

import basics.decisions.nested_decision.nestception as nestception
import basics.decisions.nested_decision.nested as nested

import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.for_loop.range as range
import basics.repetitions.for_loop.reverse as reverse
import basics.repetitions.for_loop.simple as simple_for_loop

import basics.repetitions.nested_loop.nested as nested_loop
import basics.repetitions.nested_loop.nesting as nesting

import basics.repetitions.while_loop.ascii as ascii
import basics.repetitions.while_loop.count as count
import basics.repetitions.while_loop.factorial as factorial
import basics.repetitions.while_loop.len as len
import basics.repetitions.while_loop.simple as simple_while_loop
import basics.repetitions.while_loop.sum_100 as sum_100
import basics.repetitions.while_loop.sum_user_numbers as sum_user_numbers

import basics.functions.ascii_character as ascii_character
import basics.functions.ascii_code as ascii_code
import basics.functions.function_calls as function_calls
import basics.functions.function_with_loop as f_with_loop
import basics.functions.function_with_nesting as f_with_nesting
import basics.functions.function_with_parameter as f_with_parameter
import basics.functions.function_with_parameters as f_with_parameters
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_values
import basics.functions.simple_function as simple_function

import basics.modules.guess_the_number as guess_the_number
from basics.decisions.simple_decision import comparison_operators
from basics.repetitions.for_loop import count_down


def run_block_a():
    while (True):
        print("""Run any of the following from Block A: Basics:
                 [a] : Outputs
                 [b] : Inputs
                 [c] : Simple Decisions
                 [d] : Nested Decisions
                 [e] : Repetitions: While Loops
                 [f] : Repetitions: For Loops
                 [g] : Repetitions: Nested Loops
                 [h] : Functions
                 [i] : Modules
                 [m] : Main menu """)
        response = input()

        if response == "a":
            run_output()
        elif response == "b":
            run_input()
        elif response == "c":
            run_simple_decisions()
        elif response == "d":
            run_nested_decisions()
        elif response == "e":
            run_while_loops()
        elif response == "f":
            run_for_loops()
        elif response == "g":
            run_nested_loops()
        elif response == "h":
            run_functions()
        elif response == "i":
            run_modules()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")

def run_output():
    while (True):
        print("""Run any of the following from Block A: Outputs:
                 [a] : simple_message.py
                 [b] : multiline_message.py
                 [c] : escape_characters.py
                 [d] : ascii_art.py
                 [m] : Block A Menu """)
        response = input()

        if response == "a":
            simple_message.run()
        elif response == "b":
            multiline_message.run()
        elif response == "c":
            escape_characters.run()
        elif response == "d":
            ascii_art.run()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")

def run_input():
    while (True):
        print("""Run any of the following from Block A: Inputs:
                 [a] : ascii_robot.py
                 [b] : data_types.py
                 [c] : review.py
                 [d] : string_operators.py
                 [e] : user_input.py
                 [m] : Block A Menu """)
        response = input()

        if response == "a":
            ascii_robot.run()
        elif response == "b":
            data_types.run()
        elif response == "c":
            review.run()
        elif response == "d":
            string_operators.run()
        elif response == "e":
            user_input.run()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")

def run_simple_decisions():
    while (True):
        print("""Run any of the following from Block A: Simple Decisions:
                 [a] : comparison_operators.py
                 [b] : counter.py
                 [c] : if.py
                 [d] : if_elif_else.py
                 [e] : if_else.py
                 [f] : modulo_operator.py
                 [g] : and_operator.py
                 [h] : or_operator.py
                 [i] : review.py
                 [m] : Block A Menu """)
        response = input()

        if response == "a":
            comparison_operators.run()
        elif response == "b":
            counter.run()
        elif response == "c":
            decision_if.run()
        elif response == "d":
            if_elif_else.run()
        elif response == "e":
            if_else.run()
        elif response == "f":
            modulo_operator.run()
        elif response == "g":
            and_operator.run()
        elif response == "h":
            or_operator.run()
        elif response == "i":
            decision_review.run()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")


def run_nested_decisions():
    while (True):
        print("""Run any of the following from Block A: Nested Decisions:
                 [a] : nestception.py
                 [b] : nested.py
                 [m] : Block A Menu """)
        response = input()

        if response == "a":
            nestception.run()
        elif response == "b":
            nested.run()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")

def run_while_loops():
    while (True):
        print("""Run any of the following from Block A: Repetitions: While loops:
                 [a] : ascii.py
                 [b] : count.py
                 [c] : factorial.py
                 [d] : len.py
                 [e] : simple.py
                 [f] : sum_100.py
                 [g] : sum_user_numbers.py
                 [m] : Block A Menu """)
        response = input()

        if response == "a":
            ascii.run()
        elif response == "b":
            count.run()
        elif response == "c":
            factorial.run()
        elif response == "d":
            len.run()
        elif response == "e":
            simple_while_loop.run()
        elif response == "f":
            sum_100.run()
        elif response == "g":
            sum_user_numbers.run()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")


def run_for_loops():
    while (True):
        print("""Run any of the following from Block A: Repetitions: For loops:
                 [a] : characters.py.py
                 [b] : count_down.py
                 [c] : membership_operators.py
                 [d] : range.py
                 [e] : reverse.py
                 [f] : simple.py
                 [m] : Block A Menu """)
        response = input()

        if response == "a":
            characters.run()
        elif response == "b":
            count_down.run()
        elif response == "c":
            membership_operators.run()
        elif response == "d":
            range.run()
        elif response == "e":
            reverse.run()
        elif response == "f":
            simple_for_loop.run()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")


def run_nested_loops():
    while (True):
        print("""Run any of the following from Block A: Repetitions: Nested Loops:
                 [a] : nested.py
                 [b] : nesting.py
                 [m] : Block A Menu """)
        response = input()

        if response == "a":
            nested_loop.run()
        elif response == "b":
            nesting.run()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")

def run_functions():
    while (True):
        print("""Run any of the following from Block A: Functions:
                 [a] : ascii_character.py
                 [b] : ascii_code.py
                 [c] : function_calls.py
                 [d] : function_with_loop.py
                 [e] : function_with_nesting.py
                 [f] : function_with_parameter.py
                 [g] : function_with_parameters.py
                 [h] : multiple_functions.py
                 [i] : return_values.py
                 [j] : simple_function.py
                 [m] : Block A Menu """)
        response = input()

        if response == "a":
            ascii_character.run()
        elif response == "b":
            ascii_code.run()
        elif response == "c":
            function_calls.run()
        elif response == "d":
            f_with_loop.run()
        elif response == "e":
            f_with_nesting.run()
        elif response == "f":
            f_with_parameter.run()
        elif response == "g":
            f_with_parameters.run()
        elif response == "h":
            multiple_functions.run()
        elif response == "i":
            return_values.run()
        elif response == "j":
            simple_function.run()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")

def run_modules():
    while (True):
        print("""Run any of the following from Block A: Modules:
                 [a] : guess_the_number.py
                 [m] : Block A Menu """)
        response = input()

        if response == "a":
            guess_the_number.run()
        elif response == "m":
            break
        else:
            print("Invalid option! Please try again.")














def run():

    while(True):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' list of programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_block_a()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()