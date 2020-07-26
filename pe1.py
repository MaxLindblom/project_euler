#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

from modules.result_writer import update_results

def main():
    mul_sum = 0
    for i in range(1000):
        if i % 3 == 0:
            mul_sum = mul_sum + i
        elif i % 5 == 0:
            mul_sum = mul_sum + i

    update_results(mul_sum, 1)

main()