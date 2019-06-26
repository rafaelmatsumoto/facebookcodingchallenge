from functools import reduce

class ReliefCalculator:
    def relief_calc(self, parameter_list):
        if all(previous >= next_number for previous, next_number in zip(parameter_list, parameter_list[1:])):
            return 0
        # elif max(parameter_list) == parameter_list[0] & parameter_list[0] != parameter_list[-1]:
        #     result = 0
        #     pivot = max(parameter_list[1:])
        #     for i in parameter_list[1:]:
        #         result += pivot - i
        #     return result
        else:
            result = self.calc_volume(parameter_list)
            result += self.calc_volume_retro(parameter_list[::-1])
            return result

    def calc_volume_retro(self, parameter_list):
        result = 0
        i = 0
        j = 0
        while j < len(parameter_list):
            if parameter_list[j] > parameter_list[i]:
                my_range = parameter_list[i:j]
                for k in my_range:
                    result += max(my_range) - k
                i = j 
            j += 1
        return result

    def calc_volume(self, parameter_list):
        result = 0
        i = 0
        j = 0
        while j < len(parameter_list):
            if parameter_list[j] >= parameter_list[i]:
                my_range = parameter_list[i:j]
                for k in my_range:
                    result += max(my_range) - k
                i = j 
            j += 1
        return result

calculator = ReliefCalculator()
print(calculator.relief_calc([6, 3, 2, 1, 5]))