class IncomeManager:
    def __init__(self):
        self.income_sources = {}

    def add_income_source(self, source_name, amount):
        if source_name in self.income_sources:
            self.income_sources[source_name] += amount
        else:
            self.income_sources[source_name] = amount

    def get_income_sources(self):
        return self.income_sources

    def calculate_total_income(self):
        return sum(self.income_sources.values())
 