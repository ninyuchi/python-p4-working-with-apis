
import json

class GetPrograms:
    def get_programs(self):
        # Simulate getting programs from an API
        api_response = '[{"agency": "School A"}, {"agency": "School B"}, {"agency": "School A"}]'
        return api_response

    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list

# Create an instance of GetPrograms
programs_instance = GetPrograms()

# Call the program_school method to get a list of schools
programs_schools = programs_instance.program_school()

# Print unique schools
for school in set(programs_schools):
    print(school)
