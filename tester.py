from homework_2 import homework_2

def run_tests(homework_num, amount_tests, func):

    for i in range(amount_tests):
        f_in = open(f'./homework_{homework_num}/test/test.{i}.in')

        in_value = f_in.read()

        f_in.close()

        f_out = open(f'./homework_{homework_num}/test/test.{i}.out')

        out_value = f_out.read()

        f_out.close()

        if int(out_value) == func(int(in_value)):
            print(f'Test №{i} Success')
        else:
            print(f'Test №{i} Failed')


run_tests(2, 10, homework_2.lucky)