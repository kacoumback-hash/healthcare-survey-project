class User:

    def __init__(self, age, gender, income,
                 utilities_amount,
                 entertainment_amount,
                 school_amount,
                 shopping_amount,
                 healthcare_amount):

        self.age = age
        self.gender = gender
        self.income = income

        self.utilities_amount = utilities_amount
        self.entertainment_amount = entertainment_amount
        self.school_amount = school_amount
        self.shopping_amount = shopping_amount
        self.healthcare_amount = healthcare_amount

    def to_dict(self):

        return {
            "age": self.age,
            "gender": self.gender,
            "income": self.income,

            "utilities_amount": self.utilities_amount,
            "entertainment_amount": self.entertainment_amount,
            "school_amount": self.school_amount,
            "shopping_amount": self.shopping_amount,
            "healthcare_amount": self.healthcare_amount
        }