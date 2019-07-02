from functools import reduce

class ReliefCalculator:
    def relief_calc(self, parameter_list):
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