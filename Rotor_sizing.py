import math
## Rotor sizing equation. for a given thrust find rotor size

def VTOL_calc(weight, num_rotors, accel_v):
    hover_thrust = weight/num_rotors*9.8
    accel_thrust = (accel_v * weight)/num_rotors + hover_thrust
    return accel_thrust

def size_rotor(Thrust, Prop_area, Prop_efficiency, rho=1.204):

    # Wikipedia, stationary open rotor equation for thrust
    Power = math.sqrt((Thrust**3)(2*rho*Prop_area))

    P_engine=Power/Prop_efficiency


def Rotor_speed_check(rpm, R, speed_of_sound=343):
    # R = radius of rotor in metres
    tip_speed=rpm*60*2*math.pi*R
    if tip_speed >= speed_of_sound:
        # This should really be an exception.
        print("tip speed of rotor exceeds speed of sound. Speed is: ", tip_speed)

        max_size_rotor = speed_of_sound/(rpm*60*2*math.pi)
        print("Rotor must be smaller than:", max_size_rotor)

        max_rotor_rpm = speed_of_sound/(60*2*math.pi*R)
        print("Alternatively, RPM must be below:",max_rotor_rpm)
    else:
        print("Rotor max speed is:", tip_speed)

    return tip_speed
