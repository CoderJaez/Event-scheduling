import numpy as np
import random as rand


class Simulation:
    def __init__(self):
        self.num_in_system = 0
        self.clock = 0.0

        self.t_arrival = self.generate_interarrival()
        self.t_depart = float('inf')

        self.num_arrivals = 0
        self.num_departs = 0
        self.total_wait = 0.0

    def advance_time(self):
        t_event = min(self.t_arrival, self.t_depart)

        self.total_wait += self.num_in_system * (t_event - self.clock)
        self.clock = t_event

        if self.t_arrival <= self.t_depart:
            self.handle_arrival_event()
        else:
            self.handle_depart_event()

    def handle_arrival_event(self):
        self.num_in_system += 1
        self.num_arrivals += 1
        if self.num_in_system <= 1:
            self.t_depart = self.clock + self.generate_service()
            # print("Generate departure time: ", self.t_depart)

        self.t_arrival = self.clock + self.generate_interarrival()

    def handle_depart_event(self):
        self.num_in_system -= 1
        self.num_departs += 1
        if self.num_in_system > 0:
            t_service = self.generate_service()
            # print("Generate service: ", t_service)
            self.t_depart = self.clock + t_service
        else:
            self.t_depart = float('inf')

    def generate_interarrival(self):
        # return rand.expovariate(1./3)
        return np.random.exponential(1./3)

    def generate_service(self):
        # return rand.expovariate(1./4)
        return np.random.exponential(1./4)

    def print_customer_event(self):
        print("")
        print("Clock: ", self.clock)
        print("Customer #: ", self.num_arrivals)
        print("Arrival time: ", self.t_arrival)
        print("Departure time: ", self.t_depart)

    def generate_reports(self):
        # print("\n")
        print("Current customers: ", self.num_in_system)
        print("Total arrivals: ", self.num_arrivals)
        print("Total departure: ", self.num_departs)
        print("Total wait time: ", self.total_wait)
        print("Average total wait per customemr: ",
              self.total_wait / self.num_departs)


# rand.seed(0)
np.random.seed(0)
s = Simulation()
# s.advance_time()
# s.print_customer_event()

# s.advance_time()
# s.print_customer_event()

# s.advance_time()
# s.print_customer_event()

# s.advance_time()
# s.print_customer_event()

for i in range(100):
    s.advance_time()

s.generate_reports()
