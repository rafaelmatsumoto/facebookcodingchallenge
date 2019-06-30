class RemainingInteger:
    def find_remaining_integer(self, parameter_list):
        parameter_list.sort()
        i = 0
        while i < len(parameter_list):
            if parameter_list[i] != parameter_list[i + 1] and parameter_list[i] != parameter_list[i + 2]:
                return parameter_list[i]
            i += 3

 