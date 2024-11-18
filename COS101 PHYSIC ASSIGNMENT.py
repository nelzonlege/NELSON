#physics formular

def weight (mass,acceleration):
    return  mass * acceleration

def force (mass ,acceleration):
    return mass* acceleration

def momentum(mass,velocity):
    return mass* velocity

def Density(mass,velocity):
    return mass * velocity

def potential_energy(mass,gravity,height):
    return mass * gravity * height

# main program
def main():
    print("pysics and maths formular")
    print("COS 101 ASSIGNMENT #ANTHONY NELSON#")
    while True:
        print("#options:")
        print("1. physics")
        print("QUIET")

        choice = input("enter your choice")

        if choice == "1":

            print("\n  options:")
            print("1.Weight")
            print("2. force")
            print("3.momentum")
            print("4. Density")
            print ("5. potential energy")
            physics_choice = input ("enter your physics option:")

            if physics_choice == "1":
                mass= float(input("Enter mass (kg):"))
                acceleration= float(input("enter acceleration(m/s):"))
                print(f"Weight :{Weight(mass,acceleration)}g")
                return  mass * acceleration

            elif physics_choice == "2":
                mass =float(input("Enter mass(kg):"))
                acceleration=float(input("Enter acceleration(m/s^2)"))
                print(f"force:{force(mass,acceleration)}N")
                return(mass*acceleration)

            elif physics_choice == "3":
                mass =float(input("Enter mass(kg):"))
                velocity=float(input("Enter velocity (m/s)"))
                print(f"momentum:{momentum(mass,velocity)}kg*m/s")
                return(mass*velocity)

            elif physics_choice == "4":
                mass =float(input("Enter mass(kg):"))
                volume=float(input("Enter volume(m^3)"))
                print(f"power:{power(mass,volume)}N")
                return(mass*volume)

            elif physics_choice == "5":
                mass =float(input("Enter mass(kg):"))
                gravity=float(input("Enter gravity(g)"))
                height=float(input("Enter height(m)"))
                return(mass*gravity* height)
            else:
                print("invalid physics option.")


        elif choice == "2":
            print("ANTHONY NELSON WORK\n bhu/24/04/05/0016\n THANK U")
            break
        else:
            print("invalid choice. please reload.")

if __name__=="__main__":
 main()





