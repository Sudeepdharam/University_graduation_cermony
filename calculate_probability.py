class University():
    def __init__(self, no_of_days):
        '''
        Intialization of all the required variables
        '''
        self.current_attendance = ""
        self.absence_attendance_counter = 0
        self.total_university_days = no_of_days
        self.days_counter = 0
        self.absent_flag = False
        self.count_ways_to_attend_classes = 0
        self.count_ways_to_miss_graduation = 0
        self.calculate_attendance_probability(self.current_attendance, self.days_counter,
                                              self.absence_attendance_counter, self.total_university_days,
                                              self.absent_flag)
    
    def calculate_attendance_probability(self, current_attendance, absence_attendance_counter,\
                                         days_counter, total_university_days, absent_flag):
        """
        Calculation of number of ways to attend college and
        probability of missing graduation
        """
        if absence_attendance_counter < 4:
            absent_flag = False
        else:
            absent_flag =  True
            return

        if days_counter == total_university_days:
            if absent_flag == True:
                return
            if current_attendance == 'A':
                self.count_ways_to_miss_graduation = self.count_ways_to_miss_graduation + 1
            self.count_ways_to_attend_classes = self.count_ways_to_attend_classes+ 1
            return
        else:
            pass
        
        # Checking the probablity of present days
        self.calculate_attendance_probability(current_attendance = "P", 
                                              days_counter = days_counter+1,
                                              absence_attendance_counter = 0,
                                              total_university_days = total_university_days,
                                              absent_flag = absent_flag)
        # Checking the probability of absent days
        self.calculate_attendance_probability(current_attendance = "A", 
                                              days_counter = days_counter+1,
                                              absence_attendance_counter = absence_attendance_counter+1,
                                              total_university_days = total_university_days,
                                              absent_flag = absent_flag)
        return
    
    def get_probability_result(self):
        """
        Print the output as per requirement
        """
        print("for {0} days: {1}/{2}".format(self.total_university_days,
                                              str(self.count_ways_to_miss_graduation),
                                              str(self.count_ways_to_attend_classes)))


no_of_days = int(input("Enter the number of days: "))
university_obj = University(no_of_days)
university_obj.get_probability_result()





# Approach:

# •	Each day has two choices -> attend (present) or skip (absent) class.
# •	Initially, lets explore the probability of attending class recursively while considering constraints(attending the total number of college days).
# •	Then, backtrack to explore the probability of missing class recursively while considering constraints(not missing more than 4 days in a row).
# •	Track the absence-attendance counter to ensure that missing attendance doesn't exceed 4 consecutive days.
# •	If absence-attendance counter < 4 and total college days attended then take into consideration for count_ways_to_attend_classes.
# •	If last(Nth) day attendence is absent then take into consideration for count_ways_to_miss_graduation.
