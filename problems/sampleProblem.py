
class SampleProblem:
    def calculate_cost(self, distance):
        if distance <= 0:
            raise ValueError("Distance must be greater than 0")
        base_cost = 50.0
        if distance <= 5:
            return base_cost
        else:
            extra_distance = distance - 5
            return base_cost + (extra_distance * 10)

def main():
    sample = SampleProblem()
    result = sample.calculate_cost(8)
    print(result)

if __name__ == "__main__":
    main()