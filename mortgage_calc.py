class Mortgage:
    def __init__(self, input_home_cost, input_down_payment, input_h_interest_rate, input_loan_length):
        self.home_cost = input_home_cost
        self.down_payment = input_down_payment
        self.interest_rate = input_h_interest_rate
        self.loan_length = input_loan_length
        self.principal = input_home_cost - input_down_payment
        self.monthly_i_rate = (input_h_interest_rate / 100) / 12
        self.number_of_payments = input_loan_length * 12

    def __repr__(self):
        description = "This home costs {home_cost}, the downpayment is {down_payment}, the loan will be {loan_length} years at {interest_rate}%.".format(
            home_cost=self.home_cost, down_payment=self.down_payment, loan_length=self.loan_length, interest_rate=self.interest_rate)
        return description

    def monthly_payment(self):
        payment = round((self.principal * ((self.monthly_i_rate * (1 + self.monthly_i_rate) **
                                            self.number_of_payments) / ((1 + self.monthly_i_rate)**self.number_of_payments - 1))))
        print("${monthly_amount} Per Month".format(monthly_amount=payment))


# After adding this method to our class, let’s try printing out information about our dogs.
house_one = Mortgage(100000, 20000, 5, 30)
house_two = Mortgage(300000, 60000, 5, 30)

house_one.monthly_payment()
house_two.monthly_payment()
