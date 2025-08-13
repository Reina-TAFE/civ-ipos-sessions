# a basic import
from test.greeter import Calculator
from test.student import Student

def greet(name):
    print(name)



# print(greet)
# use an alias - consider why might we do this?

def main():
    simple_add = Calculator([5, 9], "+")
    simple_subtract = Calculator([9, 5], "-")
    simple_mult = Calculator([9, 5], "*")
    simple_div = Calculator([90, 5], "/")
    simple_pow = Calculator([9, 5], "**")
    sums = [simple_add, simple_subtract, simple_mult, simple_div, simple_pow]
    student = Student("Reina", 20066312, ["python", "Java"], "12 real road, somewhere")
    print(student.id)
    student._set_id(30)
    print(student.id)

    for _ in sums:
        print(f"{_.get_method()}: {_.get_result()}")

# sometimes we only want to import what we need

# create a calculator class in the module

# use the new class to return a score to a user

if __name__ == "__main__":
    main()
