'''This program declares a class describing a favorite animal. I created a class and
then declared the class in a main function with an animal I think is goofy. I did not
use all the real values for the animal however.'''

# This is the fav_animal class
class fav_animal():
    # This function assigns user-inputted data values into variables used for later
    def __init__(self, name, arm_length, leg_length, num_eyes, tail, furry):
        self.name = str(name)
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.num_eyes = int(num_eyes)
        self.tail = bool(tail)
        self.furry = bool(furry)
    
    # This is an extra function created to print out the data values for the favorite animal
    def anim_print(self):
        print("name :", self.name, "\narm length :", self.arm_length)
        print("leg_length :", self.leg_length, "\nnumber of eyes :", self.num_eyes)
        print("does it have a tail? :", self.tail, "\nis it furry? :", self.furry)

# I decided to create a main function to use the fav_animal class and put in my favorite animal through there
def main():
    hippo = fav_animal("hippo", 704, 705, 2, True, False)
    hippo.anim_print()

if __name__ == '__main__':
    main()