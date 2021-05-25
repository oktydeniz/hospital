from datetime import date


class Hospital:
    def __init__(self, name, address, departments, doctors):
        self.__name = name
        self.__address = address
        self.__departments = departments
        self.__doctors = doctors
        self.__appointment = []

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_departments(self):
        print("----- Departments -----")
        for i in self.__departments:
            print("""---> {department} """.format(department=i))

    def get_doctors(self):
        print("------Doctors------")
        for dr in self.__doctors:
            print(
                " FirstName : " + dr.get_first_name() +
                " LastName : " + dr.get_last_name() +
                " Phone Number :" + dr.get_number() +
                " Department :" + dr.get_department())

    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__departments = department

    def set_address(self, address):
        self.__address = address

    def set_doctor(self, doctor):
        self.__doctors = doctor

    def add_department(self, department):
        self.__departments.append(department)

    def add_doctors(self, doctor):
        self.__doctors.append(doctor)

    def take_appointment(self, patient, doctor, date_):
        flag = True
        for i in self.__appointment:
            current_date = i[2]
            current_doctor = i[1]
            if current_doctor == doctor and current_date == date_:
                print("Chance The Date or Doctor")
                flag = False
        if flag:
            self.__appointment.append((patient, doctor, date_))
            print("Done !")

    def get_appointment(self):
        appointment = 0
        print("All Appointments")
        for i in self.__appointment:
            current_patient = i[0]
            current_date = i[2]
            current_doctor = i[1]
            print(" Patient FirstName : " + current_patient.get_first_name() +
                  " Patient LastName  :" + current_patient.get_last_name() + "has an appointment with " +
                  current_doctor.get_first_name() + " " + current_doctor.get_last_name() + " on " +
                  current_date.strftime("%m/%d/%Y, %H:%M:%S"))
            appointment += 1
        if appointment == 0:
            print("Appointment List Empty")


class Person:
    def __init__(self, f_name, l_name, phone_number):
        self.__firsName = f_name
        self.__lastName = l_name
        self.__phoneNumber = phone_number

    def get_first_name(self):
        return self.__firsName

    def get_last_name(self):
        return self.__lastName

    def get_number(self):
        return self.__phoneNumber


class Doctor(Person):
    dr_sum = 0

    def __init__(self, f_name, l_name, phone_number, department):
        super().__init__(f_name, l_name, phone_number)
        Doctor.increase_dr()
        self.__department = department

    def get_department(self):
        return self.__department

    @classmethod
    def increase_dr(cls):
        cls.dr_sum += 1


class Patient(Person):
    pass


# Examples
hospital_departments = ["Operation Theatre Complex (OT)", "Pharmacy Department", "Radiology Department (X-ray)",
                        "Dietary Department", "Physical Medicine and Rehabilitation Department"]

dr1 = Doctor("Adaline ", "Rachel", "+6525148744", "Operation Theatre Complex")
dr2 = Doctor("Roscoe ", "Johns", "+655857744", "Physical Medicine and Rehabilitation Department")

p1 = Patient("Emmett ", "Leaseback", "+6585148747")
p2 = Patient("Keegan ", "Thiel", "+675859540")

hospital = Hospital("Clarissa Care", "Swaziland ", hospital_departments, [dr1, dr2])
print("Welcome To: " + hospital.get_name())
hospital.add_department("Paramedical Department")

hospital.get_departments()
hospital.get_doctors()

hospital.take_appointment(p1, dr2, date.today())
hospital.take_appointment(p2, dr2, date.today())
hospital.take_appointment(p2, dr1, date.today())
hospital.take_appointment(p1, dr1, date.today())

hospital.get_appointment()
